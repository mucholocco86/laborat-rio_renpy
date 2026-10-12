# Thief of Hearts 0.0.3b — análise inicial das relações e traduções

**Estado:** inspeção estática de arquivos do laboratório; sem execução do jogo e sem alteração das amostras.  
**Origem:** `JOGOS PARA TESTES/ThiefofHeartsPart1-0.0.3b-pc/game/`.

## Rastreamento confirmado

- `script.rpy`: `label start` executa `jump lb_ep01_intro_01_fantasy_intro`.
- `TOH_Characters.rpy`: nomes e relações são variáveis independentes, incluindo `a_mc_rel`, `mc_a_rel`, `b_mc_rel`, `mc_b_rel`, `v_mc_rel`, `mc_v_rel`, `vic_mc_rel`, `mc_vic_rel`, formas de tratamento e grupos.
- `screens.rpy`: `screen set_rel()` compõe linhas em `hbox` com vários elementos `text _(...)` e `textbutton _("[variavel]")`. **A frase visual não é necessariamente uma string única.**
- `tl/brazil/strings.rpy` e `tl/brazil/strings.json`: contêm traduções de partes da interface, inclusive versões distintas de strings inteiras e fragmentadas. Não presumir qual variante é exibida sem seguir o fluxo de tradução efetivo.
- `game/scripts/` e `game/tl/brazil/scripts/`: scripts nativos e traduções RPY de diálogos; `tl/brazil/strings.json` é outro corpus, não prova por si só que todas as linhas da tela venham do JSON.

## Defeitos comprovados em pares nativo/tradução

| Origem (texto curto) | Tradução encontrada | Problema | Tratamento seguro |
| --- | --- | --- | --- |
| `She's your younger...` | `Ela é sua filha mais nova...` | Introduz **filha** onde o original deixa a relação aberta para a escolha seguinte. | Diagnóstico de especificação indevida; não substituir relação sem verificar contexto. |
| `She's your older...` | `Ela é sua irmã mais velha...` | Introduz **irmã** onde o original deixa a relação aberta. | Diagnóstico contextual, sem correção automática genérica. |
| `So I am her ...` | `Então eu sou ela...` | Perde a construção de relação `sou [relação] dela`. | Sugestão revisável, não regra cega. |
| `You call [a_name] and/or [b_name] your ...` | `Você liga [a_name] e/ou [b_name] seu...` | Falso cognato/seleção verbal inadequada: `call` interpretado como `ligar`. | Sinalizar com base no nativo; não trocar indiscriminadamente `liga`. |
| `He is my [rel], and I am his ...` | `Ele é meu [rel] E eu sou dele...` | Capitalização e pontuação anômalas; preservar `[rel]`. | Diagnóstico pontual, sem supor gênero do valor de `[rel]`. |
| `Quiet [b_name]. I'm trying to think.` | `Quieto [b_name] Estou tentando pensar.` | Falta fronteira/pontuação entre orações ao redor de token. | Sinalizar; eventual reparo apenas com contexto comprovado. |
| `She must've tracked [y_name] as soon as he entered the house...` | `Ela deve ter rastreado [y_name] Assim que ele entrou na casa...` | Capitalização após token e divisão sintática indevida. | Sinalizar, preservar `[y_name]`. |

**Nota importante:** as linhas `She's your younger...` e `She's your older...` são fragmentos da interface `set_rel`, adjacentes a botões que exibem valores de relação escolhidos pelo jogador. Um revisor isolado de strings não pode assumir `filha`/`irmã` como valor universal.

## Consequências para o Wells Manager

1. **Dois contextos distintos:** revisão de uma string de diálogo RPY e revisão de fragmentos de interface montados por `hbox`. Uma frase exibida pode atravessar várias unidades traduzíveis.
2. **Blindagem de tokens:** nunca alterar `[a_mc_rel]`, `[b_mc_rel]`, `[rel]`, `[y_name]` ou quaisquer tokens Ren'Py.
3. **Relações bidirecionais:** `mc_a_rel` e `a_mc_rel` não são intercambiáveis; concordância e sentido dependem do ponto de vista e da escolha.
4. **JSON não é a tela:** verificar a origem exata das strings (`strings.rpy`, `strings.json`, scripts, substituições) antes de atribuir a falha a um revisor ou tradutor específico.
5. **Correção automática conservadora:** primeiro classificar como `detectável`, `sugestão` ou `correção segura`; não reescrever parentescos livremente.
6. **Testes:** criar fixtures mínimos para (a) termo de parentesco inserido indevidamente antes de valor variável, (b) erro `call`→`ligar`, (c) `sou ela` em construção relacional, (d) falta de pontuação ao redor de token, (e) fragmentos independentes de `hbox`. Testar com/sem nativo e exigir idempotência e preservação de tokens.

## Pendências

- Reconstruir a sequência exata da introdução e relacionar cada screenshot ao bloco correspondente.
- Determinar precedência/uso efetivo de `strings.rpy`, `strings.json` e `replaceText.rpy` no jogo.
- Executar os revisores em **cópias de trabalho** dos dados exportados; comparar entradas, saídas e falso-positivos.
- Verificar CI e resultados dos testes existentes antes de promover qualquer nova regra à produção.

**Classificação:** caminhos, variáveis, montagem `hbox` e pares citados = **COMPROVADO**; resultado do jogo em execução e correções automáticas = **PENDENTE**.


## Validação automatizada — checkpoint 2026-10-12

- CI `38301010914`, commit `109b924`: **49 testes aprovados**.
- Os testes de diagnóstico derivados do corpus passaram tanto no RPY quanto no JSON.
- O JSON agora expõe `linguistic_issues` sem retraduzir automaticamente os casos ambíguos.
- Uma segunda bateria usa variantes textuais copiadas dos pares efetivamente presentes em `tl/brazil/strings.json` e `tl/brazil/strings.rpy`, inclusive um **controle negativo real**: `She's your younger... (Enter relationship - Default:` → `Ela é sua mais nova... (Insira o tipo de relacionamento - Padrão:` não deve ser marcado como parentesco inventado.
- Commit dessa bateria física: `ec336f6`; CI ainda deve ser confirmada antes de classificá-la como TESTADA.

### Evidência adicional do corpus

O mesmo conceito aparece em variantes diferentes no próprio pacote: há uma tradução de `She's your younger...` sem parentesco inserido e outra com `filha`. Isso reforça que a regra deve comparar estrutura/semântica do par, e não simplesmente condenar a expressão `mais nova`.

**Classificação atual:** camada de diagnóstico no checkpoint `109b924` = **TESTADO**; bateria física `ec336f6` = **PENDENTE DE CI**; autocorreção dos casos relacionais = **PENDENTE**.
