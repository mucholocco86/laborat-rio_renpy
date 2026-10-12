
if renpy.variant("pc"):
    define config.hw_video = True
else:
    define config.hw_video = False

# Load images
#init python:
    #def load_images(path_start, extension=['.jpg', '.png'], filename_only=False):
        #for file in renpy.list_files():
            #if file.startswith(path_start):
                #for extension in extensions:
                    #if file.endswith(extension):
                        #if filename_only:
                            #name = file.replace(path_start, '').split('/')[-1].replace(extension,'')
                        #else:
                            #name = file.replace(path_start, '').replace('/', ' ').replace(extension,'')
                        #renpy.image(name, Image(file))

    #load_images('common/images/scenes/scene1/')
    #load_images('chapters/', filename_only=True)
    #load_images('gui/')

label splashscreen:

    show buuplays_logo with fade
    $ renpy.pause(4, hard=True)
    scene black with Dissolve (2.0)
    show bg warningscreen with Dissolve (3.0)
    with Pause(2)
    $ renpy.pause(1, hard=True)
    show warning_1 with dissolve
    with Pause(2)
    $ renpy.pause(1, hard=True)
    scene black with Dissolve (2.0)


    return

label start:
    jump ch1sc1

#screens / Imagebutton
#screen disc_button:
    #imagebutton:
        #xanchor 0.5
        #yanchor 0.5
        #xpos 0.5
        #ypos 0.28
        #idle "disc_button.png"
        #hover "disc_hover.png"
        #action OpenURL("https://www.patreon.com/user?u=75994765")


    #return end of version
label endofversion:
    window hide dissolve
    scene black with dissolve
    $ renpy.pause(1)
    show bg endreleasescreen with dissolve
    $ renpy.pause()
    window show dissolve
    dev "{color=#00ff00}End of Current version.{/color}"
    dev "{color=#ff8cdd}Thank you for playing, I hope you enjoyed the story so far!{/color}"
    dev "{color=#ff8cdd}Please consider supporting me on{/color} {color=#00ff00}Patreon/BuuPlays{/color} or {color=#00ff00}Subscribestar/BuuPlays{/color}"
    dev "{color=#00ff00}Supporting gives you 1-30 days early-access to updates as well as various other content and polls to help shape Nephilim.{/color}"
    dev "{color=#ff8cdd}You can also support the development by leaving a review on the site where you found Nephilim, it really helps!{/color}"
    scene eliza_bye with dissolve
    el "{color=#ff8cdd}Thank you for all the support! Patreons, Reviews, Ratings, Recommendations.{/color}"
    el "{color=#ff8cdd}ALL of it has helped grow Nephilim to where we are today!{/color}"
    el "{color=#ff8cdd}I'll see you guys next update to continue our story together! Byyyeeee!{/color}"
    scene thank_pnk with dissolve
    pnk "Special thanks to our Beta-Testers and all of our loyal Patreons!"
    pnk "Keeping consistent updates wouldn't be possible without all of you!"
    $ renpy.pause(2, hard=True)
    scene black with dissolve
    return
