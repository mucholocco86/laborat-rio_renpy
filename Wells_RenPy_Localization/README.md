# Wells · Ferramentas Ren’Py

Ferramenta Wells com interface própria para as duas operações do SDK Ren’Py
8.5.3: **Gerar Traduções** e **Extrair Diálogos**. O frontend não abre o
launcher. Ele executa diretamente os comandos headless `translate` e
`dialogue` do engine Ren’Py selecionado.

## Executar individualmente

Requer Python 3.10+ e Tkinter. Na pasta `WELLS MANAGER BETA`, execute:

```text
python -m Wells_RenPy_Localization
```

Também é possível iniciar diretamente com `python
Wells_RenPy_Localization/standalone.py`.

Para gerar um executável individual no Windows, instale PyInstaller e execute
na raiz de `WELLS MANAGER BETA`:

```text
python -m PyInstaller --clean --noconfirm Wells_RenPy_Localization/Wells_RenPy_Localization.spec
```

Selecione a pasta do SDK Ren’Py 8.5.3 e a raiz do jogo (a pasta que contém
`game/`). Para gerar traduções, informe uma localização como `brazil`; o SDK
salva os arquivos em `game/tl/<idioma>/` (ou no diretório de tradução definido
pelo projeto). Para extrair, o SDK grava `dialogue.tab` ou `dialogue.txt` na
raiz do jogo.

O checkbox **Gerar strings vazias** corresponde ao argumento `--empty`. Na
extração, as opções reproduzem os argumentos `--strings`, `--notags` e
`--escape` do SDK. O idioma `None` extrai o texto padrão do projeto.

## Integração no Wells Manager Beta

No Manager, abra **Extrair traduções** e escolha **Ren’Py SDK · Extrair / Gerar**.
O submenu atual do Wells Translator permanece disponível. Ambas as interfaces
chamam `core.py`, portanto a montagem dos comandos e a lógica de execução são
compartilhadas.

## Dependência e limite de isolamento

O SDK deve ser selecionado no computador que executa a ferramenta. Os comandos
do Ren’Py dependem do compilador, loader, AST e estado do tradutor do próprio
engine; `dialogue.py` ou `generation.py` não funcionam isoladamente como um
parser Python comum. Esta implementação reutiliza o runtime do SDK sem iniciar
seu launcher. Ela ainda exige o SDK completo como dependência externa; não
afirma ser um pacote de runtime reduzido.

O Ren’Py pode criar/atualizar caches e arquivos compilados do projeto durante a
leitura. A ferramenta não edita os arquivos-fonte `.rpy` ou `.rpym`; valide em
uma cópia do jogo antes de uso quando for importante conservar também os
artefatos de cache.

## Fontes Ren’Py e licença

Baseada nos comandos upstream `renpy/translation/generation.py` e
`renpy/translation/dialogue.py`, além da interface de referência
`launcher/game/translations.rpy`, no SDK 8.5.3. Os arquivos do SDK têm avisos
MIT de Tom Rothamel. Se código upstream for copiado ou se o runtime do SDK for
redistribuído, preserve os avisos de copyright/licença e revise também
`renpy-8.5.3-sdk/LICENSE.txt` e os avisos das dependências empacotadas. Esta
ferramenta não redistribui o SDK.

## Testes

Os testes unitários do pacote verificam a montagem dos comandos e validação de
caminhos/opções. Comparação de saídas reais com o launcher do SDK 8.5.3 precisa
ser executada em um computador com o engine e um projeto Ren’Py de teste; este
repositório de código, sozinho, não comprova equivalência visual/funcional com
um jogo específico.
