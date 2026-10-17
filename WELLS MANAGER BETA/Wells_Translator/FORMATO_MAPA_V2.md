# Wells Translator — mapa e marcadores protegidos (v2)

O Translator exporta os textos OLD/NEW de arquivos RPY para TXT ou DOCX, em arquivo completo ou em blocos. Os delimitadores de string do RPY não são incluídos nos documentos.

## Marcadores Ren'Py

Conteúdo entre chaves, como `{b}` e `{k=-1.2}`, e entre colchetes, como `[player]`, é transportado como sentinela Wells, por exemplo `[[WELLS_P_000000]]`. A sequência exata fica registrada no `wells_translation_map.json`.

Mantenha as sentinelas no NEW. Não as traduza, remova, duplique ou reordene. O Revisor verifica os marcadores antes de revisar o NEW; o injetor só grava depois de validar o mapa e restaura os tokens Ren'Py originais do arquivo TL selecionado. Se uma sentinela foi alterada, corrija o NEW antes da injeção.

Aspas que fazem parte do diálogo continuam sendo texto. Ao reconstruir a string RPY, o injetor escapa os caracteres necessários para a sintaxe.

## Mapa v2 e fluxo de revisão

O mapa registra IDs ordenados, tipo de entrada, arquivo e linhas de origem/destino, hashes dos arquivos TL e do OLD, além das sequências de marcadores do original e da tradução atual. O Revisor TXT/DOCX usa o mapa e o OLD pareado como referência sem procurar a pasta TL do jogo. A blindagem continua decidindo quais nomes próprios devem ser preservados ou restaurados antes da injeção; os demais trechos podem ser traduzidos.

A sequência recomendada é: extrair OLD/NEW e o mapa; traduzir o NEW; revisar o NEW com o OLD correspondente e a blindagem; injetar. O usuário pode revisar nomes e títulos antes de confirmar a injeção.

Mapas de versão anterior exigem uma nova extração para usar o fluxo v2. Arquivos antigos sem mapa seguem apenas pelo caminho legado compatível quando os registros correspondem ao formato anterior.
