# Loader x52MF2 — comportamento confirmado

`framework/bootstrap.rpy` declara módulos e implementa o carregamento. `.x52rpy` e `.x52` são carregados explicitamente. Quando um `.x52rpy` não está disponível como fonte carregável, o loader pode mapear o nome lógico para o `.rpyc` correspondente, por exemplo `modules/01utils.x52rpy` -> `modules/01utils.rpyc`.

O `load()` procura `bootstrap.rpyc`, registra `archivePath` e trata um `.update` pendente. `API.rpy` baixa atualizações para `.tmp`, extrai o primeiro `.rpa` para `.update`, e `applyUpdate` substitui o archive e chama `renpy.reload_script()`.

Questões abertas: trigger da aplicação, estado seguro, UI e reconciliação entre reload, contexto, AST e estado.


# Loader x52MF2

Documentos deste eixo:

- `01_LOADER_X52MF2_CARGA_E_DEPENDENCIAS.md` — catálogo de módulos, expansão de dependências, seleção de `.x52t`, substituição de placeholders, `renpy.load_string()`, fallback `.rpyc` e ciclo de atualização.

Fonte principal: `../01_MATERIAL_URM/1_URM_ORIGINAL/framework/bootstrap.rpy`. A versão convertida foi conferida e tem o mesmo SHA GitHub.

Próximas questões:
1. encontrar o produtor de `.x52t` / `.x52rpyt`, se existir no material disponível;
2. correlacionar a expansão de `availableModules` com a lista de arquivos efetivamente carregados;
3. localizar quem chama `pendingUpdate` e em que estado de jogo;
4. investigar o ajuste de `renpy.game.script.digest` quando o archive não é localizado.

A existência de um loader URM não significa que seus sufixos sejam recursos nativos do Ren'Py. Um futuro loader WF deve ter especificação e testes próprios.
