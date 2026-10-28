# 50 — Stores `labels`/`replacements` e snapshots em memória

**Data:** 2026-10-28. **Alvo:** URM X52 convertido e SDK Ren'Py 7.4.11. **Status:** inspeção estática; runtime de snapshots e filtros restaurados a partir de `.urm` pendente.

## Fontes consultadas

- URM convertido `classes/labels.rpy`, blob SHA `96713d0297cf1bedeb9232502aa0d631d2a0780e`, principalmente `LabelsStoreClass` (linhas 5–33) e `LabelMonClass` (aprox. 132–158).
- URM convertido `classes/textrepl.rpy`, blob SHA `70ce9cc40378af1de5092255558659c8512a04f6`, `TextReplacementsClass` (linhas 5–116).
- URM convertido `classes/snapshots.rpy`, blob SHA `20b45be23df8f12d7f4dfca7a1f401642d6fedba`, `SnapshotsClass` (linhas 5–91).
- SDK `renpy/pydict.pyx` e `renpy/python.py` no repositório canônico, para a semântica de `DictItems` usada no código de snapshots.
- URM convertido `classes/URMFiles.rpy`, blob SHA `888aba28d9e2d7870d8c4e6526417390179cd326`, para o contêiner ZIP/JSON descrito no documento 48.

## Store `labels`

**CONFIRMADO NA FONTE URM CONVERTIDA:** `LabelsStoreClass.store` cria/usa a entrada `.urm` chamada `labels`. `remember(labelName, displayName)` grava um registro semelhante a `{labelName: {"name": displayName}}`; `forget`, `changePos`, `sort` e `clear` alteram essa lista.

Essa estrutura é uma lista de labels lembrados com um rótulo de exibição. Não armazena o corpo AST nem as consequências executadas pelo label. `LabelMonClass` é outro objeto: instala `config.label_callback`, acompanha `lastLabel` e notifica callbacks; não grava cada execução na entrada `.urm` `labels` no código examinado.

## Store `replacements`

**CONFIRMADO NA FONTE URM CONVERTIDA:** `TextReplacementsClass.store` cria/usa a entrada `.urm` `replacements`. Cada regra guarda o texto original, substituição, referência opcional a variável de personagem e opções de sensibilidade a maiúsculas/minúsculas e correspondência parcial.

`attachFilters()` instala callbacks em `renpy.config.say_menu_text_filter` e `renpy.config.say_arguments_callback` quando compatível. Os filtros consultam `self.store` e aplicam regras ao texto e aos nomes de personagens. Portanto, a regra é configuração persistida pelo URM que altera a apresentação em runtime; ela não reescreve o script `.rpy` nem é uma alteração do valor narrativo/variável por si só.

O método `URMFiles.load()` troca o objeto `URMFiles.file`; como `TextRepl.store` consulta essa propriedade quando acessada, a fonte sugere que as regras carregadas passam a alimentar os filtros já instalados. Isso é **inferência estática**; falta comprovar em runtime a aplicação de regra carregada em save de outro processo.

## Snapshots de variáveis

**CONFIRMADO NA FONTE URM CONVERTIDA:** `SnapshotsClass.create()` mantém snapshots em `self._m1_snapshots__snapshots`, um `OrderedDict` dentro da instância em memória. O método chama `renpy.python.DictItems(renpy.store.__dict__).as_dict()`. Não acessa `URMFiles` nem cria um store `.urm`.

No SDK 7.4.11, `DictItems` em `renpy/pydict.pyx` copia os pares do dicionário mantendo referências aos objetos chave e valor (`Py_XINCREF`); `as_dict()` cria outro dicionário apontando para os mesmos objetos valor. Não é cópia profunda.

`Snapshots.findDictChanges()` compara valores de chaves no nível superior. Para uma variável escalar substituída por outra, o snapshot antigo mantém a referência ao escalar anterior e pode mostrar a diferença. Para uma lista/dicionário alterado in-place, o snapshot e o store corrente podem apontar para o mesmo objeto já mutado; a inspeção estática indica que a comparação pode não detectar a mutação interna. **Implicação inferida da semântica de referência; falta teste runtime com lista e dicionário.**

O snapshot é uma ferramenta de comparação da tabela de variáveis corrente. A fonte examinada não define esse mecanismo como checkpoint Ren'Py e não o conecta à serialização `.urm`. Sua sobrevivência a save nativo também não foi testada aqui.

## Quadro de distinção

| Recurso | Onde os dados ficam segundo a fonte | O que representam | Relação com gameplay |
|---|---|---|---|
| `labels` | Store `.urm` | Labels lembrados e nomes de exibição | Ajuda organização/acesso; não guarda execução do label |
| `replacements` | Store `.urm` | Regras de substituição de texto/nome | Filtros alteram apresentação em runtime |
| `Snapshots` | Instância `SnapshotsClass` em memória | Referências à tabela do store no instante da captura | Compara variáveis; não é rollback nem store `.urm` |
| Save nativo | Persistência Ren'Py | Estado serializado do jogo conforme o mecanismo nativo | Já validado para o valor/rota nos docs 46–47 |

## Pendências verificáveis

1. Gravar e carregar stores `labels` e `replacements` por `.urm` em processos separados; conferir as entradas JSON.
2. Aplicar uma regra de substituição carregada a uma fala e a uma Choice, comprovando o filtro em runtime.
3. Criar snapshot com escalar, lista e dicionário; alterar escalar por atribuição e containers in-place; observar exatamente o diff retornado.
4. Testar se snapshots sobrevivem a save/load nativo, sem presumir que sobrevivam por serem objetos do módulo `x52URM`.

As fixtures devem usar jogo descartável Ren'Py 7.4.11. Nenhum Wells, SDK ou fonte original deve ser modificado.
