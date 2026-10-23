# 39 — StoreMonitor, delta do StoreDict e edição iniciada por screen

**Data:** 2026-10-23  
**Escopo:** explicar a ausência de chamada a `StoreMonitor.handleVarChange` no teste integrado de edição e distinguir notificação do URM da captura reversível nativa do Ren'Py 7.4.11.  
**Evidência:** inspeção das fontes do URM original e do SDK; runtime integrado do URM original; runtime reduzido anterior sobre ciclagem de delta.  
**Proteções:** não houve mudança em SDK, fontes originais URM, `wells/` ou `wells_beta/`.

## Resultado

A edição pela tela `URM_modify_value` escreve no store por `SetVarValue → Var.setValue`. Essa rota não chama diretamente `StoreMonitor.handleVarChange` e não é, por si, a execução de um nó `renpy.ast.Python`.

O monitor do URM está ligado a `renpy.config.python_callbacks`. No SDK 7.4.11, `ast.Python.execute()` chama esses callbacks no `finally`, depois do bytecode Python do nó. Em outro momento do fluxo, quando a interação retorna ao executor e o próximo nó começa, `Context.run()` pode chamar `RollbackLog.begin()`; se a interação anterior marcou `did_interaction`, `begin()` fecha o registro anterior por `complete(True)`. Esse fechamento coleta deltas com `StoreDict.get_changes(True)`, avançando a base de comparação.

Com rollback ativo, esse ciclo pode registrar no histórico uma edição feita pela screen **antes** de um nó Python subsequente executar a callback do URM. A callback então consulta `get_changes(False)` sem encontrar o mesmo delta. A ausência de notificação do StoreMonitor não significa que o estado saiu do histórico nativo.

## Sequência que as fontes sustentam

```text
URM screen Input / ação
    ↓
SetVarValue → Var.setValue
    ↓
atribuição a renpy.store
    ↓
interação retorna / did_interaction
    ↓
Context.run inicia o próximo nó
    ↓
RollbackLog.begin() → complete(True)
    ↓
StoreDict.get_changes(True) fecha/captura o delta
    ↓
nó ast.Python executa seu bytecode
    ↓
python_callbacks → StoreMonitor._m1_vars__pythonCallback
    ↓
get_changes(False) consulta o período já ciclado
```

A sequência acima é a explicação da interação entre os componentes, não a afirmação de que toda screen, toda ação ou todo jogo atravessa exatamente o mesmo conjunto de nós. O caso integrado e o caso reduzido são classificados separadamente abaixo.

## Evidência de fonte

### URM original

- A screen `URM_modify_value` vincula `valueInput.onEnter` a `SetVarValue(...)`; Change invoca a mesma ação.
- `Var.setValue` valida/converte o valor e executa a atribuição (ou mutação de item) sobre `renpy.store`. Não chama `handleVarChange`.
- `StoreMonitor.init()` registra `_m1_vars__pythonCallback` em `renpy.config.python_callbacks` e também injeta um setter para um caminho específico de atribuições.
- `_m1_vars__pythonCallback` primeiro define `renpy.game.context().force_checkpoint = True`; depois consulta `get_changes(False)` e chama `handleVarChange` para as chaves retornadas.
- `handleVarChange` só cria notificação quando a variável está monitorada, a tela de edição não está aberta e old/new diferem. Congelamento é tratado antes e retorna `False`.

### SDK Ren'Py 7.4.11

- `renpy.ast.Python.execute()` chama callbacks ao final do bytecode, fora da fase init.
- `Context.run()` decide se atualizará rollback antes da execução do nó e pode começar esse ciclo por interação anterior.
- `RollbackLog.begin()` não fecha um registro a cada nó incondicionalmente: a interação, checkpoint anterior ou force determina se começa. Quando começa com um registro atual, chama `complete(True)`.
- `RollbackLog.complete(begin=True)` passa o parâmetro a `StoreDict.get_changes(begin)`; com `True`, o StoreDict avança sua base de comparação enquanto fornece as alterações do intervalo.
- A flag de contexto `force_checkpoint` é transferida para `RollbackLog.force_checkpoint` em `Context.run()` depois de chamar `log.begin()`. O log consome essa flag em `complete()` com `checkpoint(hard=False)`; isso não equivale a um hard checkpoint criado no instante da edição.

A conclusão sobre ciclo de delta também está registrada em [documento 32](32_CICLAGEM_STOREDELTA_ANTES_CALLBACK_REVERT.md); a semântica de checkpoint soft em [documentos 18 e 19](README.md).

## Evidência de runtime integrada

No run [39905267994](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39905267994), já com o wrapper do monitor corrigido, o fixture carregou o pacote original do URM no jogo descartável. O editor real alterou 1→7 e o valor foi lido pela rota. Não houve erro de callback nem log do wrapper em `handleVarChange` para a variável alvo. Após a sequência PAGEUP, o valor e a rota foram restaurados.

Esse runtime integrado **não instrumentou** `StoreDict.get_changes`, portanto a coleta do delta em `complete(True)` é uma explicação sustentada pelas fontes e corroborada pelo runtime reduzido do documento 32, mas não um evento medido diretamente naquele run integrado.

## Correção de leitura de `force_checkpoint`

O run integrado registrou `context.force_checkpoint=True` durante a chamada de `Var.setValue`. Isso não prova que `Var.setValue` solicitou checkpoint: a fonte dessa função não escreve a flag. O callback do URM a define incondicionalmente ao final dos nós Python, e o SDK transfere a solicitação em outro ponto do ciclo do executor. Sem instrumentar cada escrita e transferência da flag nesse fixture, a origem daquele valor naquele instante permanece **PENDENTE**.

Do mesmo modo, o registro da flag não demonstra um hard checkpoint nem explica sozinho por que o valor foi revertido. A reversibilidade decorre da integração com o histórico nativo observada no teste, enquanto a flag de checkpoint tem semântica própria.

## Trace por evento de rollback

A fixture integrada foi corrigida para instalar o wrapper de `RollbackLog.rollback` na classe; antes, a função de trace estava definida, mas não substituía o método. No run [39907164916](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39907164916), o job terminou **SUCCESS** e imprimiu estado após cada PAGEUP:

| Evento | Valor da variável | Rota | Estado observado |
|---|---:|---|---|
| PAGEUP 1 | 7 | 7 | Ainda no fluxo posterior; limite de rollback 2 |
| PAGEUP 2 | 7 | 7 | Fixed rollback ativo no retorno; limite 1 |
| PAGEUP 3 | 1 | `None` | Aqui `RollbackLog.rollback()` restaurou o estado anterior ao menu; fixed rollback ativo, limite 0 |
| PAGEUP 4 | 1 | `None` | A chamada foi registrada, mas sem novo estado a restaurar; permaneceu na fronteira |

A execução anterior [39905267994](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39905267994) demonstrava apenas o estado final após quatro teclas. O run 39907164916 substitui essa incerteza sobre o evento: no cenário testado, a restauração ocorreu no **terceiro PAGEUP**.

O teste continua condicionado ao harness: `context.rollback=True`, `store._rollback=True`, `fix_rollback_without_choice=False`, uma Choice B, chamada direta ao handler do CodeView e quatro eventos de teclado do runner. Não generalizar a contagem de PAGEUP para outros scripts, políticas ou configurações.

## Classificação

- **CONFIRMADO NA FONTE URM ORIGINAL:** editor screen → `SetVarValue` → `Var.setValue`; callback de monitor é registrado em `python_callbacks`; callback define `force_checkpoint` e consulta mudanças; setter e callback são caminhos distintos.
- **CONFIRMADO NO SDK 7.4.11:** callbacks são chamados pelo nó `ast.Python`; início de registro por interação pode fechar/ciclar StoreDict antes do próximo nó; o checkpoint soft não é hard.
- **OBSERVADO EM RUNTIME INTEGRADO:** edição 1→7 lida pela rota; o wrapper corrigido não registrou `handleVarChange`; PAGEUP 3 restaurou 1 e `None`.
- **OBSERVADO EM RUNTIME REDUZIDO:** documento 32 mediu o delta 20→10 em `get_changes(True)` antes da callback e mostrou o callback subsequente sem delta.
- **INTERPRETAÇÃO SUSTENTADA, não medição integrada:** a edição integrada foi capturada por `complete(True)` antes da callback; é consistente com a ordem estática e com o fixture reduzido.
- **PENDENTE:** medir `get_changes` e cada escrita/transferência de `force_checkpoint` dentro do fixture com loader original; testar variável marcada como monitorada/congelada; save/load; clique visual no hyperlink.

## Fontes

| Arquivo | Símbolos / intervalo aproximado | Blob SHA |
|---|---|---|
| SDK `renpy/ast.py` | `Python.execute`, ~910–940 | `d81ffc13f28f0b7442ba6905f1745ee838f7b185` |
| SDK `renpy/execution.py` | `Context.run`, início de nó e transferência de `force_checkpoint`, ~500–565 | `547f73b26dad0fe08fda6333e5f4b60c97cf8772` |
| SDK `renpy/python.py` | `RollbackLog.begin/complete/checkpoint`, ~1620–1860; `rollback`, ~1930–1995 | `c5eb2819a3e4ee096dbf01130d70a77f9b623484` |
| URM original `classes/vars.rpy` | `Var.setValue`, `StoreMonitorClass`, ~232–269, 492–577 | `57482937e14f215dac0ecb22a62da8ad160cba58` |
| URM original `screens/vars.rpy.x52` | `URM_modify_value` e ação Input/Change, ~181–254 | `7959b2c0e6249df0edbb9ebe683481d46e4537e1` |

- Fixture integrada e workflow: [run 39907164916](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39907164916).
- Fixture: [urm_real_loader_variable_edit_probe.rpy](../tools/fixtures/urm_real_loader_variable_edit_probe.rpy).
- Documento complementar de edição: [38 — Edição de variável pelo URM e retorno por rollback](38_EDICAO_VARIAVEL_URM_ROLLBACK_RUNTIME.md).
