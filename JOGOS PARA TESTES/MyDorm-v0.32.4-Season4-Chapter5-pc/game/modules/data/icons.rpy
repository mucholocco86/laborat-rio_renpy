init -9999 python:
# Icons
    icons = {
        # Main Menu
        "New Game" : "new-board-icon.png",
        "History" : "chat-list-icon.png",
        "Game Save" : "download-install-line-icon.png",
        "Game Load" : "upload-outbox-line-icon.png",
        "Game Import" : "login-icon.png",
        "Settings" : "engine-gears-icon.png",
        "Gallery" : "photos-icon.png",
        "About" : "about-me-icon.png",
        "Help" : "manual-icon.png",
        # Game Menu
        "Quit" : "exit-door-icon.png",
        "Main Menu" : "homepage-icon.png",
        # Setting Menu
        "General" : "maintenance-icon.png",
        "Menu" : "three-horizontal-lines-icon.png",
        "Dialogue" : "comments-icon.png",
        "Choices" : "choose-icon.png",
        "Languages" : "language-icon.png",
        # Help Menu
        "Keyboard" : "computer-keyboard-wireless-icon.png",
        "Mouse" : "computer-mouse-icon.png",
        "Gamepad" : "video-game-gamepad-outline-icon.png",
        # Happy Family Patch
        "Family" : "family-icon.png",
        # Quick Menu
        "Hide" : "hide-private-hidden-icon.png",
        "Unhide" : "see-icon.png",
        "Back" : "step-backward-icon.png",
        "Fwd" : "step-forward-icon.png",
        "Q.Load" : "uptime-arrow-icon.png",
        "Q.Save" : "downtime-arrow-icon.png",
        "A.Fwd" : "play-icon.png",
        "Skip" : "fast-forward-icon.png",
        "Left" : "left-angle-arrow-bold-icon.png",
        "Right" : "right-angle-arrow-bold-icon.png",
        "Profiles" : "contacts-icon.png",
        "Discord" : "images/IB/discord_button_idle.png",
        "Subscribestar" : "images/IB/ss_Idle.png",
        "Patreon" : "images/IB/patreon_button_Idle.png",
        "Steam" : "images/IB/steam.png",
        "SteamS1" : "images/IB/steams1.png",
        "SteamS2" : "images/IB/steams2.png",
        "SteamS3" : "images/IB/steams3.png",
        # Profiles
        "NotAvailable" : "close-round-line-icon.png",
        "Bride" : "bride-icon.png",
        "Harem" : "women-group-icon.png",
        "Heart" : "heart-icon.png",
        "Bride" : "ring-icon.jpg",
        "RP" : "heart-thin-icon.png",
        "Broken Heart" : "broken-heart-icon.png",
        "Pregnant" : "pregnant-maternity-icon.png",
        "Maledom" : "heart-icon-maledom.png",
        "Femdom" : "heart-icon-femdom.png",
    }
    for iconKey, iconValue in icons.items ():
        if iconValue.find ("/") == -1:
            icons.update ({ iconKey : "modules/Images/Icons/" + iconValue })
