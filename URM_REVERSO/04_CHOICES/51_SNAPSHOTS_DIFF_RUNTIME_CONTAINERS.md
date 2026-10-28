# 51 — Snapshots do diff: escalares versus containers mutados in-place

**Data:** 2026-10-28. **SDK:** Ren'Py 7.4.11. **Evidência:** runtime com a API `Snapshots` original em jogo descartável. **Run inicial:** [40658456177 — SUCCESS](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/40658456177). **Ampliações:** [40676323550 — SUCCESS](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/40676323550) e [40676920686 — SUCCESS](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/40676920686) e [40677490829 — SUCCESS](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/40677490829).

## Pergunta

O snapshot do URM detecta uma variável escalar substituída e mudanças internas em listas/dicionários que já existiam quando o snapshot foi criado?

## Procedimento reproduzível

Fixture: [urm_snapshot_shallow_probe.rpy](../tools/fixtures/urm_snapshot_shallow_probe.rpy). Workflow independente: [urm-snapshot-shallow-probe.yml](../../.github/workflows/urm-snapshot-shallow-probe.yml).

O jogo descartável usa Ren'Py 7.4.11 e as fontes originais URM. O roteiro cria, pela API original `Snapshots.create("shallow-probe")`, um snapshot com:

- escalar `urm_snapshot_probe_scalar = 10`;
- lista `urm_snapshot_probe_list = [1, 2]`;
- dicionário `urm_snapshot_probe_dict = {"a": 1}`.

Depois altera diretamente o store Ren'Py: escalar para 20, item da lista para 9 e valor da chave `a` para 9. Lê os valores reais e chama `Snapshots.findChanges("shallow-probe")`; as asserções verificam o conjunto retornado.

## Resultado observado

O run inicial concluiu **SUCCESS** e registrou:

~~~text
URM_SNAPSHOT_PROBE_AFTER_MUTATION 20 [9, 2] {'a': 9}
URM_SNAPSHOT_PROBE_VALUES 20 [9, 2] {'a': 9}
URM_SNAPSHOT_PROBE_CHANGED_NAMES ['urm_snapshot_probe_scalar']
~~~

Assim, o estado atual tinha as três mutações, mas `findChanges` retornou somente o nome do escalar substituído. A alteração da lista e do dicionário foi in-place e não apareceu como mudança de variável no diff.

### Ampliação runtime: substituição de containers e igualdade

A fixture ampliada [urm_snapshot_shallow_probe.rpy](../tools/fixtures/urm_snapshot_shallow_probe.rpy) executou três fases com checagens explícitas (erro se o conjunto esperado divergir). No run [40676323550](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/40676323550), os logs registraram:

~~~text
URM_SNAPSHOT_PROBE_CHANGED_NAMES ['urm_snapshot_probe_scalar']
URM_SNAPSHOT_PROBE_REPLACED_NAMES ['urm_snapshot_probe_dict', 'urm_snapshot_probe_list', 'urm_snapshot_probe_scalar']
URM_SNAPSHOT_PROBE_EQUAL_CONTENT_NAMES []
~~~

Depois da fase in-place, a fixture substituiu a lista e o dicionário por containers com conteúdo diferente; ambos foram incluídos no diff. Em seguida criou um segundo snapshot e substituiu lista/dicionário por novas instâncias com conteúdo igual; nenhum dos dois apareceu como alterado. O escalar continuou no conjunto no primeiro snapshot porque seguia diferente do valor de captura.

O resultado é coerente com comparação de igualdade no nível superior, não identidade do container: uma nova instância com conteúdo diferente aparece, uma nova instância igual não aparece. Como o primeiro snapshot reteve referências, a mutação interna alterou também o conteúdo visto pelo snapshot antigo; ele já não representa os valores originais `[1, 2]`/`{'a': 1}` para esses containers.

### Ampliação runtime: valor antigo versus atual no editor

A mesma fixture criou um escalar com valor 10, capturou o snapshot, alterou o store atual para 20 e obteve a entrada correspondente por `Snapshots.findChanges()`. O run [40676920686](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/40676920686) registrou:

~~~text
URM_SNAPSHOT_PROBE_EDIT_VARS False True 10 20
URM_SNAPSHOT_PROBE_EDIT_RESULTS False 20 True 30 10
~~~

A ordem é: `old.isEditable`, `new.isEditable`, valores antigo/atual; depois, resultado da tentativa de editar o antigo, valor atual após essa tentativa, resultado da edição do atual, valor atual depois e leitura antiga final. Portanto o objeto antigo apontou ao dicionário do snapshot (valor 10) e recusou `setValue`; o objeto novo resolveu pelo store atual (20), aceitou 30 e não alterou o valor 10 retido no snapshot.

A ligação visual estática na fonte original confirma que os dois botões da comparação chamam `URM_modify_value` com `var['old']` e `var['new']`. O modal inicializa o campo a partir de `var.value`, usa `var.isEditable` para permitir ou bloquear edição e encaminha a ação a `SetVarValue`. Assim, o lado antigo é apresentado como “View variable” e o atual como “Modify variable”. A fixture executou a API original `Var` e a semântica de edição; não automatizou a interação visual/click do modal.

### Ampliação runtime: variáveis adicionadas e removidas

O run [40677490829](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/40677490829) testou dois casos adicionais:

~~~text
URM_SNAPSHOT_PROBE_DELETED_VAR 41 None False True unknown False False
URM_SNAPSHOT_PROBE_ADDED_VAR None 7 False True unknown False True 8 None
~~~

- **Removida após o snapshot:** o objeto antigo lê 41 e é somente leitura. O objeto novo lê `None`, é marcado editável por não ter `storeDict` explícito, mas seu tipo é `unknown`; `setValue("42")` retorna False e a variável continua ausente. Na screen, a fonte mostra que “Change” só aparece para string, boolean, int ou float; o caso `unknown` não oferece esse botão. O teste não clicou no botão “Delete” disponível nem mediu sua interação visual.
- **Adicionada após o snapshot:** o objeto antigo lê `None`, é somente leitura e tipo `unknown`. O objeto novo lê 7 e é editável; `setValue("8")` retorna True, muda o store atual para 8 e o antigo segue lendo `None`.

Isso delimita a comparação: diferenças de presença são listadas, mas o lado ausente é uma projeção `Var` com valor `None`, não uma operação de criação/exclusão automática. A edição do estado atual só funciona quando a variável existe e tem tipo suportado.

## Conclusões e classificação

- **OBSERVADO EM RUNTIME:** `Snapshots.findChanges()` detectou a substituição escalar 10→20.
- **OBSERVADO EM RUNTIME:** o diff não incluiu a lista nem o dicionário após mutações internas, apesar de os valores atuais serem `[9, 2]` e `{'a': 9}`.
- **OBSERVADO EM RUNTIME:** substituir containers por novos conteúdos diferentes foi detectado; substituir por novos containers de conteúdo igual não foi detectado.
- **CONFIRMADO NO SDK 7.4.11:** `renpy.python.DictItems` em `renpy/pydict.pyx` guarda referências aos objetos valor, sem copiá-los profundamente.
- **CORROBORADO POR FONTE E RUNTIME:** o mecanismo de snapshots do URM conserva referências superficiais e compara os valores do nível superior por igualdade; não é uma captura histórica profunda de objetos mutáveis.
- **OBSERVADO EM RUNTIME:** `Var.setValue` no objeto antigo associado ao snapshot recusou edição; o objeto novo associado ao store ativo alterou o estado atual e preservou o valor antigo do snapshot.
- **OBSERVADO EM RUNTIME:** variáveis adicionadas/removidas aparecem com os lados ausentes como `None`; o objeto atual de uma variável removida não a recria via `setValue`, enquanto o lado atual de uma variável adicionada pode ser editado.
- **NÃO TESTADO:** igualdade de containers complexos/customizados; mutações concorrentes ou efeitos colaterais em `__eq__`; integração com os menus originais de snapshots. A persistência nativa da instância foi testada depois no doc 53.

## Execução inválida anterior

O primeiro run [40658264351](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/40658264351) terminou SUCCESS, mas seu roteiro não alterou os três valores (permaneceram 10, `[1, 2]` e `{'a': 1}`), deixando o diff vazio. Ele não serve como evidência sobre a semântica do snapshot. A fixture foi corrigida para mutar explicitamente o store e confirmar os valores após as alterações; o resultado válido está no run 40658456177.

## Limites e continuidade

A prova é para escalares, listas e dicionários simples num jogo Ren'Py 7.4.11. Ela não generaliza para quaisquer objetos, classes, coleções substituídas ou estruturas de outros SDKs. Os snapshots são distintos do rollback nativo e, conforme a análise estática do documento 50, vivem numa estrutura em memória que não é um store `.urm`. A persistência nativa da própria instância Snapshots foi examinada depois no doc 53.
