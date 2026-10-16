# 22 — Runtime de Choice e rollback: prova sintética no SDK 7.4.11

**Data:** 2026-10-16  
**Escopo:** testar a propagação de ChoiceReturn para alternativa com condição falsa e preparar teste runtime de edição de variável seguida por rollback.  
**Estado:** seleção de condição falsa observada em fixture sintética; teste runtime de rollback da edição está em execução.  
**Proteções:** fixture executada em cópia temporária do jogo the_question. Nenhum arquivo de wells/, wells_beta/, SDK ou fonte original do URM foi modificado.

## Fontes inspecionadas

Repositório mucholocco86/laborat-rio_renpy, branch main.

| Fonte | Símbolos/linhas | Resultado |
|---|---|---|
| renpy-7.4.11-sdk/renpy/test/testexecution.py | execute(), test_command() | O runner retorna quando a testcase termina, mas não encerra o engine automaticamente. |
| renpy-7.4.11-sdk/renpy/test/testast.py | _test.timeout; Assert, Label, Python | Timeout de testcase parada de 5 segundos; os nós de asserção/Python rodam no loop de interação. |
| renpy-7.4.11-sdk/renpy/exports.py | checkpoint(), L267; rollback(), L1690; quit() | checkpoint delega ao log; rollback fecha deltas e chama o log; quit levanta QuitException com status padrão zero. |
| renpy-7.4.11-sdk/renpy/ast.py | Menu.execute(), L1639–1697 | O retorno de interação não-None é usado como índice estrutural do bloco AST. |
| renpy-7.4.11-sdk/renpy/exports.py | display_menu(), L1127–1319 | O retorno da interação é registrado em checkpoint(rv) e devolvido ao chamador. |
| renpy-7.4.11-sdk/renpy/ui.py | ChoiceReturn.__call__(), aprox. L749–755 | Marca a opção escolhida quando aplicável e retorna self.value. |
| renpy-7.4.11-sdk/renpy/python.py | RollbackLog, L1550; complete(), L1707; rollback(), L1945 | complete coleta alterações de stores/objetos; rollback restaura registros, estado e contexto. |
| URM_REVERSO/tools/fixtures/urm_choice_runtime_probe.rpy | testcases de Choice e rollback | Fixture sintética que reproduz contratos específicos; não carrega o URM inteiro. |

## Runner e correção do harness

O teste inicial parecia travado mesmo depois do baseline porque, quando testexecution.execute() chega a node = None, ele apenas limpa o mouse e retorna. Ele não encerra o processo. A fixture passou a chamar renpy.quit() após cada asserção; o SDK confirma que isso encerra o engine com status zero por padrão.

O primeiro e segundo testes de escolha forçada pararam antes da ação porque os botões da fixture não estavam focáveis no momento do clique automatizado. O harness foi ajustado para mostrar a tela modal pelo próprio script imediatamente antes do Menu. A terceira configuração passou.

## Choice com condição falsa

**OBSERVADO EM RUNTIME — run 38946951166, job 117128365515:** baseline nativo e caso forçado terminaram com exit=0. A testcase forçada chama renpy.quit() apenas depois da asserção urm_probe_result == "forced-hidden". Portanto, na fixture sintética, a ação baseada em ChoiceReturn retornou o índice estrutural e Menu.execute executou o bloco que estava sob a alternativa declarada com if False.

O resultado valida este circuito reduzido no SDK 7.4.11:

1. A tela modal está aberta enquanto o Menu espera a interação.
2. A ação oculta a tela e chama a função equivalente ao contrato estreito de URMChoice.Action.
3. ChoiceReturn devolve o índice 1.
4. Menu.execute usa o índice para escolher self.items[choice] e executar o bloco.
5. O bloco atribui forced-hidden; a asserção passa.

**Limite:** a fixture não carrega as screens/classes convertidas do URM. A prova confirma que o contrato de ação pode selecionar uma alternativa com condição falsa nessa interação; não confirma todos os detalhes de abertura, sensibilidade ou integração da tela original do URM.

## Rollback nativo e edição de store

**CONFIRMADO NO SDK 7.4.11:** renpy.exports.rollback() verifica _rollback, rollback do Context e config.rollback_enabled, salvo quando force=True. Antes da restauração, chama RollbackLog.complete() para fechar as alterações correntes. RollbackLog.complete() coleta deltas do StoreDict e snapshots dos objetos revertíveis. RollbackLog.rollback() percorre registros até a fronteira de checkpoint solicitada, restaura mudanças e Context e reinicia a execução.

A fixture agora inclui um teste isolado de atribuição manual:

- Começa com urm_rollback_value = 10.
- Cria checkpoint com identificador before-manual-edit.
- Abre uma screen modal cuja ação altera o valor do store para 99.
- Continua por uma pausa de interação.
- Solicita rollback forçado de um checkpoint e direciona o fluxo ao label urm_edit_rollback_verify.
- A asserção nesse label espera novamente o valor 10.

O teste verifica atribuição simples ao store e restauração nativa. Não reproduz Var.setValue, SetVarValue, CreateVar ou StoreMonitor do URM. Também não representa ainda o retorno manual do jogador por vários diálogos/Choices; esse cenário será a próxima extensão caso a prova reduzida passe.

## Histórico dos testes

- Fixture inicial: commit 2fc71d411ce2266132d342ef61c121216ca078b7.
- Encerramento explícito do engine: 379d150512d7832fd9c61b59d8231f67a1c38585.
- Versão que passou no teste de condição falsa: e103cbc5669523609b65a036628e73f67647059a.
- Fixture com teste de rollback: d81556607c2f4780455f541f6ccdd9daebd1d7e9.
- Workflow com etapa de rollback: db7f36550a27253c8923a3dc74e954b2f80af117.
- Run 38946325518: baseline passou; primeira fixture forçada falhou esperando o botão launcher, antes de executar ação.
- Run 38946752504: baseline passou; segunda fixture forçada falhou esperando foco no botão modal, antes da ação.
- Run 38946951166: sucesso; baseline e alternativa falsa passaram com exit=0.
- Run 38947299753: teste em execução, originado pela atualização da fixture antes da etapa de rollback ser adicionada ao workflow.
- Run 38947312511: execução mais recente com a etapa de rollback; estado inicial pendente/aguardando concorrência na consulta atual.

## Classificação e próximas verificações

| Afirmação | Classificação |
|---|---|
| A testcase concluída não encerra sozinha o processo do runner | **CONFIRMADO NO SDK 7.4.11** |
| ChoiceReturn pode devolver índice estrutural consumido por Menu.execute | **CONFIRMADO NO SDK 7.4.11** |
| A fixture seleciona bloco de uma alternativa declarada com condição falsa | **OBSERVADO EM RUNTIME**, run 38946951166 |
| A screen real do URM seleciona condição falsa sem simplificação | **PENDENTE** de integração runtime com fonte convertida |
| Rollback nativo restaura deltas de store e objetos revertíveis | **CONFIRMADO NO SDK 7.4.11** por fonte |
| Atribuição 10 → 99 da fixture retorna a 10 por rollback | **PENDENTE** do run 38947312511 |
| Var.setValue do URM tem o mesmo resultado observado | **PENDENTE**; exige fixture específica que reproduza o circuito URM |
| Edição seguida de avanços e rollback manual do jogador restaura valor anterior | **PENDENTE** de teste separado |
| Arquivo .urm contém snapshot completo do store do jogo | **CONTRADITO** pela separação já documentada entre dados próprios do URM e save nativo |

