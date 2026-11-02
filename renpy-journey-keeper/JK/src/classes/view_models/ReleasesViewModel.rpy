init python in JK:
    _constant = True

    class ReleasesViewModel(x52NonPicklable):
        url = "https://api.github.com/repos/{}/{}/releases".format(MOD_GITHUB_OWNER, MOD_GITHUB_REPO)
        
        def __init__(self):
            self.loading = False
            self.error = None
            self.releases = []
        
        def fetch_all_releases(self):
            self.loading = True
            self.error = None
            renpy.restart_interaction()
            
            print("Buscando versões em: ", self.url)
            
            try:
                request = _urllib_request.Request(self.url)
                request.add_header("Accept", "application/vnd.github.v3+json")
                
                response = _urllib_request.urlopen(request)
                json_string = response.read()
                data = json.loads(json_string)
                
                for release_data in data:
                    self.releases.append(Updater.Release(release_data))
            
            
            except _urllib_error.HTTPError as e:
                print("Ocorreu um erro HTTP ao baixar as versões: ", e)
                self.error = "Ocorreu um erro HTTP ao baixar as versões: {color=[JK.Colors.error]}" + Utils.escape_renpy_reserved_characters(str(e)) + "{/color}"
            
            
            except _urllib_error.URLError as e:
                print("Ocorreu um erro de URL ao baixar as versões: ", e)
                self.error = "Ocorreu um erro de URL ao baixar as versões: {color=[JK.Colors.error]}" + Utils.escape_renpy_reserved_characters(str(e)) + "{/color}"
            
            
            except Exception as e:
                print("Ocorreu um erro ao baixar as versões: ", e)
                self.error = "Ocorreu um erro inesperado ao baixar as versões: {color=[JK.Colors.error]}" + Utils.escape_renpy_reserved_characters(str(e)) + "{/color}"
            
            finally:
                self.loading = False
                renpy.restart_interaction()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
