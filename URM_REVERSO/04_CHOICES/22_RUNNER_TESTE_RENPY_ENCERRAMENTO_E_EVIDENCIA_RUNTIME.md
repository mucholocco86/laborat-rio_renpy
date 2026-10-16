# 22 — Runtime de Choice, edição de store e rollback no SDK 7.4.11

**Data:** 2026-10-16  
**Escopo:** validar em runtime a propagação de ChoiceReturn para alternativa com condição falsa e testar restauração de uma variável alterada durante uma interação.  
**Estado:** os dois contratos reduzidos passaram em fixture sintética; a integração integral da screen original do URM ainda não foi executada.  
**Proteções:** testes em cópia temporária do jogo the_question. Nenhum arquivo de wells/, wells_beta/, SDK ou fonte original do URM foi alterado.

## Fontes examinadas

Repositório mucholocco86/laborat-rio_renpy, branch main.

| Fonte | Símbolo/linhas | Evidência |
|---|---|---|
| renpy-7.4.11-sdk/renpy/test/testexecution.py | execute(), test_command() | Quando a testcase termina, o runner retorna sem encerrar o engine. |
| renpy-7.4.11-sdk/renpy/test/testast.py | _test.timeout; Assert, Label, Python | Timeout de teste parado é 5 s; asserções e Python são executados pelo loop de interação. |
| renpy-7.4.11-sdk/renpy/ast.py | Menu.execute(), L1639–1697 | Resultado não-None é usado como índice estrutural e aponta para o bloco AST. |
| renpy-7.4.11-sdk/renpy/exports.py | display_menu(), L1127–1319 | Resultado da interação passa por checkpoint(rv) e retorna ao Menu. |
| renpy-7.4.11-sdk/renpy/ui.py | ChoiceReturn.__call__(), aprox. L749–755 | Registra opção escolhida quando aplicável e retorna self.value. |
| renpy-7.4.11-sdk/renpy/exports.py | checkpoint(), L267; rollback(), L1690; quit(), L1879 | Checkpoint é delegado ao log; rollback fecha as mudanças pendentes; quit termina o engine. |
| renpy-7.4.11-sdk/renpy/python.py | RollbackLog, L1550; complete(), L1707; rollback(), L1945 | O log coleta deltas/snapshots, reverte entradas e reinicia o Context. |
| renpy-7.4.11-sdk/renpy/game.py | call_in_new_context() | A documentação da função diz que o novo contexto desativa rollback. |
| URM_REVERSO/tools/fixtures/urm_choice_runtime_probe.rpy | três testcases | Fixture sintética para Choice visível, condição falsa e edição/rollback. |

## Diagnóstico do runner

O runner de teste do SDK deixa o processo aberto depois de a testcase terminar: testexecution.execute() apenas retorna quando node é None. A fixture passou a invocar renpy.quit() após suas asserções.

Os primeiros testes forçados não chegavam à ação porque seus botões não estavam focáveis no ponto em que o runner tentava clicar. A tela modal passou a ser mostrada pelo script antes do Menu. Essa configuração passou no run 38946951166.

## Choice com condição falsa

**OBSERVADO EM RUNTIME — run 38946951166, job 117128365515:** baseline nativo e seleção forçada terminaram com exit=0. A testcase forçada só chama renpy.quit() após assert urm_probe_result == "forced-hidden". Assim, na fixture, a ação que chama ChoiceReturn devolveu o índice estrutural 1, e Menu.execute executou o bloco da alternativa declarada com if False.

Isso confirma o circuito reduzido: screen modal durante o Menu → ChoiceReturn(index) → valor de retorno da interação → Menu.execute → bloco AST da alternativa.

**Limite:** a fixture não carrega as screens/classes convertidas do URM. Prova o contrato estreito de seleção no SDK 7.4.11; não demonstra todo o processo de abertura, sensibilidade e projeção de dados do URM.

## Edição de variável e rollback

**CONFIRMADO NO SDK 7.4.11:** exports.rollback() verifica _rollback, Context.rollback e config.rollback_enabled, exceto quando force=True. Antes de restaurar, chama RollbackLog.complete(). Esse método fecha as deltas dos stores e os snapshots de objetos mutados. RollbackLog.rollback() percorre registros até o checkpoint solicitado, restaura as mudanças e o Context e reinicia a execução.

A primeira fixture de rollback falhou com “Couldn't find a place to stop rolling back”. A inspeção do estado mostrou por que o harness era inadequado: testes são executados durante o menu principal, em contexto criado por call_in_new_context(), onde o rollback é desativado. Checkpoint() não havia estabelecido uma fronteira utilizável nesse contexto. O run 38947615122 passou da falha de checkpoint, mas a asserção recebeu valor diferente de 10; aquela versão atribuía 10 imediatamente antes do checkpoint, dentro do período que o teste pretendia restaurar.

A fixture foi ajustada para:
1. registrar que o Context inicial da testcase tinha rollback=False;
2. habilitar Context.rollback somente na cópia descartável para simular contexto de gameplay;
3. manter 10 como valor inicial do store antes do checkpoint;
4. alterar a variável para 99 pela ação da screen;
5. avançar pela interação de pausa;
6. chamar rollback(force=True, checkpoints=1, label="urm_edit_rollback_verify");
7. verificar o valor no label de retorno.

**OBSERVADO EM RUNTIME — run 38947765822, job 117131138428:** baseline e escolha falsa passaram; o teste de edição/rollback terminou com exit=0. O log imprime ROLLBACK_VALUE_AT_VERIFY 10, e a asserção confirma o valor 10. Portanto, no contexto configurado da fixture, a atribuição de store 10→99 foi desfeita ao restaurar o checkpoint anterior.

**Limites:** a ação altera diretamente renpy.store.urm_rollback_value; não executa Var.setValue nem SetVarValue do URM. O rollback é iniciado por chamada de script com force=True, não pelo gesto manual do usuário na interface nativa. A fixture habilita Context.rollback explicitamente porque o runner usa contexto de menu principal. O teste demonstra reversibilidade do store e do checkpoint nativo nesse arranjo; não demonstra ainda os detalhes do StoreMonitor, avanço por várias Choices, rollback interativo do jogador, nem save/load.

## Artefatos e execuções

- Fixture inicial: 2fc71d411ce2266132d342ef61c121216ca078b7.
- Runner encerrado após assertions: 379d150512d7832fd9c61b59d8231f67a1c38585.
- Fixture final da Choice falsa: e103cbc5669523609b65a036628e73f67647059a.
- Fixture com primeiro teste de rollback: d81556607c2f4780455f541f6ccdd9daebd1d7e9.
- Workflow com etapa de rollback: db7f36550a27253c8923a3dc74e954b2f80af117.
- Fixture que modela Context.rollback=True e checkpoint ajustado: f53f3fbc9b414f040a4a4f700b0fca8a0ffb6afa.
- Fixture final com estado inicial antes do checkpoint: 1cf7c039bd2540a114f047ebc4ebb3f4553faf65.
- Run 38947312511: rollback falhou porque não encontrou ponto de restauração.
- Run 38947615122: rollback alcançou o label, mas a asserção não encontrou valor 10.
- Run 38947765822: **SUCCESS**; baseline, escolha falsa e edição/rollback passaram.

## Classificação e próxima etapa

| Afirmação | Classificação |
|---|---|
| ChoiceReturn pode devolver índice estrutural usado pelo Menu | **CONFIRMADO NO SDK 7.4.11** |
| A fixture executou alternativa marcada if False | **OBSERVADO EM RUNTIME**, run 38946951166 |
| O runner começa essa testcase em contexto com rollback desativado | **OBSERVADO EM RUNTIME** pela asserção da fixture e compatível com call_in_new_context() |
| Store alterado de 10 para 99 foi restaurado a 10 no checkpoint anterior | **OBSERVADO EM RUNTIME**, run 38947765822 |
| Var.setValue/SetVarValue do URM apresenta o mesmo resultado | **PENDENTE** de teste que use o circuito da fonte URM |
| A screen original do URM seleciona condição falsa e abre no contexto correto | **PENDENTE** de teste integrado com fonte convertida |
| Edição seguida de várias interações e rollback manual do jogador | **PENDENTE** |
| Relação dessa edição com save/load nativo e arquivo .urm | **PENDENTE** de matriz específica |

Próxima prioridade: reproduzir em fixture a semântica exata de Var.setValue/SetVarValue e depois executar edição → avanço por menu/dialogue → rollback nativo, sem usar force=True quando o cenário permitir. Em seguida, testar salvar/carregar após a edição.