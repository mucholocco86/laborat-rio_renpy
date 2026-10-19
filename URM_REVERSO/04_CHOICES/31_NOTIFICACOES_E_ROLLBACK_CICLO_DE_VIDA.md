# 31 — Ciclo de vida das notificações do URM e rollback

**Data:** 2026-10-18  
**Escopo:** revisão estática da lista interna de notificações e confronto com o rollback de objetos do Ren'Py 7.4.11.  
**Runtime:** nenhuma execução da NotificationClass/tela real nesta etapa. Os probes dos documentos 29–30 usam coletores reduzidos.

## Achado principal

O coletor de avisos usado nos probes anteriores não reproduz a estrutura de armazenamento do URM. O harness guardava notificações numa lista de store criada por `default`; essa lista é uma raiz direta do rollback. No URM convertido, os avisos ficam em `NotificationsClass.notifications`, atributo de uma instância criada em init.

A diferença impede concluir, a partir do coletor que foi limpo no rollback, que a lista real do URM também é revertida.

## Fluxo identificado na fonte URM convertida

1. `classes/notifications.rpy`, `NotificationsClass.__init__` inicializa `self.notifications = []`.
2. `classes/main.rpy`, no bloco `init 52 python in x52URM`, instancia `Notifications = NotificationsClass()`.
3. `NotificationsClass.add` cria um `Notification`, acrescenta-o à lista e chama `renpy.restart_interaction()`. Se `Settings.notificationTimeout` estiver ativo, uma thread aguarda e tenta remover o aviso.
4. `remove` remove o aviso e reinicia a interação; `clear` substitui a lista por uma lista vazia.
5. `screens/main.rpy` inclui `use URM_notifications` dentro de `URM_overlay`. A definição dessa screen não foi localizada ainda; não se conclui aqui sua política de renderização, descarte ou reconstrução.

**CONFIRMADO NA FONTE URM CONVERTIDA:** os pontos 1–5 correspondem ao código convertido. A conversão não é, por si só, prova de identidade perfeita com o pacote original.

## Confronto com o SDK 7.4.11

### Literais de lista

Em `renpy/python.py`, `py_compile` aplica `wrap_node.visit(tree)`. O transformador `WrapNode.visit_List` substitui literais de lista em contexto de leitura por chamadas a `__renpy__list__`; `minstore.py` liga esse nome a `RevertableList`.

Assim, o literal `[]` da classe compilada como código Ren'Py é convertido para a estrutura revertível do SDK. `RevertableList.append` usa o wrapper de mutação, que registra o estado limpo no log quando a lista é alterada. A compilação no escopo `init python in x52URM` e o tipo efetivo em runtime devem ser confirmados na fixture antes de afirmar o resultado para o pacote carregado integralmente.

### Alcance do rollback por grafo de objetos

`renpy.python.reached` interrompe a travessia quando encontra uma instância de `NoRollback`: marca o objeto como não participante e não percorre seus atributos nesse caminho. O código do SDK ressalva que objetos alcançáveis por outra raiz independente ainda podem participar.

Esse mecanismo torna a classe-base de `NotificationsClass` decisiva. A fonte convertida declara `NotificationsClass(x52NonPicklable)` e `Notification(x52NonPicklable)`, mas a definição de `x52NonPicklable` não foi localizada nas fontes atualmente examinadas. O nome não basta para equipará-la a `renpy.python.NoRollback`.

### Implicação condicional

- **CONFIRMADO NO SDK 7.4.11:** quando um objeto alcançado é `NoRollback`, a travessia não visita seus atributos por esse caminho.
- **PENDENTE:** se `x52NonPicklable` herda de `NoRollback`, a lista interna e seus avisos podem ficar fora do rollback por intermédio de `Notifications`, salvo se houver outra raiz que os alcance.
- **PENDENTE:** se a classe-base não é `NoRollback`, a lista revertível pode ser capturada e restaurada segundo o alcance e as mutações registradas no ciclo correspondente.
- Não há evidência nesta etapa para afirmar se avisos persistem ou desaparecem após rollback, nem se o timeout em thread afeta esse resultado.

## Por que o coletor de teste não responde sobre o URM

No run [39148594202](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39148594202), o harness registrou o aviso imediato de `SetVariable` e o rollback restaurou a variável. O próprio coletor, por ser uma lista reversível na store da fixture, foi restaurado ao estado anterior. Isso valida o coletor do teste, mas não o atributo aninhado da NotificationClass do URM.

Essa limitação se aplica também ao teste reduzido do documento [29](29_NOTIFICACOES_VARIAVEIS_MONITORADAS_RUNTIME.md) e ao documento [30](30_MONITOR_ROLLBACK_NOTIFICACAO_URM.md).

## Classificação

- **CONFIRMADO NA FONTE URM CONVERTIDA:** Notifications é instanciada durante init; avisos são adicionados/removidos em um atributo de lista; o overlay inclui a screen de notificações.
- **CONFIRMADO NO SDK 7.4.11:** literais de lista compilados pelo pipeline Ren'Py são transformados em `RevertableList`; mutações de lista podem entrar no log de objetos; a travessia para em `NoRollback`.
- **OBSERVADO EM RUNTIME (fixture reduzida):** o coletor de avisos raiz do probe foi revertido junto com a variável no rollback.
- **HIPÓTESE:** o armazenamento real de avisos pode ter ciclo de vida diferente por estar aninhado em `Notifications` e depender da base `x52NonPicklable`.
- **PENDENTE:** definição de `x52NonPicklable`, implementação da screen `URM_notifications`, tipo real da lista e execução add → rollback → screen/timeout.

## Fontes consultadas

| Fonte | Símbolos / intervalo | Identificação |
|---|---|---|
| URM convertido `classes/notifications.rpy` | linhas 1–39; `NotificationsClass`, `Notification` | blob SHA `3283ec4b1615967a71ad21cc34670bf8158ab96d` |
| URM convertido `classes/main.rpy` | linhas 10–42; instanciação `Notifications` em init 52 | blob SHA `14f93406d2946eaed664ed72c1d47063984ce24f` |
| URM convertido `screens/main.rpy` | linhas 20–53; `URM_overlay` usa `URM_notifications` | blob SHA `ceb5dc63b3691a4b6244345e1c5a3e3b9d149291` |
| Ren'Py 7.4.11 `renpy/python.py` | linhas 354–405 (`NoRollback/reached`), 453–506 (`WrapNode`), 723–835 (`py_compile`), 953–1048 (`RevertableList`) | blob SHA `c5eb2819a3e4ee096dbf01130d70a77f9b623484` |
| Ren'Py 7.4.11 `renpy/minstore.py` | `__renpy__list__ = RevertableList` | blob SHA `5dd44affc52aeb10a9c28433baee0b9948d3f759` |

## Próximos passos

1. Localizar a definição de `x52NonPicklable` no loader/dependências do URM e verificar sua relação efetiva com `NoRollback`.
2. Localizar a declaração de `URM_notifications` e suas ações de remoção/fechamento.
3. Fazer fixture isolada que use a mesma classe-base confirmada e o pipeline Ren'Py; observar type/list identity e add → checkpoint → rollback → renderização.
4. Separar os resultados de rollback do estado de jogo dos efeitos visuais/temporais da notificação e de seu comportamento em save/load.
5. Só então revisar se o resultado dos probes 29–30 pode ser refinado para o StoreMonitor integral.


## Continuação — definição da base e screen localizadas (2026-10-18)

A revisão da árvore completa localizou os dois itens que faltavam:

- `framework/modules/01utils.rpy`, linhas 10–21, define `x52NonPicklable(python_object)`. Em `renpy/minstore.py`, `python_object = _object = object` é guardado antes de substituir `object` por `RevertableObject`. Portanto, a base do URM é o objeto Python comum; ela **não** é `renpy.python.NoRollback`.
- A classe customiza `__getstate__`, `__setstate__`, `__getnewargs__` e iteração para o protocolo de serialização. Isso não impede a inspeção de atributos pelo algoritmo de alcance: em `renpy/python.py`, `reached` examina `vars(obj).values()` antes de tentar iterar, e captura exceções da tentativa de iteração.
- `screens/watchpanel.rpy`, linhas 260–353, contém `URM_notifications`. A screen percorre `x52URM.Notifications.notifications`, cria um botão para cada aviso (ação `notif`) e oferece `Dismiss all` por `Notifications.clear`. `screens/main.rpy` inclui essa screen no overlay.

**CONFIRMADO NA FONTE URM CONVERTIDA + SDK 7.4.11:** a lista de notificações é alcançável a partir do objeto `Notifications` e a classe-base não interrompe essa travessia como `NoRollback`. O SDK transforma o literal de lista da classe Ren'Py em `RevertableList`; `append` registra mutação. A previsão estática é, portanto, que uma adição rastreável possa ser desfeita pelo rollback.

**Ainda não confirmado em runtime:** a fixture abaixo testa o mesmo formato de grafo e a base equivalente no pipeline do SDK. Ela não importa o pacote URM inteiro nem a própria screen. Até o resultado do workflow, a previsão não deve ser descrita como comportamento observado do URM.

### Nova fixture isolada

Foi acrescentado o testcase `urm_x52_nonpicklable_notification_list_rollback` à fixture e um passo correspondente ao workflow. Ele usa uma classe-base com os mesmos métodos de `x52NonPicklable`, cria a lista por literal em bloco `init python`, acrescenta um objeto de notificação depois de checkpoint e solicita rollback. As asserções verificam o tipo `RevertableList`, a relação negativa com `NoRollback` e a lista vazia após retornar ao checkpoint.

A execução foi disparada pelo push do commit `021a78ffaea993c4f647daf5941e4fc44a5592d8`; **o resultado deve ser registrado após a conclusão do run**. Esta fixture mede semântica do SDK com classe reduzida, não integração integral do URM.

### Referências adicionadas

| Fonte | Símbolos / intervalo | Blob SHA |
|---|---|---|
| URM convertido `framework/modules/01utils.rpy` | linhas 10–21; `x52NonPicklable` | `e558a2d5a5137608e542238a1d81fd65e6db349d` |
| URM convertido `screens/watchpanel.rpy` | linhas 260–353; screen `URM_notifications` e lista de avisos | `8cc83f00838ed409183e85e4ebdb37ddf4433823` |
| URM convertido `framework/bootstrap.rpy` | mapa de módulos; `main` depende de `modules/01utils.x52rpy` | `9d72267c2d86c68aa9dac1fee94652c891a611fe` |
| Fixture runtime | testcase `urm_x52_nonpicklable_notification_list_rollback` | commit `196e17e0cd474620eb21a75aa1237a45a68c9c13` |
| Workflow | passo “Run x52 notification object rollback probe” | commit `021a78ffaea993c4f647daf5941e4fc44a5592d8` |


### Revisão após o primeiro runtime probe — raízes do log

O primeiro probe [39156073470](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39156073470) terminou **FAILURE** porque a asserção esperava lista vazia e a fixture ficou presa procurando a interação textual errada. Antes da falha, o runtime imprimiu:

```text
X52_NOTIFICATION_PRE ProbeNotificationsClass RevertableList 0 False
X52_NOTIFICATION_AFTER_ADD 1 Variable changed
X52_NOTIFICATION_AFTER_ROLLBACK RevertableList 1
```

O marcador após a chamada de rollback indica que a execução chegou à etapa de verificação, mas o testcase não concluiu corretamente. O valor 1 é evidência intermediária; não é, isoladamente, uma prova integral do URM.

A revisão do SDK revelou uma condição que faltava ao raciocínio anterior:

- `RollbackLog.get_roots()` cria raízes a partir de `StoreDict.ever_been_changed`, ou seja, variáveis marcadas como alteradas desde o fim da fase init.
- `RollbackLog.complete()` registra objetos mutados, mas `purge_unreachable()` remove registros de objetos não alcançáveis a partir das raízes e do contexto.
- A instância `Notifications` do URM é atribuída durante `init 52`. A lista pode ser `RevertableList` e registrar o append, mas isso **não basta**: se o objeto dono não for alcançado por uma raiz elegível, o snapshot da lista pode ser descartado.
- Uma referência adicional a `Notifications` guardada numa variável de store alterada em runtime pode tornar o grafo alcançável e mudar o resultado do mesmo append.

Isso concilia a implementação de `x52NonPicklable` com o probe: a classe não interrompe a travessia como `NoRollback`, mas a raiz inicial ainda pode estar ausente de `get_roots()`. A screen em execução pode adicionar caminhos de alcance por displayables/actions; esse caminho ainda precisa de teste e não é inferido só por sua declaração estática.

**Classificação atual:** confirmado no SDK que mutações de objetos são filtradas por alcance; observado em runtime reduzido que o probe sem uma raiz de store alterada manteve a lista em 1 após a tentativa de rollback; hipótese forte que o singleton de init isolado seja descartado do log quando não houver outro caminho alcançável; pendente comparar a raiz init-only com uma raiz adicionada/alterada em runtime e com a screen ativa.

A fixture e o workflow foram ampliados para duas comparações controladas: (a) singleton init-only; (b) a mesma instância também referenciada por variável raiz alterada em runtime antes do checkpoint. O segundo run deve ser consultado antes de concluir a previsão.


### Comparação runtime com checagens explícitas — run 39156621298

O run [39156621298](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39156621298) terminou **SUCCESS**. As duas comparações usaram exceções explícitas em vez de depender de `assert` no código Python da fixture.

**Singleton criado durante init, sem variável raiz alterada:**

```text
X52_NOTIFICATION_PRE ProbeNotificationsClass RevertableList 0 False
X52_NOTIFICATION_AFTER_ADD 1 Variable changed
X52_NOTIFICATION_AFTER_ROLLBACK RevertableList 1
```

O probe terminou com código 0 exigindo que a lista continuasse com uma entrada. Isso confirma no cenário reduzido que a mutação da lista interna do objeto init-only não foi restaurada quando não havia outra raiz considerada.

**A mesma instância referenciada por variável raiz alterada antes do checkpoint:**

```text
X52_NOTIFICATION_ROOTED_AFTER_ADD 1
X52_NOTIFICATION_ROOTED_AFTER_ROLLBACK RevertableList 0 False
```

O probe terminou com código 0 exigindo lista vazia e variável raiz de volta a `None`. A lista foi revertida; a referência temporária também voltou ao valor anterior.

**CONFIRMADO EM RUNTIME (fixture SDK reduzida):** o destino da mutação de uma lista revertível depende de o grafo do objeto ser alcançável pelas raízes do rollback no cenário testado. Isso corresponde ao código do SDK em `RollbackLog.get_roots()` (linhas 1757–1777) e `purge_unreachable()` (1779–1797). O run não carregou URM e não tinha screen ativa; logo, ainda não responde se os displayables/actions da `URM_notifications` real mantêm o singleton alcançável.

O probe final, [39156073470](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39156073470), falhou por expectativa incorreta e interação do teste. O run [39156311306](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39156311306) também falhou porque o diálogo de verificação repetiu o fluxo antes da asserção. Ambos foram substituídos pela fixture com saída direta no label de verificação e checagens explícitas. O run [39156468364](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39156468364) passou, mas usava asserts Python que não eram uma garantia suficiente; seus valores de log coincidiram, e a conclusão é apoiada pelo run 39156621298.

### Screen ativa: comparação concluída

A fixture inclui `urm_x52_notification_overlay_probe`, com um `textbutton` cuja action é o objeto Notification. O run [39156808878](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39156808878) concluiu **SUCCESS**. Os marcadores e a interpretação estão registrados na seção final deste documento.


### Screen ativa como raiz de alcance — run 39156808878

O run [39156808878](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39156808878) terminou **SUCCESS**, incluindo o testcase `urm_x52_displayed_notification_list_rollback`. A fixture exibiu um screen com o mesmo padrão estrutural importante da screen URM: iteração pela lista e botão com `action notif`.

```text
X52_NOTIFICATION_SCREEN_BEFORE_ROLLBACK 1 True
X52_NOTIFICATION_SCREEN_AFTER_ROLLBACK 0 False
```

As verificações explícitas exigiram a lista vazia após rollback. Portanto, o displayable visível que contém a action alcançou o objeto de notificação e sua lista no cenário reduzido; ao voltar ao checkpoint, a lista foi revertida e a screen posterior foi retirada/restaurada conforme o estado do contexto.

### Síntese para o URM

- **CONFIRMADO NA FONTE URM CONVERTIDA:** `Notifications.add` acrescenta Notification à lista; `Notification` guarda referência ao dono `NotificationsClass`; `URM_notifications` percorre essa lista e usa cada objeto como action; `URM_overlay` inclui a screen; `afterLoad` mostra `URM_overlay`.
- **CONFIRMADO NO SDK 7.4.11:** `show_screen` insere `ScreenDisplayable` em `Context.scene_lists`; a purga de objetos do rollback percorre os displayables da scene list. A action do botão é, portanto, um possível caminho de alcance para Notification → NotificationsClass → lista.
- **OBSERVADO EM RUNTIME (fixture reduzida):** sem screen/action ou raiz de store alterada, a lista do singleton init-only permaneceu com um item; com raiz de store alterada ou com screen visível que carrega `action notif`, a lista retornou ao estado vazio no rollback.
- **INFERÊNCIA FORTE, ainda não integração runtime URM:** quando a overlay real já está visível e a notificação foi renderizada como botão, o caminho de alcance da action deve permitir que o rollback desfaça a inclusão. A estrutura fonte da screen real coincide no aspecto relevante, mas ainda falta executar o pacote URM completo.
- **PENDENTE:** testar notificação adicionada e rollback antes da screen concluir um novo render; testar timeout/thread e `clear()`; testar save/load da lista; carregar URM real para validar a hipótese ponta a ponta.

O erro anterior de esperar rollback da lista init-only sem uma raiz ativa estava no modelo inicial, não no SDK. Os runs [39156073470](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39156073470) e [39156311306](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39156311306) foram tentativas de fixture com expectativa/fluxo de interação incorretos; as conclusões agora apoiam-se nas comparações controladas dos runs [39156621298](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39156621298) e [39156808878](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39156808878).

### Novo alvo: `clear()` substitui o atributo (2026-10-18)

A fonte de `classes/notifications.rpy` distingue três operações:

- `add()` chama `self.notifications.append(notif)`;
- `remove()` chama `self.notifications.remove(notif)`;
- `clear()` faz `self.notifications = []`.

A diferença interessa porque o dono `NotificationsClass` herda de `x52NonPicklable`, que por sua vez herda de `python_object` (o `object` nativo preservado por `renpy/minstore.py)), e não de `RevertableObject`. Já os conteúdos são listas revertíveis: mutações como append/remove passam pelo wrapper `mutator`, que guarda um estado limpo no rollback log. Uma substituição de atributo em objeto Python comum não é automaticamente a mesma operação que uma mutação da `RevertableList`.

- **CONFIRMADO NA FONTE URM CONVERTIDA:** `clear()` substitui a referência da lista; `remove()` altera a lista atual.
- **CONFIRMADO NO SDK 7.4.11:** mutadores de `RevertableList` registram snapshot do próprio objeto. O SDK salva a classe nativa `object` como `python_object` antes de mapear `object` para `RevertableObject` no ambiente Ren'Py.
- **HIPÓTESE:** `clear()` pode não ser revertido como `remove()` quando o dono é a instância URM baseada no objeto Python comum. A screen pode restaurar um displayable antigo no contexto, mas isso não restaura necessariamente o atributo `notifications` do dono.
- **PENDENTE DE RUNTIME:** confirmar essa diferença com fixture reduzida e depois com o URM completo.

Foi acrescentado o testcase `urm_x52_notification_clear_rollback` à fixture e o passo “Run x52 notification clear rollback probe” ao workflow. O probe mantém uma screen com action de notificação visível, cria checkpoint, substitui a lista como o método `clear()` faz e retorna ao checkpoint. Commit do passo do workflow: [7cb6f6c5b0e20a9cb0198b3acbfd7dfb3b19a103](https://github.com/mucholocco86/laborat-rio_renpy/commit/7cb6f6c5b0e20a9cb0198b3acbfd7dfb3b19a103). **Resultado runtime ainda pendente; não tratar a previsão acima como observação.**

Para separar os dois mecanismos com condições equivalentes, foi adicionado também `urm_x52_notification_remove_rollback`: começa com uma notificação já alcançável pela screen, cria checkpoint, chama `RevertableList.remove()` no objeto atual e volta ao checkpoint. A expectativa testável é a lista retornar a um item, em contraste com a previsão de `clear()` permanecer vazia. Ambos os probes estão no workflow atualizado; o run de push não está exposto pelo conector disponível, então **os dois resultados seguem pendentes até que os logs do Actions sejam consultados**. A última alteração do workflow é o commit [537a46dcbc98ae76af80464efc7ae8582aa62eaa](https://github.com/mucholocco86/laborat-rio_renpy/commit/537a46dcbc98ae76af80464efc7ae8582aa62eaa), e a fixture foi atualizada no commit [37deb35335fec1fb140ab6b26e565ac7bdd6ab3e](https://github.com/mucholocco86/laborat-rio_renpy/commit/37deb35335fec1fb140ab6b26e565ac7bdd6ab3e).

Fontes adicionais consultadas:

| Fonte | Símbolos | Identificação |
|---|---|---|
| URM convertido `classes/notifications.rpy` | `NotificationsClass.add/remove/clear`, linhas 1–39 | blob SHA `3283ec4b1615967a71ad21cc34670bf8158ab96d5` |
| Ren'Py 7.4.11 `renpy/minstore.py` | aliases `python_object = _object = object`; substituição `object = RevertableObject` | blob SHA `5dd44affc52aeb10a9c28433baee0b9948d3f759` |
| Ren'Py 7.4.11 `renpy/python.py` | `mutator`, `RevertableList` | blob SHA `c5eb2819a3e4ee096dbf01130d70a77f9b623484` |
| Fixture | testcase `urm_x52_notification_clear_rollback` | commit `1f3e253e01c2d713cf3ed72999c0dcfce347c6a1` |
| Workflow | passo de clear rollback | commit `7cb6f6c5b0e20a9cb0198b3acbfd7dfb3b19a103` |


### Timeout em thread e mutação da lista (2026-10-18)

A fonte convertida mostra que, quando `Settings.notificationTimeout` está ativo, `NotificationsClass.add` cria uma função que espera com `time.sleep` e então executa `self.notifications.remove(notif)`; essa função é enviada a `renpy.invoke_in_thread`.

No SDK 7.4.11, `invoke_in_thread` inicia uma thread daemon e reinicia a interação quando ela termina. A documentação da função delimita o que pode ser feito nessa thread: escrita de variáveis do store e `renpy.queue_event` são permitidas; a maior parte das outras APIs deve ficar na thread principal. A remoção não é uma simples atribuição a variável do store: `RevertableList.remove` passa por `mutator`, que acessa `renpy.game.log.mutated`, guarda o estado limpo e altera a lista.

Há um detalhe no rollback log: `RollbackLog.complete` percorre `self.mutated` para comprimir snapshots e tenta novamente até quatro vezes se ocorrer `RuntimeError` por mudança concorrente desse dicionário. Isso demonstra que o SDK reconhece concorrência nessa estrutura; **não prova** que toda mutação revertível em thread seja suportada, segura ou determinística. Também não prova que a remoção por timeout terá o mesmo ponto de rollback que uma remoção executada pela interação principal.

- **CONFIRMADO NA FONTE URM CONVERTIDA:** timeout chama `self.notifications.remove(notif)` dentro da função passada a `renpy.invoke_in_thread`.
- **CONFIRMADO NO SDK 7.4.11:** `invoke_in_thread` usa thread daemon e documenta limites de uso da API; `RevertableList` usa mutator ligado ao log; `RollbackLog.complete` repete a coleta se o mapa de mutações mudar durante a iteração.
- **HIPÓTESE / RISCO A VALIDAR:** timeout e rollback podem disputar o registro de mutação ou mudar o instante em que a lista é capturada. O retry nativo reduz um caso específico de erro de iteração, sem garantir o resultado semântico.
- **PENDENTE:** runtime com timeout real, rollback imediatamente antes/depois da remoção, encerramento do jogo durante a espera, e comparação entre timeout e remoção por botão.

Nenhum teste de thread foi adicionado nesta etapa; a conclusão acima é somente estática. Os probes pareados de `clear()` e `remove()` continuam sem logs runtime verificados, pois o conector não expõe runs de push.

| Fonte | Símbolos / intervalo | Blob SHA |
|---|---|---|
| URM convertido `classes/notifications.rpy` | `NotificationsClass.add`, linhas 9–17 | `3283ec4b1615967a71ad21cc34670bf8158ab96d5` |
| SDK 7.4.11 `renpy/exports.py` | `invoke_in_thread`, linhas 3698–3728 | `781b35b31522dafc6a24e7c3212d206c7bd6dfa5` |
| SDK 7.4.11 `renpy/python.py` | `mutator`, linhas 862–877; `RollbackLog.complete`, linhas 1707–1743 | `c5eb2819a3e4ee096dbf01130d70a77f9b623484` |


### Probe de timeout em thread preparado (2026-10-18)

Foi adicionada a testcase `urm_x52_notification_timeout_rollback`. Ela exibe a notificação numa screen, registra checkpoint, inicia `renpy.invoke_in_thread`; a função worker espera brevemente, executa `ProbeNotifications.notifications.remove(notification)` e marca uma variável de conclusão. A execução principal aguarda o sinal e solicita rollback ao checkpoint anterior. A expectativa é que a mutação da lista seja desfeita e que o item retorne.

Esse teste mede se o SDK reduzido registra e restaura uma mutação `RevertableList` feita nessa thread. Não mede segurança geral de chamadas Ren'Py em thread, timeout longo, corrida na borda do checkpoint, encerramento durante a espera nem o pacote URM integral.

- **PENDENTE:** nenhum log runtime verificado até o momento.
- **Evidência estática preservada:** `invoke_in_thread` permite poucas operações na thread; `mutator` escreve em `renpy.game.log.mutated`; `RollbackLog.complete` repete a iteração do mapa em certos `RuntimeError`.
- **Fixture:** testcase `urm_x52_notification_timeout_rollback`, commit [b4de1e4c476668f27da51775c48536f82fe16f91](https://github.com/mucholocco86/laborat-rio_renpy/commit/b4de1e4c476668f27da51775c48536f82fe16f91).
- **Workflow:** passo “Run x52 notification timeout thread rollback probe”, commit [4ffdae65e48c42dad9c314c62fd1c68b78e78c63](https://github.com/mucholocco86/laborat-rio_renpy/commit/4ffdae65e48c42dad9c314c62fd1c68b78e78c63).

### Save/load nativo: interação com o singleton (revisão estática)

O fluxo do SDK adiciona uma hipótese importante para o ciclo de vida entre saves:

1. `renpy.loadsave.save` chama `RollbackLog.freeze`, depois serializa `(roots, log)`.
2. `freeze` chama `complete(False)`, obtém `get_roots()` e remove snapshots inalcançáveis.
3. `get_roots()` inclui variáveis de StoreDict que entraram em `ever_been_changed` desde init; alteração interna de uma lista aninhada não equivale, por si, a reatribuir a variável do store.
4. `clean_stores()`, chamado durante `RollbackLog.unfreeze` no load, restaura o backup dos stores. `StoreBackup` copia cada dicionário de store de forma rasa (`dict(d)`), mantendo referências a objetos mutáveis. O SDK também comenta que `store_dicts` e `store_modules` não são reinicializados durante reload; isso sustenta a continuidade de identidade dos módulos na mesma sessão, mas não resolve sozinho quais mutações aninhadas o rollback do save restaura.
5. O URM cria `x52URM.Notifications` durante init. A classe-base define `__getstate__` como dicionário vazio e `__setstate__` sem restauração de atributos; se o objeto for efetivamente pickled, seus atributos não são reconstruídos por esses métodos.

Isso permite duas rotas possíveis, ainda não distinguidas em runtime: (a) a instância init-only permanece pela referência rasa do store durante o load na mesma sessão, mantendo seu estado de lista corrente; (b) referências alcançáveis pelo contexto/log entram no arquivo de save, onde a serialização customizada da classe pode omitir atributos. A screen também participa: `ScreenDisplayable` exclui `child`/widgets da serialização e reconstrói a screen após carregar, então a action pode ser refeita a partir do estado corrente do singleton em vez de preservar a action serializada.

- **CONFIRMADO NO SDK 7.4.11:** save serializa roots + RollbackLog; roots são limitadas a variáveis marcadas como alteradas; StoreBackup é cópia rasa; ScreenDisplayable não salva os widgets e reconstrói sua árvore.
- **CONFIRMADO NA FONTE URM CONVERTIDA:** o singleton é criado em init; `x52NonPicklable` descarta atributos em seu protocolo de estado.
- **HIPÓTESE:** o comportamento de notificações após carregar um save depende de quais snapshots do log/contexto continuam alcançáveis e do ponto em que a screen é reconstruída. A simples presença de `__getstate__` não demonstra que `Notifications` é serializada.
- **PENDENTE:** runtime comparando (1) aviso ainda ativo no momento de salvar, (2) timeout remove depois do save, (3) load do slot, (4) processo novo versus load na mesma sessão, e (5) save/load sem overlay visível.

| Fonte | Símbolos / intervalo | Blob SHA |
|---|---|---|
| SDK 7.4.11 `renpy/loadsave.py` | `save`, linhas 373–410; `load`, linha 762 em diante | `c8b831ebfd5487f11a1d4dde8c87cde7f7ed93e3` |
| SDK 7.4.11 `renpy/python.py` | `StoreBackup`, linha 260 em diante; `clean_stores`, linha 323; `RollbackLog.get_roots`, linhas 1757–1777; `freeze/unfreeze` | `c5eb2819a3e4ee096dbf01130d70a77f9b623484` |
| SDK 7.4.11 `renpy/display/screen.py` | `ScreenDisplayable`, linhas 290–315+; `nosave` exclui widgets/filhos; `after_setstate` reconstrói | `cf7997b04c3b17a337809f58aa6591ccd58a15a7` |
| URM convertido `classes/main.rpy` | instanciação de `Notifications`, linha 38 | `14f93406d2946eaed664ed72c1d47063984ce24f` |
| URM convertido `framework/modules/01utils.rpy` | `x52NonPicklable.__getstate__/__setstate__`, linhas 10–21 | `e558a2d5a5137608e542238a1d81fd65e6db349d` |

