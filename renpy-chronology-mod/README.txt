CHRONOLOGY MOD
==============

A choice history tracker for Ren'Py visual novels. Records every decision you make, shows which paths you've seen and which are still locked, and lets you jump back to any past choice to try a different one.



INSTALLATION
------------

Download the zip from the latest release and follow the steps for your platform.


Windows

1. Open your game's install folder (right-click the shortcut → Open file location, or find it in Steam).
2. Right-click the zip → Extract All, and set the destination to the game's root folder.
3. The mod files will be copied into game/ automatically.


macOS

The game is packaged as a .app bundle, so the game/ folder is hidden inside it.

1. Extract the zip — you'll get a game/ folder.
2. Find the game in Finder, right-click the .app → Show Package Contents.
3. Navigate to Contents/Resources/autorun/.
4. Drag the game/ folder from the zip into the autorun/ folder. When prompted to merge, choose Merge.

Launch the game — no further setup needed. Works on existing saves; the mod starts recording from the point you install it.



CONTROLS
--------

Key                   Action
T                     Open / close timeline
R                     Open / close route tracker
Esc                   Close



FEATURES
--------


Choice Timeline

Every menu choice you make is recorded as a card in the timeline. Each card shows a thumbnail from when the choice appeared, the option you picked, and a dot if any option in that menu leads to content you haven't seen yet.


New Content Indicators

The mod walks the game's script at startup to detect which options lead to unseen content. A dot (●) marks any card or option that still has unexplored paths. The header shows how many choices in your history have new paths available and how many branches across the game are still locked.


All Options Modal

Click All options on any past card to see every choice that was available at that point:
- → marks the option you chose
- A muted → marks the option from the path your current save branched off from
- A dot marks options with unseen content


Jump Back and Replay

In the modal, click any option to jump back to that point and play forward with a different choice. The mod saves a recovery point first, so you can always return to where you were.

Playing what-if from a save. If you want to try a different choice without losing your current progress, save to a new slot first — that keeps your current run intact. Then jump back to an earlier choice from your original save. Now you have two independent runs: one continuing as it was, one playing out differently from that point. You don't have to replay the whole game just to see what changes.

The new run carries hints from the original, so you know exactly where the two paths diverge:
- At each upcoming choice, a muted → shows what you picked on the original run. Follow it or go a different way.
- The point where you split off gets a ⎇ marker in your timeline.
- Further down, any choice where the two runs differ also shows ⎇ — open the modal on those cards to see what the original path took.

Hints persist across saves and loads. They clear as each matching choice is reached, and reset if you jump again.


Chapter Markers

If the mod is configured with your game's chapters, the timeline shows a divider at the end of each chapter. Clicking the divider jumps directly to that chapter's ending — useful for catching up on a new update without replaying everything.


Route Tracker

Press R to open the route tracker. It shows the story variables that gate content — route flags, relationship values, stat choices — and what they're currently set to. Variables tied to the most recent branch cards are highlighted at the top.


Branch Cards

When the game evaluates a story branch between your choices, the route screen shows one card per path. A lock icon means you've never seen that path. A dim overlay means you've seen it on a previous playthrough. No overlay means you took it this run. Branch cards clear at the next choice.


Branch Notifications

When you pass through a branching point, a brief toast appears: ⎇ if there are paths you haven't taken, ⎇ New path if the branch you just took is itself new.

When a story variable changes mid-scene, a separate toast shows what changed — ↑ Affection, Route → romance, etc. These are off by default. To enable them, open the route tracker (R) and toggle Var change notifs in the header.


Save Compatibility

- Installing mid-playthrough: the mod starts recording from that point. Earlier choices show no history, which is expected.
- Removing the mod: existing saves load normally. Ren'Py ignores the unused _tl_* variables. A _tl_thumbs.pkl file in the save directory can be deleted manually — it is only used by the mod.
- Loading a corrupted save: history is validated and any malformed entries are dropped silently.



REN'PY COMPATIBILITY
--------------------

Should work with most Ren'Py 7 and 8 versions. The background blur may not render on some Ren'Py 7 renderers, but all other features work normally. Chapter markers may not work with all Ren'Py 7 versions.




================================================================================================
================================================================================================
================================================================================================

MOD DE CRONOLOGIA
==============

Um rastreador de histórico de escolhas para visual novels Ren'Py. Registra todas as suas decisões, mostra quais caminhos você já explorou e quais ainda estão bloqueados, e permite que você retorne a qualquer escolha anterior para tentar uma diferente.

INSTALAÇÃO
------------

Baixe o arquivo zip da versão mais recente e siga os passos para a sua plataforma.

Windows

1. Abra a pasta de instalação do seu jogo (clique com o botão direito no atalho → Abrir local do arquivo ou encontre-a no Steam).

2. Clique com o botão direito no arquivo zip → Extrair tudo e defina o destino para a pasta raiz do jogo.

3. Os arquivos do mod serão copiados automaticamente para a pasta game/.

macOS

O jogo é empacotado como um aplicativo (.app), então a pasta game/ está oculta dentro dele.

1. Extraia o arquivo zip — você obterá uma pasta game/.

2. Encontre o jogo no Finder, clique com o botão direito do mouse no arquivo .app → Mostrar Conteúdo do Pacote.
3. Navegue até Conteúdo/Recursos/autorun/.
4. Arraste a pasta game/ do arquivo zip para a pasta autorun/. Quando solicitado a mesclar, escolha Mesclar.

Inicie o jogo — nenhuma configuração adicional é necessária. Funciona com jogos salvos existentes; o mod começa a gravar a partir do momento da instalação.

CONTROLES
--------

Tecla Ação
T Abrir/fechar a linha do tempo
R Abrir/fechar o rastreador de rotas
Esc Fechar

RECURSOS
--------

Linha do Tempo de Escolhas

Cada escolha de menu que você fizer é registrada como um cartão na linha do tempo. Cada cartão mostra uma miniatura de quando a escolha apareceu, a opção que você selecionou e um ponto se alguma opção nesse menu levar a conteúdo que você ainda não viu.

Indicadores de Novo Conteúdo

O mod percorre o script do jogo na inicialização para detectar quais opções levam a conteúdo inédito. Um ponto (●) marca qualquer carta ou opção que ainda tenha caminhos inexplorados. O cabeçalho mostra quantas escolhas no seu histórico têm novos caminhos disponíveis e quantas ramificações no jogo ainda estão bloqueadas.

Modal de Todas as Opções

Clique em "Todas as opções" em qualquer carta anterior para ver todas as escolhas disponíveis naquele ponto:
- → marca a opção que você escolheu
- Um → apagado marca a opção do caminho a partir do qual seu jogo salvo atual se ramificou
- Um ponto marca opções com conteúdo não visto

Voltar e Repetir

No modal, clique em qualquer opção para voltar a esse ponto e jogar com uma escolha diferente. O mod salva um ponto de recuperação primeiro, para que você sempre possa retornar de onde parou.

Jogando "e se" a partir de um jogo salvo. Se você quiser tentar uma escolha diferente sem perder seu progresso atual, salve em um novo slot primeiro — isso mantém sua partida atual intacta. Em seguida, volte para uma escolha anterior do seu jogo salvo original. Agora você tem duas partidas independentes: uma continuando como estava e outra se desenrolando de forma diferente a partir desse ponto. Você não precisa jogar o jogo inteiro novamente só para ver as mudanças.

A nova partida traz dicas da original, para que você saiba exatamente onde os dois caminhos se separam:
- Em cada escolha futura, um → discreto mostra o que você escolheu na partida original. Siga essa escolha ou vá por um caminho diferente.

- O ponto onde você se separa recebe um marcador ⎇ na sua linha do tempo.

- Mais adiante, qualquer escolha onde as duas partidas divergem também mostra um ⎇ — abra o modal nesses cartões para ver o caminho original.

As dicas persistem entre os jogos salvos e carregados. Elas desaparecem ao alcançar cada escolha correspondente e são redefinidas se você pular novamente.

Marcadores de Capítulo

Se o mod estiver configurado com os capítulos do seu jogo, a linha do tempo mostra um divisor no final de cada capítulo. Clicar no divisor leva você diretamente ao final daquele capítulo — útil para acompanhar uma nova atualização sem precisar jogar tudo de novo.

Rastreador de Rotas

Pressione R para abrir o rastreador de rotas. A tela exibe as variáveis ​​da história que controlam o conteúdo — indicadores de rota, valores de relacionamento, escolhas de atributos — e seus valores atuais. As variáveis ​​vinculadas aos cartões de ramificação mais recentes são destacadas na parte superior.

Cartões de Ramificação

Quando o jogo avalia uma ramificação da história entre suas escolhas, a tela de rotas exibe um cartão para cada caminho. Um ícone de cadeado significa que você nunca viu esse caminho. Uma sobreposição esmaecida significa que você já o viu em uma partida anterior. Sem sobreposição significa que você o escolheu nesta partida. Os cartões de ramificação desaparecem na próxima escolha.

Notificações de Ramificação

Ao passar por um ponto de ramificação, uma breve notificação aparece: ⎇ se houver caminhos que você ainda não percorreu, ⎇ Novo caminho se a ramificação que você acabou de escolher for nova.

Quando uma variável da história muda no meio de uma cena, uma notificação separada mostra o que mudou — ↑ Afeto, Rota → romance, etc. Essas notificações estão desativadas por padrão. Para ativá-las, abra o rastreador de rotas (R) e ative a opção Notificações de alteração de variáveis ​​no cabeçalho.

Compatibilidade com jogos salvos

- Instalação durante o jogo: o mod começa a gravar a partir desse ponto. Escolhas anteriores não mostram histórico, o que é esperado.

- Remoção do mod: os jogos salvos existentes carregam normalmente. O Ren'Py ignora as variáveis ​​_tl_* não utilizadas. Um arquivo _tl_thumbs.pkl no diretório de jogos salvos pode ser excluído manualmente — ele é usado apenas pelo mod.

- Carregar um jogo salvo corrompido: o histórico é validado e quaisquer entradas malformadas são descartadas silenciosamente.

COMPATIBILIDADE COM REN'PY
--------------------

Deve funcionar com a maioria das versões do Ren'Py 7 e 8.