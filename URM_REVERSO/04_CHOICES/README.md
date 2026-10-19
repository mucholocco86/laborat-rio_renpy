# Choices — sistema completo identificado até agora

## Estado da investigação

A análise do sistema de Choices avançou de uma simples identificação de `ChoicesClass` para um modelo arquitetural mais completo: **AST/Choice estrutural**, **estado dinâmico**, **seleção real**, **checkpoint**, **rollback**, **Context** e **estrutura interna dos blocos AST** são canais relacionados, mas não são a mesma coisa.

Documentos detalhados desta etapa:

- `01_FLUXO_CHOICE_ROLLBACK.md` — fluxo da Choice desde a detecção no `renpy.ast.Menu`, passando pela seleção via `ChoiceReturn`, execução pelo Ren'Py, observação de alterações pelo `StoreMonitor` e retorno por rollback.
- `02_LIMITES_E_CASOS_ESPECIAIS.md` — limites, Choices ocultas, texto substituído versus valor real, `jumpTo`, CodeView, fixed rollback, Skip e regras de preservação para o Wells.
- `03_AST_MENU_BLOCOS_CALL_IF_JUMP.md` — estrutura real de `Menu.items`, blocos de Choice, `If.entries`, diferença entre `Call` e `Jump`, operações visuais separadas e limite estrutural de `URMChoice.jumpTo`.
- `06_CONTEXT_ROLLBACK_EXECUTION_7_4_11.md` — relação entre `Context`, `RollbackLog`, restauração do contexto, `current`, `Context.run()`, `RestartContext`, fixed rollback e retomada da execução do AST no Ren'Py 7.4.11.
- `07_URM_CHOICE_INFORMATION_PROJECTION.md` — `Menu.items` como fonte estrutural, `URMChoice` como camada de interpretação/projeção e distinção entre estrutura, estado, execução e apresentação.
- `08_FLUXO_EXECUCAO_BLOCO_CHOICE_IF_CALL_JUMP.md` — distinção entre próximo nó, destino direto, caminhos possíveis, caminho atualmente executável e consequências ao analisar `If`, `Call` e `Jump` dentro de uma Choice.
- `09_MENU_ROLLBACK_FORCE_E_CONTINUIDADE_BLOCO.md` — descoberta de que `Menu` possui `rollback = "force"` por padrão e análise da relação entre política de rollback, `Menu.execute()`, `Menu.next` e a continuidade dos blocos de Choice.
- `10_URM_CHOICES_COMO_PROJECAO_DA_INTERACAO_NATIVA.md` — fecha a ponte entre `Menu.items`, `URMChoice`, `MenuEntry`, `ChoiceReturn`, a Choice Screen e a interação nativa; incorpora o aprendizado do protótipo experimental e define a base mínima segura para um primeiro Walkthrough somente-leitura.

## Núcleo

`classes/choices.rpy` contém `ChoicesClass`.

`isDisplayingChoice` consulta o nó atual pelo contexto/script e verifica `renpy.ast.Menu`.

`currentChoices` percorre `script.items` e cria objetos `URMChoice` para os itens válidos.

`hiddenCount` conta escolhas não visíveis.

## URMChoice

O item é tratado como tupla com:

```text
item[0] → texto da Choice
item[1] → condição
item[2] → lista de nós AST da alternativa
```

Propriedades importantes:

- `isVisible` avalia a condição em `renpy.store.__dict__`;
- `text` usa `renpy.exports.substitute`;
- `condition` preserva a condição da alternativa;
- `code` usa `CodeView.nodesToCode`;
- `jumpTo` procura o primeiro `renpy.ast.Jump` direto no conteúdo da alternativa.

## Relação Context ↔ Rollback

A análise do SDK 7.4.11 confirmou que o rollback restaura não apenas valores do store, mas também estado de controle associado ao `Context`.

O fluxo consolidado é:

```text
RollbackLog
    ↓
seleciona entradas
    ↓
revlog
    ↓
rb.rollback()
    ↓
restauração do estado/contexto
    ↓
execute_default_statement(False)
    ↓
novo Rollback corrente
    ↓
Context.rollback_copy()
    ↓
RestartContext / RestartTopContext
    ↓
Context.run()
    ↓
AST continua do ponto restaurado
```

`Context` e `RollbackLog` têm responsabilidades diferentes:

```text
Context
  → estado de controle da execução atual

RollbackLog
  → histórico de estados restauráveis
```

O `Context` contém, entre outros dados, `current`, `return_stack`, `dynamic_stack`, `scene_lists`, `rollback`, `info` e `force_checkpoint`.

`RollbackLog.rollback()` usa os contextos associados aos registros restaurados e, ao final, cria um novo registro corrente baseado em `renpy.game.context().rollback_copy()`, seguido de uma reinicialização controlada da execução.

## Fixed rollback

No SDK 7.4.11, `fix_rollback()` estabelece uma `fixed_rollback_boundary`, mas não ativa diretamente `rollback_is_fixed`.

Durante a restauração dos registros em `rollback()`, quando o `Context.current` restaurado alcança essa fronteira, `rollback_is_fixed` passa a `True`.

Portanto:

```text
fix_rollback()
    ↓
define boundary
    ↓
rollback()
    ↓
restore entries
    ↓
reach boundary
    ↓
rollback_is_fixed = True
```

A semântica exata desse estado na seleção programática do URM continua sendo tratada junto com `ChoiceReturn` e o circuito de interação.

## StoreMonitor e checkpoint

O StoreMonitor permanece separado do dono do rollback.

O fluxo confirmado é:

```text
StoreMonitor
      ↓
Context.force_checkpoint
      ↓
Context.run()
      ↓
RollbackLog.force_checkpoint
      ↓
RollbackLog.complete()
      ↓
checkpoint(hard=False)
```

Isso não significa que toda alteração arbitrária de variável gere automaticamente um checkpoint. O caminho confirmado é o callback Python do StoreMonitor solicitando `force_checkpoint`, seguido do processamento nativo do Ren'Py.

## Choice e rollback

O circuito nativo continua sendo:

```text
Menu
 ↓
display_menu()
 ↓
ui.interact()
 ↓
ChoiceReturn
 ↓
checkpoint(rv)
 ↓
bloco escolhido
 ↓
execução AST
```

Se ocorrer rollback posteriormente, o Ren'Py restaura estado/contexto e reinicia a execução. O URM observa esse processo; ele não precisa manter um segundo mecanismo de rollback.

O próprio `Menu` possui `rollback = "force"` no AST 7.4.11. Essa propriedade participa da política de rollback consumida pelo executor e não deve ser confundida com a chamada posterior de `checkpoint(rv)` feita pelo circuito de interação.

## Execução do bloco de uma Choice

Uma alternativa de Menu possui um bloco AST próprio. Esse bloco pode conter Python, diálogo, `If`, `Call`, `Jump` e outras statements.

Portanto:

```text
Choice
 ↓
block AST
 ↓
execução dos nós
```

não equivale necessariamente a:

```text
Choice → Jump
```

Para análise completa, distinguimos:

```text
destino direto
próximo nó
caminhos possíveis
caminho atualmente executável
consequências efetivamente produzidas
```

`URMChoice.jumpTo` cobre somente uma pequena projeção dessa estrutura.

## Replay

`renpy.call_replay()` cria uma execução separada com novo `Context`, novo `RollbackLog` e stores preparados para replay. Ao terminar, o contexto de replay é removido e o log/store do jogo principal é restaurado.

Portanto:

```text
Jump
  → continua no contexto atual

Replay
  → cria uma bolha de execução separada
```

## Invariante arquitetural vs. detalhe de versão

Os mecanismos acima são **confirmados para Ren'Py 7.4.11**.

Não devemos assumir que nomes, campos, classes ou sequência interna sejam idênticos em SDKs posteriores. A futura comparação entre SDKs deverá separar:

```text
princípio arquitetural
        ×
implementação específica da versão
```

Essa separação será especialmente útil para investigar a fronteira de compatibilidade observada entre Ren'Py 8.5.2 e 8.5.3.

## Regra de preservação

Primeiro entender → depois inspecionar → depois planejar → só então modificar.

O objetivo continua sendo completar a árvore do URM antes de decidir o que será transplantado para o Wells Framework.

## Continuação de 2026-10-13 — identidade e índice da Choice

A nova análise [11 — Menu, Choice Screen e integridade da seleção](11_MENU_CHOICE_SCREEN_CORRELACAO_E_INTEGRIDADE_DA_SELECAO.md) aprofunda o documento 10: a posição original `i` de `Menu.items` é preservada em `URMChoice` e é o valor usado pela seleção nativa para resolver o bloco AST. A interface visual pode omitir/transformar entradas; não se deve tratar seu índice visual ou texto exibido como identificador estrutural universal.

**Questões pendentes:** menus com `condition=False`, legendas, alternativas com rótulos duplicados, `set`, tradução, argumentos por item e testes após rollback. Essas questões devem ser investigadas por leitura e experimentação controlada, preservando a separação entre observação, hipótese e prova.


## Continuação de 2026-10-16 — validação SDK e rollback

O documento [15 — Validação no SDK 7.4.11: ChoiceReturn, checkpoint, store e rollback](15_VALIDACAO_SDK_CHOICERETURN_CHECKPOINT_ROLLBACK.md) confirma por inspeção estática o caminho Menu → valor estrutural → ChoiceReturn → checkpoint → deltas de StoreDict → restauração de estado e Context. Também localiza RollbackLog em renpy/python.py.

A relação entre o relato de edição manual e o instante exato em que o rollback a desfaz continua pendente de runtime, assim como save/load e fixed rollback.

## Continuação de 2026-10-16 — CodeView e edição de variáveis

O documento [16 — CodeView, busca e edição de variáveis ligadas a Choices](16_CODEVIEW_BUSCA_EDICAO_VARIAVEIS.md) rastreia Choice.code → CodeView → hyperlink de variável → URM_modify_value → SetVarValue → store ativo. Registra os limites dos padrões regex e separa essa mutação dos metadados guardados em .urm.


## Continuação de 2026-10-16 — mutações de variáveis e objetos revertíveis

O documento [17 — Edição de itens, mutações de objetos e rollback](17_EDICAO_ITENS_MUTACOES_OBJETOS_ROLLBACK.md) cruza `Var.setValue`, `CreateVar`, exclusão de variáveis e edição de itens de listas/dicionários com `RevertableList`/`RevertableDict` e `RollbackLog.complete()/rollback()` do SDK 7.4.11. A evidência é estática. Permanecem pendentes testes de runtime do URM e o alcance do `StoreMonitor` em mutações aninhadas.


## Continuação de 2026-10-16 — callback Python e checkpoints

O documento [18 — Callback Python, construtores revertíveis e edição pela screen](18_CALLBACK_PYTHON_E_CHECKPOINTS_URM.md) localiza a chamada de python_callbacks em ast.Python.execute(), rastreia a transferência adiada de Context.force_checkpoint ao RollbackLog e confirma em minstore.py que os nomes especiais são ligados a RevertableList/RevertableDict. A mutação interna de container depende do log de objetos; o delta de StoreDict não é um snapshot do conteúdo.


## Continuação de 2026-10-16 — fechamento do estado antes do rollback

O documento [19 — Fechamento do estado corrente antes do rollback](19_FECHAMENTO_ESTADO_ANTES_ROLLBACK.md) confirma que exports.rollback() chama RollbackLog.complete() imediatamente antes da restauração. O log então coleta deltas do StoreDict e snapshots dos objetos mutados. Também esclarece que o checkpoint solicitado pelo StoreMonitor é soft (hard=False), não uma barreira rígida ao rollback. A aplicação exata a ações do URM segue pendente de runtime.


## Continuação de 2026-10-16 — edição manual e save nativo

O documento [20 — Edição manual e save nativo: raízes e ciclos do StoreDict](20_EDICAO_MANUAL_SAVE_NATIVO_E_ROOTS.md) detalha loadsave.save → RollbackLog.freeze → complete(False) → roots/log serializados. get_roots usa ever_been_changed, atualizado em ciclos cycle=True. Isso identifica casos que precisam ser testados ao salvar imediatamente após editar/criar variável pela screen; não conclui que haja perda de dados. O arquivo .urm permanece separado do save nativo.


## Continuação de 2026-10-16 — retorno da ação URM e condições do Menu

O documento [21 — Propagação da ação do URM e condições do Menu](21_PROPAGACAO_ACAO_URM_E_CONDICOES_MENU.md) acompanha o retorno não-None da ação Select pela interação Ren'Py até o índice estrutural consumido por `Menu.execute`. A análise estática indica uma possível seleção de alternativa cuja condição é falsa, pois não encontrou revalidação do índice após a interação; a integração de tela e o comportamento ponta a ponta continuam pendentes de teste runtime.


## Continuação de 2026-10-16 — runner e limites da validação runtime

O documento [22 — Runner de teste Ren'Py 7.4.11: encerramento e limite da evidência runtime](22_RUNNER_TESTE_RENPY_ENCERRAMENTO_E_EVIDENCIA_RUNTIME.md) registra que o runner deixa o processo ativo quando a testcase termina com node vazio. A fixture passou a encerrar explicitamente o engine depois das asserções, e o workflow agora limita ambos os comandos. O baseline nativo e a fixture de seleção forçada passaram em runtime no Ren'Py 7.4.11 (run 38946951166). A fixture adicional também alterou um valor de store de 10 para 99 e, após checkpoint e rollback, observou o valor restaurado em 10 (run 38947765822). Os dois resultados validam contratos sintéticos do SDK. A integração integral das telas e das ações originais convertidas do URM continua pendente. Uma reprodução reduzida do caminho escalar SetVarValue → Var.setValue passou em runtime no run 38950917699 e restaurou 10 após editar para 99 e executar rollback; limites e detalhes estão no documento 22. Uma prova seguinte passou no run 38973243038: após duas Choices, rollback pela API com force=False restaurou o valor editado (99→10) e os efeitos das duas alternativas (rota 2→0). Isso ainda não simula a tecla/botão de rollback do jogador; veja os limites no documento 22. A entrada `type PAGEUP` no harness passou em runtime no run 38978993727: após edição e duas Choices, as amostras foram 99/2 → 99/2 → 99/1 → 10/0; a contagem é específica da fixture. Veja documento 22.


A extensão mais recente de [22](22_RUNNER_TESTE_RENPY_ENCERRAMENTO_E_EVIDENCIA_RUNTIME.md) passou no run **38979502224**: depois de gravar save nativo com a variável editada em 99, o fixture mudou o valor para 123 e carregou o slot; o runtime observou 99 novamente. Isso comprova somente, para o caso escalar raiz reduzido, que a edição já existente no instante do save entrou no estado nativo serializado. O marcador do harness foi movido para o módulo do runner após a primeira tentativa ter sido reiniciada pelo próprio load. Containers, variáveis criadas, StoreMonitor, variáveis congeladas e URM integral seguem pendentes.


A validação de container também passou no run **38979672209**: a ação reduzida de URM_add_item acrescentou 20 a uma lista Ren'Py ([10] → [10, 20]); depois de duas Choices e rollback com force=False, a lista voltou a [10] e a rota a 0. A evidência cobre o caso de lista revertível compilada pelo Ren'Py e não demonstra reversibilidade de qualquer objeto/container nem notificação pelo StoreMonitor. Detalhes e limites no documento 22.


A edição de item em dicionário também passou no run **39013297447**: a ação reduzida baseada em Var.getChild/SetVarValue mudou a chave a de 10 para 20; após duas Choices e rollback com force=False, o runtime observou o valor 10 e a rota voltou a 0. O teste usa um dict literal Ren'Py e não instrumenta o objeto/log diretamente; veja os limites no documento 22. A matriz reduzida cobre agora escalar raiz, append em lista e edição de chave em dicionário.


O run **39013412540** validou também a exclusão de um índice de lista e uma chave de dicionário pela reprodução reduzida de Var.delete: antes do rollback, lista `[20]` e dicionário `{b: 20}`; depois, `[10, 20]` e `{a: 10, b: 20}`. As duas mutações e os efeitos das Choices foram restaurados. A matriz runtime e seus limites estão no documento 22.


O run **39064784962** validou na reprodução reduzida a regra de truthiness de CreateVar: valores convertidos para inteiro 0, boolean False e string vazia não foram criados; o inteiro 7 foi aceito. A fonte convertida também prevê 0.0 como rejeitado, mas esse valor ainda não foi testado em runtime. Isso é separado da edição de valores existente. Ver limites e classificação no documento 22.


O run **39064935980** validou save/load nativo de containers editados: uma lista salva como `[10, 20]` e um dicionário como `{a: 20}` foram alterados depois para `[10, 20, 30]` e `{a: 30}`; o load restaurou os conteúdos do momento do save. O teste é reduzido e usa literais Ren'Py; não valida objetos externos nem metadados `.urm`. Detalhes no documento 22.


### StoreMonitor: hook e edição direta (2026-10-18)

A análise estática separou o callback `python_callbacks` do hook que o StoreMonitor instala no helper nativo `_m1_00action_data__set_field`/`_set_field`. `SetVariable` passa pelo helper; o `Var.setValue` convertido usa atribuição direta via `exec`, e `CreateVar` usa `setattr`. Logo, o hook não deve ser atribuído automaticamente às ações de edição próprias do URM. A fixture runtime contrapõe esses caminhos, mas o run estava pendente/em execução na revisão; veja [documento 23](23_STOREMONITOR_INTERCEPTACAO_E_EDICAO_URM.md) para fontes e status.


A execução **39098070978** concluiu **SUCCESS** para o contraste do helper de atribuição. Na fixture reduzida, a ação nativa `SetVariable` chamou o helper uma vez (contador 1, valor 20); a ação reduzida `SetVarValue` mudou para 30 sem incrementar o contador. Isso confirma a diferença de rota no ambiente do teste, sem equivaler a integração completa do URM. Detalhes e logs em [documento 23](23_STOREMONITOR_INTERCEPTACAO_E_EDICAO_URM.md).


### Callback após edição por screen — runtime (2026-10-18)

No run [39098269040](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39098269040), a ação da screen mudou o valor 10→99 sem incrementar o contador do callback; ao fim do primeiro nó Python posterior, o callback observou o novo valor e o delta anterior 10. O testcase usou rollback desabilitado, portanto não confirma a transferência de `force_checkpoint` ao log em gameplay. A evidência e os limites estão no [documento 24](24_CALLBACK_SCREEN_EDIT_RUNTIME.md).


### Callback com rollback habilitado — restauração verificada (2026-10-18)

O run [39098551052](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39098551052) repetiu a edição por screen com rollback habilitado. A fixture observou valor 99 após a edição; o callback Python posterior não encontrou o delta do alvo em **StoreDict.get_changes(False)**, enquanto **RollbackLog.force_checkpoint=True**. Depois, o rollback explícito restaurou o valor a 10. Isso demonstra, para o escalar raiz da fixture reduzida, que a ausência do delta naquele callback não significa que a alteração esteja fora do histórico reversível. A explicação provável é a ciclagem anterior do StoreDict pelo caminho de checkpoint/registro; a fixture não instrumenta todas as estruturas internas do RollbackLog e não é integração completa do URM. Fontes, log e limites no [documento 25](25_CALLBACK_ROLLBACK_STOREDELTA_GAMEPLAY.md).


### Freeze, monitor e watch — distinção estática (2026-10-18)

A leitura de **classes/vars.rpy** e **screens/vars.rpy** separou três mecanismos do URM: freeze e monitor são flags no store **vars** e aceitam apenas variáveis escalares raiz segundo os predicados convertidos; watch usa o store **watched** e alimenta o painel de observação. **Var.setValue** remove temporariamente freeze, realiza a edição direta e volta a aplicar freeze, o que permite a edição feita pelo próprio URM. O hook SetField e o callback Python são caminhos de detecção diferentes; quando uma edição direta vira notificação depende do delta disponível ao callback. Esta etapa é estática e deixa a validação runtime em aberto. Detalhes, símbolos e pendências no [documento 26](26_FREEZE_MONITOR_WATCH_EDICAO_URM.md).


### Freeze em runtime — edição nativa, URM e callback (2026-10-18)

O probe [39104245128](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39104245128) passou. Na fixture reduzida, a escrita nativa foi bloqueada com valor 10 frozen; a edição direta SetVarValue mudou para 30 e manteve freeze; no callback seguinte, que ainda tinha o delta 10→30, o handler restaurou 10 e conservou freeze. Essa restauração foi observada com rollback desabilitado. O caso de rollback habilitado permanece pendente porque o callback pode não receber o delta, como observado no documento 25. Ver [documento 27](27_FREEZE_RUNTIME_EDICAO_E_CALLBACK.md) e revisão do modelo estático no [documento 26](26_FREEZE_MONITOR_WATCH_EDICAO_URM.md).


### Freeze com rollback habilitado (2026-10-18)

O segundo probe de freeze também passou no run [39104385145](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39104385145). A escrita nativa continuou bloqueada em 10; a edição URM reduziu o valor para 30 e reaplicou freeze; desta vez o callback posterior não recebeu o delta, então o valor permaneceu em 30 até o rollback explícito, que restaurou 10. Isso reproduz, para uma variável escalar e uma fixture reduzida, a relação relatada entre edição durante a execução e rollback para um estado anterior. O metadado frozen do URM real não foi validado; ver [documento 28](28_FREEZE_ROLLBACK_RUNTIME.md).


### Monitor de variáveis e notificações — runtime (2026-10-18)

O run [39148026518](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39148026518) comparou SetVariable nativo e SetVarValue direto. No teste reduzido, a escrita nativa gerou uma notificação síncrona pelo hook; a edição direta não notificou durante a ação, mas foi detectada pelo callback posterior quando o delta estava disponível. Sem rollback, o callback simplificado processou repetidamente o mesmo delta não ciclado, acrescentando registros duplicados no harness. Isso levanta uma hipótese de duplicação no StoreMonitor, ainda sem confirmação no URM integral ou em gameplay com rollback. Detalhes e classificação no [documento 29](29_NOTIFICACOES_VARIAVEIS_MONITORADAS_RUNTIME.md).


### Monitor URM com rollback habilitado (2026-10-18)

No run [39148219484](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39148219484), a edição direta SetVarValue de variável monitorada foi para 30, não passou pelo hook nativo e não produziu aviso no contexto testado. O callback posterior não encontrou o delta; o rollback explícito restaurou o valor a 10. Isso mostra que a restauração do estado do jogo pode ocorrer sem notificação do StoreMonitor reduzido naquele instante. A integração completa e a escrita nativa sob rollback continuam pendentes. Ver [documento 30](30_MONITOR_ROLLBACK_NOTIFICACAO_URM.md).


O contraponto nativo com rollback habilitado também passou no run [39148594202](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39148594202): SetVariable gerou aviso imediato 10→20 pelo hook e o rollback restaurou a variável a 10. O coletor de avisos da fixture foi limpo pelo rollback porque era uma lista reversível do store; isso não prova que a lista interna da NotificationClass do URM seja revertida. A comparação está consolidada no [documento 30](30_MONITOR_ROLLBACK_NOTIFICACAO_URM.md).


### Notificações do URM e rollback — ciclo de vida

O documento [31 — Ciclo de vida das notificações do URM e rollback](31_NOTIFICACOES_E_ROLLBACK_CICLO_DE_VIDA.md) identifica `x52NonPicklable` como classe baseada no objeto Python comum e localiza `URM_notifications` em `screens/watchpanel.rpy`. O SDK 7.4.11 filtra snapshots de objetos por alcance a partir das raízes alteradas e dos displayables ativos. Nos runs [39156621298](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39156621298) e [39156808878](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39156808878), as fixtures reduzidas observaram: singleton init-only sem raiz alterada manteve a lista com 1; referência raiz alterada ou screen visível com `action notif` levou a lista de volta a 0 após rollback. A screen real e o pacote URM completo ainda não foram executados. A hipótese de que a overlay real alcance a lista está fortemente apoiada pela correspondência estrutural, mas permanece inferência. Pendências: rollback antes do novo render, timeout/thread, save/load e integração ponta a ponta. Os probes `urm_x52_notification_clear_rollback` e `urm_x52_notification_remove_rollback` agora comparam a substituição de atributo feita por `clear()` com a mutação in-place de `RevertableList.remove()`, sob screen visível e checkpoint equivalente. Fixture commit [37deb35335fec1fb140ab6b26e565ac7bdd6ab3e](https://github.com/mucholocco86/laborat-rio_renpy/commit/37deb35335fec1fb140ab6b26e565ac7bdd6ab3e); workflow commit [537a46dcbc98ae76af80464efc7ae8582aa62eaa](https://github.com/mucholocco86/laborat-rio_renpy/commit/537a46dcbc98ae76af80464efc7ae8582aa62eaa). O run runtime [39205520906](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39205520906) concluiu os dois probes: `clear()` deixou a lista vazia após rollback (screen ativa), enquanto `remove()` restaurou o item (screen ativa). Isso foi observado na fixture reduzida, não no URM integral. A causa das falhas anteriores foi rollback não habilitado nos dois labels; detalhes, logs e limites estão no documento 31.


A análise estática do timeout, também registrada no [documento 31](31_NOTIFICACOES_E_ROLLBACK_CICLO_DE_VIDA.md), confirmou que a remoção automática ocorre dentro da thread de `renpy.invoke_in_thread`. O SDK limita as operações esperadas nessa thread; `RevertableList.remove()` também grava no mapa de mutações do rollback. `RollbackLog.complete` tenta novamente se esse mapa muda durante a iteração, mas isso não comprova suporte semântico ou segurança para o padrão do URM. O run [39205520906](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39205520906) passou no probe de timeout: a lista voltou a 1 após rollback, e a flag do worker retornou a `False`. É um resultado do harness reduzido num agendamento controlado, não validação integral do URM nem garantia geral de concorrência.


Foi incluído também o testcase `urm_x52_notification_timeout_rollback` para medir uma remoção de `RevertableList` dentro de `renpy.invoke_in_thread`, seguida por rollback ao checkpoint anterior. Fixture commit [b4de1e4c476668f27da51775c48536f82fe16f91](https://github.com/mucholocco86/laborat-rio_renpy/commit/b4de1e4c476668f27da51775c48536f82fe16f91); workflow commit [4ffdae65e48c42dad9c314c62fd1c68b78e78c63](https://github.com/mucholocco86/laborat-rio_renpy/commit/4ffdae65e48c42dad9c314c62fd1c68b78e78c63). O run [39205520906](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39205520906) concluiu com sucesso: o item removido pela thread retornou após rollback. O probe é reduzido e não demonstra determinismo em outros agendamentos.

A revisão estática do save/load no documento 31 localizou outra pendência: o SDK salva roots do store e RollbackLog, enquanto o singleton de notificações é criado em init e sua classe customiza o estado de serialização para não restaurar atributos. O SDK cria o backup limpo depois do init, quando o singleton URM já foi criado; cópias rasas do StoreBackup mantêm sua referência sem copiar a lista interna. Snapshots do RollbackLog ainda podem restaurá-la quando alcançável, por exemplo via screen. A reconstrução de ScreenDisplayable deixa aberta a forma como a screen relê o estado. O primeiro roundtrip reduzido [39214784786](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39214784786) carregou na mesma sessão e manteve `Post-save notification` após o teste substituir a lista depois do save; isso sugere que o atributo do owner Python comum não foi restaurado nessa rota. O resultado não valida o URM integral e ainda requer comparação com mutação in-place e processo novo; ver limitações no documento 31.


**Save/load de notificações em processo novo — run 39215564208:** o processo que criou o save registrou a lista com `Saved notification`; ao carregar o mesmo slot em outro processo, o singleton iniciado por `init` tinha lista vazia antes e depois do load, embora a screen de probe aparecesse ativa. Isso é evidência runtime da fixture reduzida; não esclarece se os displayables/action guardados pela screen apontam para objetos salvos nem comprova o comportamento do pacote URM integral. A interpretação de que o singleton init-only ficou fora das roots serializadas permanece hipótese. Ver [documento 31](31_NOTIFICACOES_E_ROLLBACK_CICLO_DE_VIDA.md).


**Reconstrução da screen após load — run 39229685100:** o fixture consultou o widget identificado após load em processo novo. A screen existia, mas o botão de notificação não; a asserção passou. O SDK 7.4.11 exclui os widgets filhos do estado serializado e os reconstrói executando novamente a função da screen. Na fixture, essa reconstrução leu o singleton recém-iniciado com lista vazia. Isso fecha a lacuna do probe anterior, mas ainda não valida a screen do pacote URM integral. Fontes, linhas e limites no [documento 31](31_NOTIFICACOES_E_ROLLBACK_CICLO_DE_VIDA.md).


**Callback pós-load do URM — run 39230107907:** `main.rpy` registra `afterLoad` em `config.after_load_callbacks`; o Ren'Py 7.4.11 executa esses callbacks em `_after_load`. `afterLoad` mostra `URM_overlay`, que inclui `URM_notifications`. O fixture reproduziu esse callback em processo novo: callback executado, lista vazia, screen presente e botão da notificação ausente. Esse resultado é runtime da fixture reduzida, não prova do pacote URM integral. Fontes e limites no [documento 31](31_NOTIFICACOES_E_ROLLBACK_CICLO_DE_VIDA.md).
