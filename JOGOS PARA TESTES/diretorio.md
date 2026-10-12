# Jogos para testes — laboratório Ren'Py

Este diretório reúne **cópias de estruturas de jogos reais** para pesquisa, reprodução de defeitos e validação das ferramentas desenvolvidas no laboratório.

## Finalidades

- **Compatibilidade:** verificar o comportamento das ferramentas em projetos Ren'Py de diferentes versões, estruturas, convenções e recursos.
- **Tradução e revisão:** comparar scripts nativos, traduções RPY e, quando disponíveis, pares JSON; identificar erros linguísticos, de formatação e de preservação de tokens.
- **Testes de integração:** reproduzir fluxos reais de extração, tradução, revisão e reinjeção, inclusive casos extremos.
- **Pesquisa técnica:** comparar funções, estruturas e comportamentos dos jogos com os projetos Wells e com SDKs Ren'Py adequados, quando necessário.
- **Novas investigações:** permitir outros usos relevantes que surjam durante o desenvolvimento, sem limitar o diretório à revisão linguística.

## Organização e preservação

Cada jogo deve permanecer em sua própria pasta, com a hierarquia original preservada tanto quanto possível. Os scripts e dados incluídos devem representar fielmente a cópia usada como referência.

Arquivos de imagem, áudio e fontes podem ser omitidos quando não forem necessários ao objetivo do teste. A ausência desses recursos **não comprova que a cópia seja executável** nem que contenha todos os componentes do jogo original.

**Não alterar as amostras para fazer os testes passarem.** Experimentos, saídas revisadas, relatórios e arquivos temporários devem ficar separados das cópias de referência. Antes de qualquer teste com escrita, criar uma cópia de trabalho.

## Critérios de validação

1. Registrar jogo, versão e caminhos de origem/tradução efetivamente encontrados.
2. Identificar a causa do defeito antes de propor correções automáticas.
3. Separar o que foi **COMPROVADO** nos arquivos, **TESTADO** em execução, é **HIPÓTESE** ou está **PENDENTE**.
4. Proteger código, identificadores, tags, variáveis, nomes e estruturas Ren'Py; não reescrever conteúdo nativo.
5. Transformar ocorrências úteis em testes mínimos, preferencialmente sem incorporar grandes trechos de obras de terceiros ao código-fonte das ferramentas.
6. Validar os resultados em múltiplos jogos antes de generalizar regras linguísticas ou de compatibilidade.

## Amostra inicial

**ThiefofHeartsPart1-0.0.3b-pc** — contém scripts originais em `game/scripts/`, traduções em `game/tl/brazil/scripts/` e o arquivo `game/tl/brazil/strings.json`. Serve inicialmente para investigar diálogos com erros de concordância, parentesco, títulos, pontuação e organização sintática, além de futuros testes de compatibilidade.

> Este diretório é um **corpus de referência**, não um componente de produção do Wells Manager. A presença de uma amostra não implica autorização para redistribuí-la fora do laboratório.
