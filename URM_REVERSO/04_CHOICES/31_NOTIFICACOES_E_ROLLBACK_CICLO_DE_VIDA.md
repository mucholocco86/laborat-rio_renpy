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
