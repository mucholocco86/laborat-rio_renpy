# Build do Wells SDK

O executável individual é Windows e empacota a interface Wells e o runtime recortado do Ren'Py 8.5.3. O usuário não precisa selecionar ou instalar outra cópia do SDK.

## Preparação

Abra o terminal na pasta `WELLS MANAGER BETA` e execute:

```bat
py -3.11 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install pyinstaller python-docx
```

`python-docx` é usado pelo Wells Manager. O Wells SDK individual usa Tkinter da instalação Python.

## Testes e executável individual

```bat
python -m unittest discover -s wells_sdk/tests -p "test_*.py" -v
python -m PyInstaller --clean --noconfirm wells_sdk/Wells_SDK.spec
```

Saída esperada: `dist\Wells_SDK.exe`.

## Executável do Wells Manager integrado

```bat
python -m unittest discover -s wells_sdk/tests -p "test_*.py" -v
python -m unittest discover -s tests -p "test_*.py" -v
python -m PyInstaller --clean --noconfirm Wells_Manager.spec
```

Saída esperada: `dist\Wells_Manager.exe`. O `.spec` integrado inclui o mesmo runtime e os mesmos módulos `wells_sdk`; as duas interfaces chamam `wells_sdk.core`.

## Arquivos do runtime

`wells_sdk/runtime/` contém o engine e bibliotecas Windows do Ren'Py 8.5.3 necessários para ler os projetos e executar `translate` e `dialogue`. Mantém o `LICENSE.txt` upstream e os avisos de dependências incluídos. Não copie para lá o launcher, os projetos de exemplo, a documentação ou ferramentas de build de outras plataformas.

O runtime ainda precisa ser aberto e testado em Windows com uma cópia de jogo. A aprovação dos testes unitários não confirma equivalência real com o launcher, criação de arquivos ou funcionamento do `.exe`.

