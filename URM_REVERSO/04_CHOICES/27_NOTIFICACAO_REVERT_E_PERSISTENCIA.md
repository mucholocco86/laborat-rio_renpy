# 27 — Notificação de variável, ação “Revert” e persistência

**Data:** 2026-10-20  
**Escopo:** separar notificações do StoreMonitor, a ação visual “Revert”, configurações de notificação, arquivo .urm e save nativo.  
**Evidência:** inspeção estática do código convertido do URM. Não foi executado o pacote completo do URM nesta etapa.  
**Proteções:** nenhum arquivo original do URM, SDK, wells/ ou wells_beta/ foi alterado.

## Conclusão principal

A notificação de variável alterada é um objeto transitório em uma lista de NotificationsClass. O botão chamado **Revert** na janela da notificação não aciona renpy.rollback(): ele usa SetVarValue para atribuir à variável o valor anterior recebido pela tela. É uma correção manual do valor corrente, não uma restauração do histórico de execução.

A configuração notificationTimeout é persistida pelos mecanismos de Settings. Isso não demonstra que os objetos das notificações sejam persistidos junto com ela.

## Circuito da notificação

1. StoreMonitor.handleVarChange detecta que a variável tem a flag monitor, compara valor antigo e atual, e chama Notifications.add(...) se a tela de edição do URM não estiver aberta.
2. NotificationsClass.add cria Notification, adiciona o objeto a self.notifications e reinicia a interação.
3. A screen URM_notifications percorre essa lista e exibe rótulo/texto. Ao clicar, a ação do objeto é executada e a notificação é removida.
4. Se Settings.notificationTimeout for diferente de zero, add agenda uma thread para remover a notificação após o intervalo.

A lista é criada como [] em NotificationsClass.__init__; os métodos examinados alteram essa lista em memória. A classe de notificações não escreve diretamente em persistent, em arquivo .urm ou em arquivo global.

## O que “Revert” realmente faz

A tela URM_var_changed(varName, prevVal) apresenta valor anterior e valor atual. O botão Revert invoca SetVarValue(var, newValue=prevVal). Isso leva a Var.setValue, que faz atribuição no store do jogo. A ação não chama renpy.rollback(), não restaura o Context e não desfaz outros efeitos que ocorreram depois da mudança.

Portanto, se a variável monitorada mudou de 10 para 20, o botão tenta escrever 10 novamente no estado atual. Esse ato pode ele próprio ser registrado no histórico nativo como uma nova mutação do store, mas o efeito temporal exato na sessão integral ainda não foi testado.

Se a variável estiver congelada, Var.setValue tenta removê-la temporariamente da lista congelada, realiza a escrita e a congela novamente no bloco finally. O botão Revert usa essa mesma rota.

## Quatro superfícies de dados separadas

| Superfície | Conteúdo confirmado | Relação com notificações |
|---|---|---|
| Lista Notifications.notifications | objetos com rótulo, texto e ação; remoção por fechar, limpar ou timeout | Dados transitórios em memória no circuito examinado |
| Configuração notificationTimeout | intervalo de duração das notificações | Settings.set persiste em persistent.URMSettings por padrão; opção global escreve JSON em arquivo compactado próprio |
| Arquivo .urm | stores de ferramentas como vars, watched, labels, replacements e propriedades | A classe Notifications não aparece como store consumidor/produtor no circuito consultado |
| Save nativo | Gamesaves.save/load delegam para renpy.save/load | É o mecanismo de save de gameplay; a interação de objetos de notificação com esse ciclo precisa de teste |

### Cuidado com save/load nativo

NotificationsClass herda de x52NonPicklable. No código convertido, essa base define __getstate__ como {} e __setstate__ como operação vazia. Isso demonstra que o estado Python serializado por esses hooks não inclui os atributos normais do objeto. **Não é suficiente, isoladamente, para afirmar o resultado visível de um save/load**: o ciclo de reconstrução do store do Ren’Py e a disponibilidade da lista após carregar ainda precisam ser observados em runtime.

A mesma distinção vale para StatesClass: o mapa _states mostrado na fonte pertence ao objeto URM e não é escrito explicitamente em persistent nem no arquivo .urm pelos métodos examinados. Não inferir sua vida útil após carregar uma partida sem teste.

## Classificação

- **CONFIRMADO NA FONTE URM CONVERTIDA:** NotificationsClass mantém e remove objetos de uma lista em memória; timeout também remove dessa lista.
- **CONFIRMADO NA FONTE URM CONVERTIDA:** o botão “Revert” chama SetVarValue com prevVal; é uma atribuição, não uma chamada ao mecanismo de rollback.
- **CONFIRMADO NA FONTE URM CONVERTIDA:** notificationTimeout é uma configuração acessada por Settings, cujos destinos de persistência são persistent.URMSettings e arquivo global próprio.
- **CONFIRMADO NA FONTE URM CONVERTIDA:** os hooks de x52NonPicklable retornam estado vazio e não restauram estado próprio.
- **PENDENTE DE RUNTIME:** se notificações visíveis sobrevivem, desaparecem ou são reconstruídas após carregar save nativo; e se uma notificação pendente acompanha um rollback da sessão.
- **PENDENTE DE RUNTIME:** se a atribuição executada pelo botão Revert é imediatamente reversível e qual fronteira a desfaz, considerando a posição corrente no histórico.

## Fontes consultadas

| Arquivo convertido | Símbolos / intervalos | Blob SHA |
|---|---|---|
| classes/notifications.rpy | NotificationsClass, Notification (5–43) | 3283ec4b1615967a71ad21cc34670bf8158ab96d |
| classes/vars.rpy | StoreMonitor.handleVarChange, callback e Var.setValue | 57482937e14f215dac0ecb22a62da8ad160cba58 |
| screens/vars.rpy | URM_var_changed: botões Change/Revert/Close (453–487) | 7959b2c0e6249df0edbb9ebe683481d46e4537e1 |
| screens/watchpanel.rpy | renderiza e executa notificações; ação para limpar todas (330–351) | 8cc83f00838ed409183e85e4ebdb37ddf4433823 |
| classes/settings.rpy | leitura/escrita de Settings e destinos persistentes (151–218) | 13fd70596135c4389c9ab01cae982f80bfcad461 |
| classes/URMFiles.rpy | stores do arquivo, serialização ZIP/JSON e load/save (194–220, 308–372) | 888aba28d9d2e7870d8c4e6526417390179cd326 |
| classes/gamesaves.rpy | wrappers de save/load nativos | bbedbd08f9ce106c77a12bdb984e11008cf995bf |
| classes/states.rpy | mapa local de flags transitórias | b787b94fc40183b24165d2844a0f91bc12980626 |
| framework/modules/01utils.rpy | hooks de x52NonPicklable | e558a2d5a5137608e542238a1d81fd65e6db349d |

## Próximo teste reduzido recomendado

No SDK 7.4.11, gerar uma notificação sintética com valor anterior conhecido; comparar três ações isoladas: fechar a notificação, clicar Revert, e acionar rollback nativo. Registrar valor do store, fronteira/contexto e existência da notificação antes/depois. Em outro cenário, salvar e carregar com uma notificação pendente, observando a screen e o objeto. Esse teste separa a semântica da ação Revert da persistência visual da lista sem executar ou modificar o pacote integral do URM.

## Atualização de runtime — fixtures reduzidas (2026-10-20)

Esta seção atualiza as pendências de runtime acima com resultados posteriores. Ela **não** substitui os limites de escopo indicados no restante do documento.

### Ação “Revert”

A fixture reproduziu a chamada da tela: `SetVarValue(Var(...), newValue=prevVal)()`. No run [39379101294](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39379101294), o valor corrente começou em 20, com marcador independente de rota em 1 e valor anterior 10. Após a ação, o valor passou a 10 e o marcador permaneceu 1 (`20 / rota 1 / prev 10 → 10 / rota 1`). O teste passou no SDK 7.4.11.

**Classificação:** observado em runtime numa fixture reduzida; confirma que a reprodução da ação faz uma atribuição e não retrocede o fluxo ou desfaz o marcador de rota. Isso corrobora a leitura estática, mas não é um teste da tela nem do pacote integral do URM. A interação dessa atribuição com um rollback posterior e com os deltas internos do log continua pendente.

### Notificações: resultados de save/load e rollback já registrados

O documento [31 — Ciclo de vida das notificações do URM e rollback](31_NOTIFICACOES_E_ROLLBACK_CICLO_DE_VIDA.md) e os runs associados já fecharam parte da antiga pendência:

- **Mesma sessão:** nos runs [39214784786](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39214784786) e [39215118198](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39215118198), após salvar e mutar a lista em seguida, o load reduziu a lista ao item pós-save observado pela fixture, em vez de restaurar o item que existia no instante do save. É um resultado específico da rota testada, não uma regra universal para qualquer objeto URM.
- **Processo novo:** nos runs [39215564208](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39215564208), [39229685100](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39229685100) e [39230107907](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39230107907), o singleton da fixture começou vazio após init e permaneceu vazio depois do load; a screen foi reconstruída sem o botão que representaria a notificação. O último teste reproduziu um callback pós-load, mas não carregou o pacote dinâmico original do URM nem seu arquivo `.urm`.
- **Rollback da lista:** o run [39205520906](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/39205520906) comparou `clear()` e remoção in-place, além do timeout reduzido. Com a screen ativa, `clear()` deixou a lista vazia após rollback; `remove()` restaurou o item; a remoção temporizada também foi revertida na execução controlada. Esses resultados pertencem ao harness reduzido e não demonstram concorrência geral nem integração com a `NotificationsClass` real.

Assim, a antiga formulação “save/load pendente” precisa ser lida como **save/load reduzido parcialmente observado; integração do URM integral pendente**. O singleton, o callback e a screen da fixture reproduzem partes do circuito, não o loader real e os módulos `.x52` do URM.

### Fontes de evidência e limites

- Fixture e workflow do teste “Revert”: fixture commit [8d08fa82d3a7e3bdd2862c2dd8ddd2a60c538524](https://github.com/mucholocco86/laborat-rio_renpy/commit/8d08fa82d3a7e3bdd2862c2dd8ddd2a60c538524) e workflow commit [ee18b6cbb823cf7f91cdf6ac69173d43e58fae40](https://github.com/mucholocco86/laborat-rio_renpy/commit/ee18b6cbb823cf7f91cdf6ac69173d43e58fae40).
- A fixture é uma reprodução reduzida no SDK Ren’Py 7.4.11. Não editou o Wells estável, `wells_beta/`, o SDK ou fontes originais do URM.
- Continua pendente executar o pacote convertido completo: o loader exige módulos e telas dinâmicas `.rpy.x52` que não estão presentes no jogo reduzido. Também falta testar a atribuição Revert seguida por rollback em diferentes pontos do histórico, bem como a interação com freeze/monitor e save/load do jogo real.

### Classificação atualizada

- **CONFIRMADO NA FONTE URM CONVERTIDA:** Revert encaminha `prevVal` para `SetVarValue`; não chama `renpy.rollback()`.
- **OBSERVADO EM RUNTIME (fixture reduzida, SDK 7.4.11):** a ação reproduzida reatribui 10 ao valor corrente 20 e conserva o marcador de rota 1.
- **OBSERVADO EM RUNTIME (fixtures reduzidas):** há diferenças entre rollback de `clear()` e remoção in-place da lista, e entre load na mesma sessão e load em processo novo, conforme casos e runs acima.
- **PENDENTE:** comportamento da screen e dos objetos da `NotificationsClass` no pacote integral, além do rollback posterior à ação Revert e suas combinações com save/load e metadados de monitoramento.