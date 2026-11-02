init python in JK:
    _constant = True
    _urllib_request = None
    _urllib_error = None

    import json
    import re
    import os
    import shutil

    class UpdaterClass(x52NonPicklable):
        asset_name = "JK.rpa"
        temp_asset_name = asset_name + ".temp"
        
        mod_path = os.path.join(renpy.config.gamedir, asset_name)
        download_path = os.path.join(renpy.config.gamedir, temp_asset_name)
        
        url = "https://api.github.com/repos/{}/{}/releases/latest".format(MOD_GITHUB_OWNER, MOD_GITHUB_REPO)
        
        unavailable = False
        
        def __init__(self):
            self.pending_update = None
            self.loading = False
            self.asset_url = None
            self.checked_for_update = False
            self.downloading = False
            self.installing = False
            self.installed = False
            self.error = None
            self.latest = None
            self.rpa_locked_exception = False
            self.pending_utter_restart = False
            self.reload_and_update = False
            
            if os.path.exists(self.download_path):
                if renpy.store.persistent.JK_TriedUtterRestart:
                    print("O arquivo temporário de atualização \"{}\" continua presente após a tentativa de recarregar. Isso não deveria acontecer. Outro programa pode estar usando o arquivo ou pode haver uma falha no sistema de atualização.".format(self.download_path))
                else:
                    print("Arquivo temporário de atualização encontrado: \"{}\". Tentando atualizar...".format(self.download_path))
                    self.install_update()
                    self.pending_utter_restart = True
        
        def check_for_update(self, ignore_blacklist=False, ignore_force_auto_update=False):
            if self.loading or self.unavailable:
                return
            
            self.checked_for_update = True
            
            self.pending_update = None
            self.latest = None
            self.error = None
            renpy.restart_interaction()
            
            self.latest = self.fetch_latest_release()
            if self.latest:
                version = self.latest.version
                if version != MOD_VERSION and (ignore_blacklist or renpy.store.persistent.JK_IgnoredUpdate != version):
                    self.pending_update = self.latest
                    
                    if self.pending_update.asset:
                        if Settings.autoUpdateWithoutPrompt and not ignore_force_auto_update:
                            Updater.InstallUpdateAction(self.latest)()
                        elif not Settings.noUpdatePrompt and renpy.get_screen("JK_Settings_Updater") is None:
                            renpy.show_screen("JK_PendingUpdate", self.latest)
        
        
        def fetch_latest_release(self):
            self.loading = True
            self.error = None
            renpy.restart_interaction()
            
            print("Buscando metadados em: ", self.url)
            
            try:
                request = _urllib_request.Request(self.url)
                request.add_header("Accept", "application/vnd.github.v3+json")
                
                response = _urllib_request.urlopen(request)
                json_string = response.read()
                return Updater.Release(json.loads(json_string))
            
            
            except _urllib_error.HTTPError as e:
                print("Ocorreu um erro HTTP ao baixar os metadados da atualização: ", e)
                self.error = "Ocorreu um erro HTTP ao baixar as informações da atualização: {color=[JK.Colors.error]}" + Utils.escape_renpy_reserved_characters(str(e)) + "{/color}"
            
            
            except _urllib_error.URLError as e:
                print("Ocorreu um erro de URL ao baixar os metadados da atualização: ", e)
                self.error = "Ocorreu um erro de URL ao baixar as informações da atualização: {color=[JK.Colors.error]}" + Utils.escape_renpy_reserved_characters(str(e)) + "{/color}"
            
            
            except Exception as e:
                print("Ocorreu um erro ao baixar os metadados da atualização: ", e)
                self.error = "Ocorreu um erro inesperado ao baixar as informações da atualização: {color=[JK.Colors.error]}" + Utils.escape_renpy_reserved_characters(str(e)) + "{/color}"
            
            finally:
                self.loading = False
                renpy.restart_interaction()
            
            return None
        
        def download_and_install_update(self, release=None):
            if self.download_asset(release):
                self.installing = True
                self.installed = False
                renpy.restart_interaction()
                
                self.install_update()
        
        def install_update(self):
            path = self.mod_path
            
            if os.path.islink(self.mod_path):
                
                
                try:
                    path = os.path.realpath(self.mod_path)
                except Exception as e:
                    print("Erro ao resolver o link simbólico: ", e)
            
            try:
                shutil.move(self.download_path, path)
                self.installing = False
                self.installed = True
                renpy.restart_interaction()
                return
            except Exception as e:
                error_message = "{color=[JK.Colors.error]}" + Utils.escape_renpy_reserved_characters(str(e)) + "{/color}"
                
                if e.args[0] == 13:
                    print("Não foi possível substituir o arquivo .rpa. O Ren’Py ou outro programa está usando o arquivo.")
                    renpy.store.persistent.JK_TriedUtterRestart = False
                    self.rpa_locked_exception = True
                    self.error = "Não foi possível substituir o arquivo .rpa. O Ren’Py ou outro programa está usando o arquivo: {}".format(error_message)
                else:
                    print("Erro ao mover o arquivo: ", e)
                    self.error = "Ocorreu um erro inesperado: {}".format(error_message)
            
            self.installing = False
            renpy.restart_interaction()
            
            renpy.notify("Journey Keeper atualizado com sucesso para a versão " + MOD_VERSION)
        
        def download_asset(self, release):
            release = release or self.latest
            
            self.downloading = True
            self.error = None
            
            if os.path.exists(self.download_path):
                os.unlink(self.download_path)
            
            print("Baixando arquivo de: ", release.download_url)
            try:
                request = _urllib_request.Request(release.download_url)
                request.add_header("Accept", "application/octet-stream")
                
                response = _urllib_request.urlopen(request)
                
                with open(self.download_path, "wb") as output_file:
                    output_file.write(response.read())
                
                print("Arquivo baixado para: ", self.download_path)
                
                return True
            
            
            except _urllib_error.HTTPError as e:
                print("Ocorreu um erro HTTP ao baixar ou gravar o arquivo: ", e)
                self.error = "Ocorreu um erro HTTP ao baixar ou gravar o arquivo: {color=[JK.Colors.error]}" + Utils.escape_renpy_reserved_characters(str(e)) + "{/color}"
            
            
            except _urllib_error.URLError as e:
                print("Ocorreu um erro de URL ao baixar ou gravar o arquivo: ", e)
                self.error = "Ocorreu um erro de URL ao baixar ou gravar o arquivo: {color=[JK.Colors.error]}" + Utils.escape_renpy_reserved_characters(str(e)) + "{/color}"
            
            
            except Exception as e:
                print("Ocorreu um erro ao baixar ou gravar o arquivo: ", e)
                self.error = "Ocorreu um erro inesperado ao baixar ou gravar o arquivo: {color=[JK.Colors.error]}" + Utils.escape_renpy_reserved_characters(str(e)) + "{/color}"
            
            finally:
                self.downloading = False
                renpy.restart_interaction()
            
            return False
        
        class Release(x52NonPicklable):
            assets_url = "https://api.github.com/repos/{}/{}/releases/assets/".format(MOD_GITHUB_OWNER, MOD_GITHUB_REPO)
            
            def __init__(self, data):
                self.data = data
                
                
                self._download_url = None
                self._changelog = None
                self._asset = None
            
            @property
            def version(self):
                return self.data.get("tag_name").replace("v", "")
            
            @property
            def download_url(self):
                if self._download_url:
                    return self._download_url
                
                asset = self._find_asset()
                if not asset:
                    return None
                
                self._download_url = self.assets_url + str(self.asset.get("id"))
                
                return self._download_url
            
            @property
            def url(self):
                return self.data.get("html_url")
            
            @property
            def changelog(self):
                if self._changelog:
                    return self._changelog
                
                self._changelog = Utils.translate_markdown(self.data.get("body"))
                
                return self._changelog
            
            @property
            def asset(self):
                if self._asset:
                    return self._asset
                
                self._asset = self._find_asset()
                
                return self._asset
            
            def _find_asset(self):
                assets = self.data.get("assets")
                if assets and len(assets) > 0 and assets[0]:
                    return assets[0]
        
        class SkipUpdateAction(renpy.ui.Action):
            def __init__(self, version):
                self.version = version
            
            def __call__(self):
                renpy.store.persistent.JK_IgnoredUpdate = self.version
                
                renpy.restart_interaction()
        
        class InstallLatestUpdateAction(renpy.ui.Action):
            def __call__(self):
                Updater.InstallLatestUpdateAction(Updater.latest)()
        
        class InstallUpdateAction(renpy.ui.Action):
            def __init__(self, release=None):
                self.release = release
            
            def __call__(self):
                if renpy.get_screen("JK_PendingUpdate") is None:
                    renpy.show_screen("JK_PendingUpdate", release=self.release)
                
                renpy.invoke_in_thread(Updater.download_and_install_update, release=self.release)
                renpy.restart_interaction()
        
        class DisableUpdatesAction(renpy.ui.Action):
            def __call__(self):
                showConfirm(
                    title="Desativar atualizações",
                    message="Deseja mesmo desativar a verificação automática de atualizações?\n{color=[JK.Colors.info]}Você pode reativá-la nas configurações quando quiser.{/color}",
                    yes=Settings.ToggleEnabledAction("updater"),
                    yes_icon="\ue888",
                    yes_color=Colors.error
                )
        
        class CheckForUpdateAction(renpy.ui.Action):
            def __call__(self):
                Updater.check_for_update(ignore_blacklist=True, ignore_force_auto_update=True)
        
        class RestartGameAction(renpy.ui.Action):
            def __call__(self):
                if renpy.get_screen("JK_PendingUpdate") is None:
                    renpy.show_screen("JK_PendingUpdate", release=Updater.pending_update)
                
                Updater.reload_and_update = True
                renpy.restart_interaction()

    try:
        import urllib2 as _urllib_request
        import urllib2 as _urllib_error
    except:
        try:
            import ssl
            ssl._create_default_https_context = ssl._create_unverified_context
            
            from urllib import request as _urllib_request
            from urllib import error as _urllib_error
        except Exception as e:
            UpdaterClass.unavailable = True
            print("urllib não está disponível. O atualizador foi desativado.")
            pass
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
