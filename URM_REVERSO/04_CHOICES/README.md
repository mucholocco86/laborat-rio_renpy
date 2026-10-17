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
