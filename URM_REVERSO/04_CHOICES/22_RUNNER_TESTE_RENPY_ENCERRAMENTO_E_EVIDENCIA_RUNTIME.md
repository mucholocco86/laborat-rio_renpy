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

**CONFIRMADO NO SDK 7.4.11:** uma testcase pode terminar com node = None. Nesse estado, testexecution.execute() limpa o estado do mouse e retorna. Esse trecho não chama renpy.quit() nem encerra o processo.

Isso explica por que o passo do workflow podia continuar ativo depois de a testcase possivelmente ter completado suas verificações. Sem saída final ou logs, não se pode afirmar que as asserções passaram. O diagnóstico explica a falta de encerramento; não prova sucesso.

A fixture agora termina explicitamente cada testcase com $ renpy.quit(). **CONFIRMADO NO SDK 7.4.11:** a chamada encerra o Ren'Py via QuitException, com status zero por padrão. O workflow atualizado também limita cada invocação a 120 segundos e imprime marcadores UTC de início e fim.

## Circuito nativo confirmado por leitura

1. Menu.execute() percorre Menu.items por índice e associa esse índice às alternativas com bloco.
2. display_menu() cria ou recebe ChoiceReturn para as entradas; após ui.interact, registra a seleção com checkpoint(rv).
3. ChoiceReturn.__call__() retorna seu value.
4. O valor sobe até Menu.execute(), que seleciona self.items[choice][2][0].
5. O Ren'Py executa o bloco AST correspondente.

A cadeia estrutural do índice está **CONFIRMADA NO SDK**. Ela não comprova, sozinha, que a ação modal da fixture devolve esse resultado à interação do menu nem que uma alternativa falsa será executada.

## Execuções e artefatos

- Fixture criada em 2fc71d411ce2266132d342ef61c121216ca078b7; encerramento explícito em 379d150512d7832fd9c61b59d8231f67a1c38585; substituição do seletor launcher por abertura direta da tela durante o menu em cb1294d1e72f65ed52864dc500c3c031f9429197.
- Workflow criado em 99eed0a8a55c340f46a1bb523900ef804efb0c42; limites e marcadores adicionados em 958db3d04671eb459b6c1f0915df8788d94bd9b5.
- Run 38945163460: ativo na consulta de 2026-10-16; o passo era o baseline. Iniciado antes dos limites atuais.
- Run 38945788113: cancelado após entrar execução mais recente no controle de concorrência.
- Run 38946285401: aguardava concorrência e depois foi cancelado.
- Run 38946325518: pendente na última consulta, com fixture atualizada.

Nenhuma dessas execuções foi classificada como OBSERVADA EM RUNTIME para a seleção oculta. Os logs da execução corrigida precisam ser lidos quando terminar.

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
| Baseline do menu nativo seleciona bloco visível e termina com sucesso | **OBSERVADO EM RUNTIME** no run 38946325518 |\n| A ação da fixture executa bloco de alternativa com condição falsa | **PENDENTE DE RUNTIME**; duas execuções pararam esperando foco nos botões, antes de chamar a ação |
| A fixture representa integralmente a integração URM | **NÃO DEMONSTRADO**; reproduz apenas o contrato estreito de ChoiceReturn |
