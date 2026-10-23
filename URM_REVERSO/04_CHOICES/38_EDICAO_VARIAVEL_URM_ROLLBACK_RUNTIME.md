# 38 — Edição de variável pelo URM e retorno por rollback (runtime)

**Data:** 2026-10-23  
**Escopo:** validação integrada do editor de variável do URM original, carregado em um jogo descartável no Ren'Py 7.4.11, com seleção de Choice sob fixed rollback e uma passada posterior de rollback.  
**Classificação:** runtime observado no cenário controlado descrito abaixo.

## Resultado

O teste integrado observou a edição real da variável do jogo pela tela original do URM. A rota leu o valor editado; depois, rollback restaurou o valor anterior. A instrumentação posterior, porém, não encontrou a edição 1→7 em deltas de `StoreDict`: um registro anterior contendo 1 foi reaplicado. Portanto, o teste demonstra o retorno do estado observado, mas não prova que a escrita 1→7 tenha sido registrada como delta próprio do rollback.

1. O jogo iniciou com `urm_edit_probe_value = 1`.
2. Após escolher a rota nativa B, o fixture criou uma fronteira com `renpy.fix_rollback()` e retornou até o estado de fixed rollback.
3. A tela original `URM_CodeView` foi aberta durante `rollback_is_fixed=True`.
4. O handler original `CodeView.handleVarClicked("urm_edit_probe_value")` abriu a tela original `URM_modify_value`, também com fixed rollback ativo.
5. A entrada da tela foi alterada pelo fluxo de input real do Ren'Py: apagar o valor e inserir `7`. O log do wrapper em `Var.setValue` registrou:
   - old = 1; new = 7; result = True;
   - `rollback_is_fixed=True`;
   - `rollback_limit=0`;
   - `context.force_checkpoint=True`.
6. A execução continuou pela alternativa escolhida, e a leitura do bloco AST e do checkpoint seguinte encontrou valor 7 e rota 7.
7. O trace por evento mostrou PAGEUP 1 e 2 mantendo valor/rota em 7; PAGEUP 3 aplicou um registro de rollback associado ao nó do Menu anterior que continha o valor 1, restaurando o valor e a rota `None`; PAGEUP 4 não alterou o estado. O contexto terminou com `rollback_is_fixed=True`, `can_rollback=False` e `rollback_limit=0`. Ver [run 39907164916](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39907164916).

**Conclusão limitada ao fixture:** a edição feita pela tela do URM não foi uma alteração permanente do script nem sobreviveu à restauração do estado que cruzou o menu anterior. Ela foi observada no estado ativo durante o avanço e foi revertida junto com o estado da execução ao retornar ao menu.

## Evidências

- Workflow integrado: [run 39905267994](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39905267994) — **SUCCESS**.
- Fixture com trace por tecla: commit `44b34d9eaf1c63bbf2b9a7830730d9201bd8c4eb`; instrumentação de delta/registro: run [39909338891](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39909338891), SUCCESS.
- Fixture: [urm_real_loader_variable_edit_probe.rpy](../tools/fixtures/urm_real_loader_variable_edit_probe.rpy).
- Workflow isolado: [urm-real-loader-variable-edit-rollback-probe.yml](../../.github/workflows/urm-real-loader-variable-edit-rollback-probe.yml).
- O job copiou o conteúdo de `URM_REVERSO/01_MATERIAL_URM/1_URM_ORIGINAL/` sem alterações para `game/0x52-URM/` de uma cópia descartável de `renpy-7.4.11-sdk/the_question`. Nem fontes originais, SDK ou Wells foram alterados pelo teste.
- A saída contém `URM_EDIT_CODEVIEW_SHOWN`, `URM_EDIT_MODIFY_SCREEN_SHOWN`, `URM_EDIT_VAR_SET`, `URM_EDIT_RUNTIME_RESULT` e `URM_EDIT_AFTER_ROLLBACK_SWEEP`; as asserções de restauração encerraram o testcase sem erro.

## StoreMonitor: observação restrita

A fixture substituiu temporariamente o método de instância `StoreMonitor.handleVarChange` por um wrapper delegante com a assinatura alinhada à fonte original (`varName, oldVal, newVal`). Na execução limpa, não houve linha `URM_EDIT_MONITOR_HANDLE` para `urm_edit_probe_value`, nem erro de callback.

Isso permite afirmar somente que **essa edição específica, nesse caminho de interação e nesse fixture, não chamou o método instrumentado com o delta da variável**. Não prova que o StoreMonitor jamais observe edições de tela, nem que outras operações de edição, versões ou configurações tenham o mesmo comportamento.

As execuções diagnósticas anteriores tiveram erros no próprio wrapper (`takes exactly 4 arguments` e depois referência a `self` não definido). Elas não são usadas como evidência sobre o StoreMonitor. A execução 39905267994 é a execução limpa para o wrapper de `handleVarChange`; a instrumentação posterior do store/rollback está no run 39909338891.

## Limites e questões ainda abertas

- O test runner não conseguiu focar e clicar automaticamente no token hyperlink renderizado do CodeView. Para validar o circuito sem atribuir ao runner uma capacidade que ele não demonstrou, o fixture invocou diretamente o handler original `CodeView.handleVarClicked`. Portanto, a abertura da tela e a edição são integradas/reais, mas o clique visual no hyperlink permanece pendente.
- O teste usa um jogo de laboratório e habilita explicitamente `context.rollback=True` e `store._rollback=True`. Não generalizar a sequência para todos os jogos ou configurações.
- O run 39907164916 localizou a restauração no terceiro PAGEUP. O run posterior 39909338891 instrumentou os registros internos: um registro contendo o valor 1 foi aplicado nessa chamada. As consultas instrumentadas a `get_changes` não retornaram a chave editada, portanto a origem do valor antigo naquele registro permanece pendente.
- A observação de `context.force_checkpoint=True` durante `Var.setValue` não demonstra que a edição solicitou checkpoint nem explica o registro antigo reaplicado. A semântica de checkpoint soft e os outros percursos de StoreDict estão nos documentos 18, 19, 32 e 39.
- Save/load, criação de variável, freeze, monitoramento configurado via stores URM, edição durante outros pontos do menu, e edição de objetos/listas/dicionários não foram testados aqui.
- O fixture chama `renpy.hide_screen('URM_CodeView')` explicitamente para sair do CodeView no test runner; não é evidência sobre como a interação manual fecha essa tela em todas as situações.

## Fatos e interpretação

| Categoria | Afirmação |
|---|---|
| **CONFIRMADO NA FONTE URM** | CodeView registra `handleVarClicked`, que abre `URM_modify_value`; o editor usa `SetVarValue` e `Var.setValue` para escrever no store. Ver [documento 37](37_CODEVIEW_EDICAO_VARIAVEL.md). |
| **OBSERVADO EM RUNTIME** | O pacote original carregou; tela editou 1→7 e rota leu 7. No PAGEUP 3 um registro anterior contendo 1 foi aplicado e o estado observado voltou a 1/None. O run 39909338891 não encontrou a chave em `get_changes`. |
| **OBSERVADO EM RUNTIME, limitado** | O método instrumentado `StoreMonitor.handleVarChange` não registrou essa variável durante a execução limpa. |
| **PENDENTE** | Clique real no hyperlink renderizado; save/load; outras configurações de rollback e formas de mutação. |

## Próximos probes

1. Fazer o test runner ativar o hyperlink renderizado com um mecanismo de foco compatível, sem substituir o handler direto, ou registrar essa limitação e usar teste manual reprodutível.
2. Localizar quando o registro de rollback que contém 1 foi preenchido e por que o delta da edição 1→7 não apareceu nas chamadas instrumentadas de `get_changes`; rastrear também as escritas/transferências de `force_checkpoint`.
3. Testar save/load em casos separados: salvar imediatamente após editar, salvar depois de avançar e carregar o slot.
4. Testar separadamente uma variável monitorada e uma congelada pela configuração real do URM, verificando `python_callbacks`, `get_changes`, notificação e precedência do freeze.
5. Comparar edição antes/durante/depois do menu sem combinar esses casos em um único resultado.

