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
    
    play music "ocean waves.mp3"
    scene introp
    hide window
    pause
    
    m "The East Yorkshire coast..."
    
    m "Not as bad as I thought it would be honestly."

    scene intro2
    m "Sweet fresh air."
    r "Aye... The sea be loud."
    m "I guess you're too used to the streets of York my friend!"
    r "That be so. What's the plan?"
    m "Go in, ask questions."
    r "I'm sure the accents here will be terrifying."
    m "Aye, that be so Smitt."
    m "But I've heard Ravenscar is a nice place."
    stop music
    scene fields
    show smitt 
    with fade
    play music "soft wind.mp3"
    m "Do you have your pistol and sabre?"
    r "Yes Sir."
    m "Splendid, we can not be too careful."
    m "You look prim and proper with your red coat."
    r "Uniform, sir."

    menu:
        "Are you ready to go?":
            m "Are you ready to head in?"
            r "Aye, let's head to."
            jump after_menu

        "Any questions?":
            m "Do you have any quick questions, Smitt?"
            hide smitt 
            show smittnervous 
            r "Aye, I do Mr. Magnus Remond sir..."
            m "Well? What do they be?"
            r "I know I am your guard. Your military escort."
            r "But I be a bit nervous..."
            m "That's okay Smitty."
            m "I've been nervous on cases before too."
            r "How are you so composed?"
            r "How do you do it?"
            r "You seem so relaxed!"
            hide smittnervous 
            show smitt 
            r "Content even?"
            m "I love the shore, me lad."
            m "Is that all?"
            r "Aye sir."
            m "We have a ripper to catch!"
            jump after_menu
    
    label after_menu:
    


    



    # This ends the game.

    return
