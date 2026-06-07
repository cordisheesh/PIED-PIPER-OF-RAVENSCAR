# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Magnus F. Remond")

define r = Character("Robert Smitt")

default preferences.text_cps = 45
default preferences.afm_enable = False


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    m "The East Yorkshire coast..."
    play music "soft wind.mp3"
    play music "ocean waves.mp3"
    m "Not as bad as I thought it would be honestly."
    r "Aye... The sea be loud."
    m "I guess you're too used to the streets of York my friend!"
    r "That be so. What's the plan?"
    m "Go in, ask questions."
    r "I'm sure the accents here will be terrifying."
    m "Aye, that be so Smitt."
    m "Do you have your pistol and sabre?"
    r "Yes Sir."
    m "Splendid, we can not be too careful."



    # This ends the game.

    return
