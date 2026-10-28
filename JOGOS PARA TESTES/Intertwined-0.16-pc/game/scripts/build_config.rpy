define build.name = "Intertwined"

init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    # build.archive("core_assets", "all")
    # build.archive("logic_data", "all")
    # build.archive("media_music", "all")

    # for _ep in range(1, 16):
    #     _media_name = "media_ep%02d" % _ep
    #     build.archive(_media_name, "all")
    #     build.classify("game/images/Episode %d/**" % _ep, _media_name)

    # build.classify("game/Music/**", "media_music")

    # build.classify("**.rpy", None)
    # build.classify("**.rpyc", "logic_data")

    # build.classify("game/**", "core_assets")