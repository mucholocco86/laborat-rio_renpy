# 22 — Runner de teste Ren'Py 7.4.11: encerramento e limite da evidência runtime

**Data:** 2026-10-16  
**Escopo:** diagnóstico do teste isolado da propagação de ChoiceReturn no contexto de um menu.  
**Estado:** mecanismo de encerramento explicado estaticamente; a seleção segue sem resultado runtime conclusivo.  
**Proteções:** a fixture é copiada para pasta temporária; Wells, SDK e fontes originais do URM não foram alterados.

## Fontes inspecionadas

Repositório mucholocco86/laborat-rio_renpy, branch main, consultado em 2026-10-16.

| Fonte | Símbolos/intervalos | Resultado |
|---|---|---|
| renpy-7.4.11-sdk/renpy/test/testexecution.py | execute(), test_command(); arquivo | execute() retorna quando node is None; test_command() inicia a testcase. O término da árvore de teste não encerra o engine. |
| renpy-7.4.11-sdk/renpy/test/testast.py | _test.timeout; Assert, Label, Python | Timeout padrão de teste parado é 5 segundos; Assert e Python são nós da testcase. |
| renpy-7.4.11-sdk/renpy/exports.py | quit(); aproximadamente linha 1638 | renpy.quit() levanta QuitException com status padrão zero. |
| renpy-7.4.11-sdk/renpy/ast.py | Menu.execute(), linhas 1639–1697 | O resultado não-None é usado como índice estrutural do bloco. |
| renpy-7.4.11-sdk/renpy/exports.py | display_menu(), linhas 1127–1319 | O valor da interação é registrado por checkpoint(rv) e devolvido ao chamador. |
| renpy-7.4.11-sdk/renpy/ui.py | ChoiceReturn.__call__(), aproximadamente linhas 749–755 | Marca a opção escolhida quando há estado chosen e retorna self.value. |
| URM_REVERSO/tools/fixtures/urm_choice_runtime_probe.rpy | urm_probe_select, duas testcases | Fixture reduzida; cada testcase termina agora com renpy.quit() após a asserção. |

## Diagnóstico do runner

**CONFIRMADO NO SDK 7.4.11:** uma testcase pode terminar com node = None. Nesse estado, testexecution.execute() limpa o estado do mouse e retorna; esse trecho não encerra o processo. A fixture chama renpy.quit() depois de cada asserção, o que encerra o Ren'Py por QuitException com status padrão zero.

A primeira execução limpa mostrou baseline exit=0 e falha do teste forçado antes da ação, esperando “Open URM probe”. A segunda também passou no baseline, mas esperou “Select hidden route” após show_screen ser chamado dentro da testcase. Ambas pararam antes de executar a ação.

Na terceira configuração, a screen modal é mostrada pelo script imediatamente antes de entrar no menu. **OBSERVADO EM RUNTIME:** baseline nativo e teste forçado encerraram com exit=0. A testcase forçada só chama renpy.quit() depois da asserção urm_probe_result == "forced-hidden"; logo, nessa fixture o índice devolvido pela ação fez Menu.execute alcançar e executar o bloco AST da alternativa cujo menu declara if False.

Esse resultado comprova o contrato estreito de ChoiceReturn com screen modal na interação ativa. Não comprova a integração integral da screen real do URM, nem o comportamento de edição manual e rollback.

## Circuito nativo confirmado por leitura

1. Menu.execute() percorre Menu.items por índice e associa esse índice às alternativas com bloco.
2. display_menu() cria ou recebe ChoiceReturn para as entradas; após ui.interact, registra a seleção com checkpoint(rv).
3. ChoiceReturn.__call__() retorna seu value.
4. O valor sobe até Menu.execute(), que seleciona self.items[choice][2][0].
5. O Ren'Py executa o bloco AST correspondente.

A cadeia estrutural do índice está **CONFIRMADA NO SDK**. Ela não comprova, sozinha, que a ação modal da fixture devolve esse resultado à interação do menu nem que uma alternativa falsa será executada.

## Execuções e artefatos

- Fixture criada em commit 2fc71d411ce2266132d342ef61c121216ca078b7; encerramento após asserções em 379d150512d7832fd9c61b59d8231f67a1c38585; fixture final validada em e103cbc5669523609b65a036628e73f67647059a.
- Workflow criado em 99eed0a8a55c340f46a1bb523900ef804efb0c42; limites de 120 segundos e marcadores UTC em 958db3d04671eb459b6c1f0915df8788d94bd9b5.
- Runs 38945163460, 38945788113 e 38946285401: execuções iniciais canceladas ou substituídas durante o diagnóstico do runner.
- Run 38946325518: baseline passou; fixture inicial do teste forçado falhou esperando o botão de abertura, antes da ação.
- Run 38946752504: baseline passou; segunda fixture falhou aguardando foco no botão modal, antes da ação.
- Run 38946951166: **SUCCESS**. Job 117128365515. Baseline: exit=0. Teste forçado de condição falsa: exit=0. A asserção forced-hidden foi executada antes da chamada de encerramento.

A evidência runtime aplica-se à fixture sintética, não a uma carga integral do URM. Ela confirma que, nessa configuração e versão, um valor ChoiceReturn devolvido por ação de screen modal pode selecionar um item estrutural cujo menu tinha condição falsa.

## Próxima verificação

1. Obter o resultado e logs de 38946325518 ou de uma execução substituta.
2. Confirmar baseline, encerramento status zero e asserção do caminho visível.
3. Confirmar se a ação da fixture seleciona a alternativa falsa e se a asserção forced-hidden passa.
4. Se falhar, distinguir erro da fixture, propagação, visibilidade da tela e semântica de condição; não extrapolar para o URM completo.
5. Em seguida, ampliar a matriz para rollback, edição antes/durante/depois do menu e save/load.

## Classificação

| Afirmação | Classificação |
|---|---|
| O término da testcase não encerra por si só o processo no runner | **CONFIRMADO NO SDK 7.4.11** |
| renpy.quit() encerra via QuitException com status padrão zero | **CONFIRMADO NO SDK 7.4.11** |
| O índice retornado localiza o bloco em Menu.execute | **CONFIRMADO NO SDK 7.4.11** |
| Baseline nativo seleciona bloco visível e termina com sucesso | **OBSERVADO EM RUNTIME** no run 38946951166 |
| A ação da fixture executa bloco de alternativa com condição falsa | **OBSERVADO EM RUNTIME** no run 38946951166; fixture sintética |
| A screen original do URM, sem simplificação, seleciona condição falsa | **PENDENTE** de integração runtime da fonte convertida |
| A fixture representa integralmente a integração URM | **NÃO DEMONSTRADO**; reproduz o contrato estreito de ChoiceReturn |
| O efeito da seleção ou de edição manual sobre rollback/save-load | **PENDENTE** de testes separados |
