# URM — Stores, monitoramento e substituição de texto (primeira validação)

**Data:** 2026-10-15. **Escopo:** inspeção estática do código convertido do URM. **Sem testes de runtime.** Nenhum arquivo protegido foi alterado.

## Fontes verificadas

Prefixo comum: `URM_REVERSO/01_MATERIAL_URM/2_URM_X52_CONVERTIDO/`.

- `classes/vars.rpy` SHA `57482937e14f215dac0ecb22a62da8ad160cba58`: linhas 5–138, 232–269, 437–479, 483–577.
- `classes/labels.rpy` SHA `96713d0297cf1bedeb9232502aa0d631d2a0780e`: linhas 5–32.
- `classes/textrepl.rpy` SHA `70ce9cc40378af1de5092255558659c8512a04f6`: linhas 5–64, 70–122.
- `classes/main.rpy` SHA `14f93406d2946eaed664ed72c1d47063984ce24f`: linhas 18–63 e 194–227.
- `classes/URMFiles.rpy` SHA `888aba28d9d2e7870d8c4e6526417390179cd326`: linhas 78–91, 231–248, 308–372.
- `screens/vars.rpy` SHA `7959b2c0e6249df0edbb9ebe683481d46e4537e1`: referências a `SetVarValue`, `CreateVar`, `VarsStore`, `URMFiles.Save/Load` (linhas 115–168, 192, 270, 370–445, 485, 563).
- `screens/watchpanel.rpy` SHA `8cc83f00838ed409183e85e4ebdb37ddf4433823`: acesso a `VarsStore.watchedStore` (linhas 77–108).

## 1. Quem consome os stores `.urm`?

**Confirmado no código:** `VarsStoreClass.store` acessa `URMFiles.file['vars']` e cria o store se ausente; `watchedStore` faz o mesmo para `'watched'` (`vars.rpy` 5–20). `LabelsStoreClass.store` usa `'labels'` (`labels.rpy` 5–12). `TextReplacementsClass.store` usa `'replacements'` (`textrepl.rpy` 10–16). `URMFile.getStore` carrega sob demanda (`URMFiles.rpy` 231–238).

| Store | Conteúdo demonstrado | Consumidor |
|---|---|---|
| `vars` | nomes lembrados e metadados `name`, `frozen`, `monitor`, `ignored` | `VarsStoreClass` |
| `watched` | nomes de variáveis e nomes de exibição | `VarsStoreClass.watchedStore` |
| `labels` | nomes de labels e nomes de exibição | `LabelsStoreClass` |
| `replacements` | texto original, substituição, `characterVar`, flags de case e palavra parcial | `TextReplacementsClass` |

**Distinção fundamental:** `VarsStore.remember` grava `{'name': ...}` e não uma cópia do valor da variável; `freeze` e `monitor` registram flags. Logo, o arquivo `.urm` armazena **configurações de acompanhamento e substituições** neste circuito, não um snapshot genérico de `renpy.store`.

## 2. Como `freeze` e `monitor` funcionam

**Confirmado no código:** `StoreMonitorClass.init` (`vars.rpy` 492–509) adiciona `_pythonCallback` a `renpy.config.python_callbacks` se o suporte estiver disponível e tenta localizar funções nativas `_m1_00action_data__set_field` ou `_set_field`. Clona a função e substitui seu `__code__` por um interceptador.

O interceptador (`vars.rpy` 521–524) consulta `handleVarChange` antes de chamar o `originalSetField`. Quando a variável está congelada, `handleVarChange` retorna `False`, bloqueando essa rota de atribuição, e tenta restaurar o valor anterior caso haja diferença (`vars.rpy` 526–538). Para variáveis monitoradas, se houver mudança e a tela de edição não estiver aberta, gera uma notificação.

O callback Python (`vars.rpy` 540–563) ativa `renpy.game.context().force_checkpoint = True`, obtém alterações do store via `renpy.store.__dict__.get_changes` e as envia a `handleVarChange`.

**Limites importantes:** a interceptação de `SetField` e o callback Python são **rotas distintas**, não prova de cobertura de todas as mutações possíveis. O comportamento efetivo depende do SDK 7.4.11 e precisa ser conferido, sobretudo `get_changes`, `force_checkpoint`, checkpoints e rollback. A substituição de `__code__` é invasiva; **não transportar para Wells sem análise de compatibilidade e testes**.

## 3. Substituição de texto não é edição de arquivo de script

**Confirmado no código:** `TextRepl.attachFilters` (`textrepl.rpy` 56–64) guarda filtros anteriores e configura `renpy.config.say_menu_text_filter` e `renpy.config.say_arguments_callback`. A instalação ocorre no `init 999` quando não há `pendingUpdate` (`textrepl.rpy` 119–122).

`_textFilter` aplica substituições armazenadas em `replacements` após eventual filtro anterior; `_sayFilter` trata nomes de personagens; `_replace` usa `str.replace` ou regex com opções de sensibilidade a maiúsculas e correspondência parcial (`textrepl.rpy` 70–116).

**Consequência:** o mecanismo demonstrado modifica a **representação de texto exibido**, não o arquivo `.rpy` no disco. Por atuar em `say_menu_text_filter`, também pode interferir na correlação entre texto original do menu e texto exibido: qualquer sistema de Walkthrough deve evitar tratar legenda filtrada como identidade única de Choice.

## 4. Quando o arquivo é carregado

`main.rpy` cria os objetos no `init 52`; `afterLoad` chama `StoreMonitor.init` e `URMFiles.autoLoad` (`main.rpy` 54–63). O `init 999` registra `afterLoad` em `renpy.config.after_load_callbacks` e `onLabelCalled` no monitor de labels (`main.rpy` 194–218). `URMFiles.autoLoad` depende de `Settings.lastLoadedFile` e de condições de `unsaved` (`URMFiles.rpy` 61–64).

**Limite:** o carregamento de stores é lazy e seu uso posterior é demonstrado por propriedades; isso não prova que cada regra foi aplicada em toda interação ou que o rollback preserva o estado desejado.

## 5. Hipóteses e testes pendentes

1. Verificar no SDK 7.4.11 a assinatura de `_set_field` e as versões da API `get_changes`; verificar se `python_callbacks` e `force_checkpoint` operam como suposto.
2. Criar cenários de `freeze` com atribuição direta, `SetField`, mutação de objetos, rollback e load de save; observar o que de fato é bloqueado.
3. Testar `replacements` com Choice, `say`, personagem dinâmico, texto traduzido e labels duplicadas; comparar `Menu.items` e legenda exibida.
4. Verificar se outras stores são adicionadas fora dos consumidores aqui inspecionados; não afirmar inventário global completo.
5. Rastrear se o estado de `watch`, `monitor`, `freeze` é restaurado ao abrir arquivos `.urm` e quando as interfaces os leem.

**Classificação:** fatos marcados como confirmados referem-se à fonte convertida. **Nenhum resultado de execução nem equivalência entre SDKs foi afirmado.**
