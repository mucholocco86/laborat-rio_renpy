# 39 — StoreMonitor, delta do StoreDict e edição iniciada por screen

**Data:** 2026-10-23  
**Escopo:** explicar a ausência de chamada a `StoreMonitor.handleVarChange` no teste integrado de edição e distinguir notificação do URM da captura reversível nativa do Ren'Py 7.4.11.  
**Evidência:** inspeção das fontes do URM original e do SDK; runtime integrado do URM original; runtime reduzido anterior sobre ciclagem de delta.  
**Proteções:** não houve mudança em SDK, fontes originais URM, `wells/` ou `wells_beta/`.

## Resultado

A fonte do URM confirma que `URM_modify_value` escreve no store por `SetVarValue → Var.setValue`, sem chamar diretamente `StoreMonitor.handleVarChange`. O monitor consulta mudanças em callback de nó `ast.Python`.

O probe reduzido do documento 32 demonstrou que um delta pode ser ciclado por `complete(True)` antes da callback em um percurso específico. Porém, o trace integrado do editor original (run [39909338891](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39909338891)) não encontrou `urm_edit_probe_value` em nenhuma chamada instrumentada de `get_changes`, embora o valor atual fosse 7. Portanto, não aplicamos ao editor real a explicação medida no probe reduzido.

O PAGEUP 3 ainda retornou o estado observado a 1: o trace encontrou um registro de rollback anterior contendo 1, que ao ser aplicado mudou o valor de 7 para 1. Não encontrou registro contendo 7. Assim, foi observada a restauração do estado, mas não demonstrado que a edição 1→7 tenha sido registrada como delta próprio. A origem temporal do registro que continha 1 segue aberta.

## Sequência que as fontes sustentam

O SDK permite o seguinte caminho genérico: interação anterior pode levar `Context.run()` a `RollbackLog.begin()`; quando começa novo período, `begin()` pode chamar `complete(True)`, que consulta `StoreDict.get_changes(True)`. Em outro momento, `ast.Python.execute()` chama os callbacks, e a callback do URM consulta `get_changes(False)`.

Esse diagrama é uma possibilidade arquitetural baseada nas fontes, não o trace observado da edição integrada. O run 39909338891 mediu `get_changes` após a edição e não encontrou a chave-alvo. O probe reduzido do documento 32 é evidência independente de outro caminho.

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

No run [39909338891](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39909338891) (**SUCCESS**), a fixture instrumentou `StoreDict.get_changes`, `StoreDict.begin`, `RollbackLog.complete` e `Rollback.rollback`, delegando aos métodos originais. O pacote URM original foi copiado sem alterações para o jogo descartável.

- `Var.setValue` alterou 1→7; o bloco da rota leu 7.
- As chamadas instrumentadas de `get_changes(True)` e `get_changes(False)` após a tela de edição apareceram sem a chave `urm_edit_probe_value`, embora a chave estivesse no StoreDict principal e seu valor atual fosse 7.
- Na restauração do PAGEUP 3, os registros examinados não continham a chave-alvo até um registro associado ao nó do Menu anterior conter `('store', 1)`. Aplicá-lo mudou o valor observado de 7 para 1; a rota voltou a `None`.
- PAGEUP 1 e 2 mantiveram valor/rota em 7; PAGEUP 4 não mudou o estado.

O resultado confirma a restauração do estado observável, mas não mostra um delta específico da edição 1→7. Uma entrada histórica anterior contendo 1 foi reaplicada. A origem e o momento em que esse registro passou a conter 1 em relação à edição continuam pendentes. O trace do rollback por evento anterior está em [run 39907164916](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39907164916).

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

- **CONFIRMADO NA FONTE URM ORIGINAL:** editor screen → `SetVarValue` → `Var.setValue`; callback do monitor é registrada em `python_callbacks`; callback define `force_checkpoint` e consulta mudanças; setter e callback são caminhos distintos.
- **CONFIRMADO NO SDK 7.4.11:** `ast.Python.execute()` chama callbacks depois do bytecode; `RollbackLog.begin/complete` pode ciclar StoreDict; `Rollback.rollback()` reaplica valores antigos armazenados em cada registro.
- **OBSERVADO EM RUNTIME INTEGRADO:** edição 1→7 foi lida pela rota; nenhuma chamada instrumentada de `get_changes` trouxe a chave-alvo; no PAGEUP 3, registro anterior contendo 1 foi aplicado, restaurando 1/`None`.
- **OBSERVADO EM RUNTIME REDUZIDO:** documento 32 mediu outro percurso onde o delta 20→10 foi retornado por `get_changes(True)` antes da callback.
- **CORRIGIDO:** a interpretação anterior de que o editor integrado foi capturado por `complete(True)`; o run 39909338891 não encontrou o delta-alvo.
- **PENDENTE:** localizar quando o registro contendo 1 foi criado/atualizado; determinar se a atribuição 1→7 é registrada em outro caminho; instrumentar cada escrita/transferência de `force_checkpoint`; testar variável marcada, save/load e clique visual no hyperlink.

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
