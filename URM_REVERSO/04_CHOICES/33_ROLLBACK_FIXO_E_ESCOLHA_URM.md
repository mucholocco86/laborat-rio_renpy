# 33 — Fixed rollback e escolha acionada pelo URM

**Data:** 2026-10-23  
**Escopo:** cruzamento estático entre a ação de Choice do URM convertido e o SDK Ren'Py 7.4.11.  
**Status:** fonte URM e fonte SDK confirmadas; integração ponta a ponta em runtime permanece pendente.

## Pergunta

Por que `URMChoice.Action` define `renpy.game.log.rollback_is_fixed = False` antes de devolver o índice da alternativa por `ChoiceReturn`? Essa atribuição remove a decisão fixada, libera uma nova seleção, ou altera o histórico de rollback?

## Evidências

### Fonte URM convertida

- `URM_REVERSO/01_MATERIAL_URM/2_URM_X52_CONVERTIDO/classes/choices.rpy`, blob `48fc35f96119189e50f038981795115b3df7b770`, propriedade `URMChoice.Action` (linhas 87–93 no snapshot examinado):
  - define `renpy.game.log.rollback_is_fixed = False`;
  - chama `renpy.ui.ChoiceReturn(choice[0], index)()`;
  - retorna o valor produzido por essa ação.
- `.../screens/choices.rpy`, blob `a78de7e46a5b6230b4871628bfa62708233a07ce`, linhas 79–84:
  - o botão Select executa a ação URM em uma lista de ações;
  - declara `sensitive=True`;
  - não consulta `choice.isVisible` para desabilitar esse botão.

### SDK Ren'Py 7.4.11

- `renpy/config.py`, blob `781b35b31522dafc6a24e7c3212d206c7bd6dfa5`, linha 75: `fix_rollback_without_choice = False` por padrão. O comentário descreve que, quando ativada, menus em fixed rollback não têm opções clicáveis e um clique/roda do mouse avança o roll-forward.
- `renpy/ui.py`, blob `914a0c4702b7af391e014702a16ccc333e7573de`, `ChoiceActionBase.get_sensitive()` (696–703): a sensibilidade nativa depende de `in_fixed_rollback()`, `block_all` e `get_selected()`. `block_all` assume o valor de `config.fix_rollback_without_choice` quando não especificado. Com o padrão `False`, a alternativa já selecionada no roll-forward pode continuar sensível; alternativas diferentes ficam bloqueadas enquanto fixed rollback estiver ativo.
- No mesmo arquivo, `ChoiceReturn.__call__()` (aprox. 758–762) retorna `self.value`; só registra `chosen` se a ação tiver localização e store de escolhas disponível.
- `renpy/exports.py`, blob `781b35b31522dafc6a24e7c3212d206c7bd6dfa5`, `display_menu` (1127 em diante, em especial 1205–1206 e 1296–1300): em fixed rollback, chama `saybehavior()` quando a configuração correspondente está ligada; a interação retorna `rv`, que é então processado pelo fluxo do menu e pelo checkpoint (linha 1476 no caminho de menu examinado).
- `renpy/ast.py`, blob `d81ffc13f28f0b7442ba6905f1745ee838f7b185`, `Menu.execute()` (1639–1698): depois de `renpy.exports.menu(...)`, se o resultado não for `None`, usa `self.items[choice][2][0]` como próximo nó. O valor retornado precisa corresponder ao índice estrutural em `Menu.items`.
- `renpy/exports.py`, `in_fixed_rollback()` (aprox. 245–255): delega a `renpy.game.log.in_fixed_rollback()`.
- `renpy/python.py`, blob `c5eb2819a3e4ee096dbf01130d70a77f9b623484`:
  - `RollbackLog.in_fixed_rollback()` (aprox. 1805–1806) retorna `rollback_is_fixed`;
  - `fix_rollback()` (1911–1913) define `fixed_rollback_boundary` se ainda não estiver em fixed rollback e houver histórico;
  - `rollback()` (aprox. 2064–2067) liga `rollback_is_fixed` quando um registro restaurado alcança a fronteira;
  - `begin()` (1673–1685) encerra o estado fixo ao alcançar a fronteira durante a continuação ou atualiza a fronteira quando termina o dado de replay.

## Circuito e interpretação delimitada

O motor mantém a fronteira (`fixed_rollback_boundary`) separada do indicador consultado pela UI (`rollback_is_fixed`). A ação do URM altera somente o indicador booleano; ela não apaga a fronteira, não altera diretamente os registros do log e não regrava uma decisão no AST.

Na fonte, a ação está desenhada para limpar o estado que faz as ações nativas restringirem alternativas durante fixed rollback e, em seguida, devolver o índice original à interação de menu. O Ren'Py continua responsável por consumir o resultado e direcionar `Menu.execute()` ao bloco correspondente.

Isto permite uma conclusão estática sobre a intenção e o caminho de dados: **o URM abre uma rota programática para escolher uma alternativa durante a janela de fixed rollback, contornando a restrição de sensibilidade do botão nativo**. Não permite concluir, sem runtime, que todos os contextos/telas do jogo aceitam a troca, nem que a fronteira de fixed rollback foi removida. Como `begin()` também controla o ciclo de vida do indicador, o estado pode ser recalculado em uma fronteira posterior.

A configuração `fix_rollback_without_choice=False` é apenas o padrão do SDK; jogos podem sobrescrevê-la. Quando ela é `True`, `display_menu` também aciona `saybehavior()`. O alcance dessa interação sobre a tela modal do URM exige teste integrado antes de afirmar o comportamento final.

## Classificação

- **CONFIRMADO NA FONTE URM CONVERTIDA:** a ação limpa `rollback_is_fixed` antes de invocar `ChoiceReturn`; botão Select do URM declara `sensitive=True`.
- **CONFIRMADO NO SDK 7.4.11:** fixed rollback é representado pela combinação do estado `rollback_is_fixed` e da fronteira; as ações nativas consultam fixed rollback para limitar seleção; `ChoiceReturn` retorna seu valor; `Menu.execute` usa o resultado como índice estrutural.
- **HIPÓTESE FORTE a partir do fluxo:** limpar o indicador tem como efeito operacional pretendido liberar a seleção via URM durante a janela fixa. A ponte passa por ação de screen e interação ativa, então a integração precisa ser exercitada em runtime.
- **NÃO DEMONSTRADO:** a atribuição não prova que o URM remova a fronteira, altere o histórico, preserve a alternativa nova após outro rollback ou funcione da mesma forma quando `fix_rollback_without_choice=True`.
- **PENDENTE:** teste de runtime que crie uma decisão com `renpy.fix_rollback()`, faça rollback até antes dela, compare a seleção nativa e a seleção via URM, observe o bloco executado e repita com ambos os valores da configuração. Depois, testar novo rollback e save/load.

## Próximo experimento isolado

Usar uma fixture temporária fora de `wells/`, `wells_beta/`, das fontes originais do URM e do SDK:

1. Criar duas alternativas A/B com efeitos distintos no store e em labels.
2. Executar `renpy.fix_rollback()` em ponto conhecido, avançar e fazer rollback até a decisão fixada.
3. Registrar `in_fixed_rollback()`, `roll_forward_info()`, alternativa disponível e label/bloco efetivamente alcançado.
4. Repetir com ação nativa, ação de seleção URM reduzida e `fix_rollback_without_choice` igual a `False` e `True`.
5. Após a escolha forçada, avançar, aplicar outro rollback e observar a fronteira, o estado e o roll-forward.
6. Manter a evidência de runtime separada da conclusão estática e remover/arquivar a fixture de acordo com o fluxo de experimentação do laboratório.

Nenhum código protegido foi alterado nesta etapa.
