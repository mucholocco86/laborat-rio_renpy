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

