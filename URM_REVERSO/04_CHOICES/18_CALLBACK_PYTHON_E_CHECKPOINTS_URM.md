# 18 — Callback Python, construtores revertíveis e edição pela screen

**Data:** 2026-10-16  
**Escopo:** Ren'Py 7.4.11 e URM convertido.  
**Evidência:** inspeção estática; nenhuma execução runtime feita.

Este documento complementa o documento 17 e fecha dois pontos: a chamada efetiva de python_callbacks pelo SDK e a transformação de literais para os construtores usados pelo mecanismo de rollback.

## Resultado principal

O SDK 7.4.11 chama os callbacks de python_callbacks no finally de renpy.ast.Python.execute(), após py_exec_bytecode(), desde que o Context não esteja em init_phase. Essa chamada não está no caminho de SetVarValue, CreateVar ou Var.delete acionados por uma ação de screen.

Assim, não se pode dizer que uma edição feita na interface URM aciona imediatamente o callback StoreMonitor. O estado pode ainda ser capturado por mecanismos nativos no ciclo do rollback; isso é separado da notificação feita pelo monitor.

## Fontes

- SDK: renpy-7.4.11-sdk/renpy/ast.py, blob SHA d81ffc13f28f0b7442ba6905f1745ee838f7b185, classe Python, aproximadamente linhas 865–925.
- SDK: renpy-7.4.11-sdk/renpy/python.py, blob SHA c5eb2819a3e4ee096dbf01130d70a77f9b623484, StoreDict e compilador/WrapNode, aproximadamente linhas 80–180 e 440–570.
- SDK: renpy-7.4.11-sdk/renpy/python.py, RevertableList/Dict e RollbackLog, aproximadamente linhas 820–1230 e 1480–1760.
- URM convertido: URM_REVERSO/01_MATERIAL_URM/2_URM_X52_CONVERTIDO/classes/vars.rpy, blob SHA 57482937e14f215dac0ecb22a62da8ad160cba58, Var.setValue e StoreMonitorClass.
- URM convertido: URM_REVERSO/01_MATERIAL_URM/2_URM_X52_CONVERTIDO/screens/vars.rpy, blob SHA 7959b2c0e6249df0edbb9ebe683481d46e4537e1, ações de modificação/criação/exclusão.

## Fluxo exato do callback no SDK

A implementação de Python.execute segue esta ordem:

    next_node(self.next)
    statement_name("python")
    py_exec_bytecode(...)
    finally:
        se não estiver em init_phase:
            executar cada callback em renpy.config.python_callbacks

O bloco finally significa que o loop de callbacks é alcançado mesmo quando py_exec_bytecode levanta uma exceção; a condição init_phase ainda pode impedir sua execução. O callback do StoreMonitor descreve o próprio momento como “quando um Python node acabou de executar”.

No SDK, esta é a chamada de callbacks identificada nesta classe. A tela do URM usa ações como Function/SetVarValue/CreateVar e chamadas diretas a métodos; tais ações não são, por esse fato, instâncias de ast.Python.execute.

## Consequência para StoreMonitor

O callback do URM faz duas coisas relevantes:

1. Marca context().force_checkpoint = True.
2. Solicita get_changes(False) no dicionário do store e processa os nomes de nível superior retornados.

O código do SDK de StoreDict mostra que get_changes(False) calcula deltas em relação ao início do período sem ciclar a referência anterior. Portanto, a observação no callback não consome o delta. O RollbackLog.complete() posteriormente coleta as mudanças dos StoreDicts, registra os objetos mutados e lida com a solicitação de checkpoint do log.

A passagem de Context.force_checkpoint até o checkpoint do RollbackLog depende do ciclo de Context.run(), detalhado na documentação anterior da área. Isso não autoriza dizer que o checkpoint ocorre sincronamente dentro da ação da screen ou no instante em que o callback chama a função. A posição temporal exata entre a ação do URM, a interação visual e a conclusão do log permanece uma pergunta de runtime.

### O que se pode afirmar sobre edição pela tela

- **CONFIRMADO NA FONTE URM:** ações diretas da tela chamam SetVarValue/Var.setValue, CreateVar, ou Var.delete.
- **CONFIRMADO NO SDK:** o callback python_callbacks é chamado pela execução de um nó ast.Python.
- **CONCLUSÃO ESTÁTICA:** a ação de screen não chama esse callback por meio do caminho Python.execute mostrado.
- **PENDENTE:** se outro mecanismo de interação produz checkpoints antes da próxima execução de nó Python, e em que momento uma edição de screen passa a ser observada pelo StoreMonitor.
- **PENDENTE:** comportamento exato de rollback e notificação com edição feita enquanto um menu está aberto.

## Transformação dos literais

A classe WrapNode, usada por py_compile, transforma nós AST de lista/dicionário e suas compreensões em chamadas aos nomes __renpy__list__ e __renpy__dict__. Isso confirma que código Python compilado pelo Ren'Py não mantém necessariamente o literal como list/dict padrão.

RevertableList e RevertableDict implementam os métodos de mutação por wrappers mutator. Esse wrapper cria um snapshot limpo na primeira mutação do objeto dentro do log corrente. RollbackLog.complete() transfere snapshots vivos para o registro corrente, e Rollback.rollback() chama _rollback no objeto.

**Limite da evidência:** neste cruzamento não foi localizado o ponto de registro dos nomes __renpy__list__/__renpy__dict__ no store. A transformação do AST e a existência das classes revertíveis foram confirmadas, mas a associação integral do nome de construtor ao tipo concreto requer localizar o registro em outra parte do SDK. Não inferir que todo objeto lista/dicionário alcançado pelo URM tem tipo revertível.

## Modelo separado: rollback e monitoramento

| Evento | Mecanismo | Evidência |
|---|---|---|
| Atribuir nome raiz do store | StoreDict delta | confirmado no SDK |
| Mutar RevertableList/Dict | mutator → log.mutated → snapshot de objeto | confirmado no SDK, condicionado ao tipo |
| URM solicitar checkpoint | Context.force_checkpoint no callback | confirmado na fonte URM |
| SDK executar callback | Python.execute, após o bytecode e fora de init_phase | confirmado no SDK |
| Screen action acionar Python callback | nenhum caminho identificado | não ocorre pelo caminho Python.execute; outros gatilhos não demonstrados |
| URM notificar variável após edição de screen | lógica depende do callback/patch de atribuição | pendente de runtime |

## Implicação para o relato do usuário

O relato de que uma variável editada pelo URM permanece alterada durante o avanço e volta ao valor anterior ao retroceder é compatível com os mecanismos nativos de deltas do store e snapshots de objetos. A leitura estática explica uma via plausível e diferencia alterações raiz das mutações internas de containers, mas ainda não demonstra o instante exato em que a edição é incluída num Rollback record. Logo, esse relato permanece **RELATADO PELO USUÁRIO**, e sua explicação mecânica completa segue **HIPÓTESE** até teste controlado no SDK 7.4.11/URM.

## Próxima investigação

1. Localizar no SDK o registro dos construtores especiais e confirmar o tipo retornado.
2. Inspecionar Context.run() para concluir a transição de Context.force_checkpoint ao RollbackLog.
3. Preparar uma fixture runtime mínima fora de wells/, wells_beta/, SDKs e fontes originais.
4. Medir atribuição raiz, mutação aninhada, edição durante menu e rollback em passos controlados.
