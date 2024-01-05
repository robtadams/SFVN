# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define PC = Character("[povname]" , who_color = "C0C0C0")
define F = Character("Fox")
define W = Character("Wolf")
define L = Character("Falco")
define P = Character("Peppy")
define S = Character("Slippy")
define K = Character("Krystal")
define Pa = Character("Panther")
define Da = Character("Dash")
define Bi = Character("Bill")
define Fa = Character("Faye")
define Mi = Character("Miyu")
define Fr = Character("Alicia")



# The game starts here.

label start:

    python:
        povname= renpy.input("What is your first name?")
        povname= povname.strip()
        if not povname:
            povname = "Zeke"

    "The world seems to shudder as the shuttle starts its landing protocols, turbulence buffeting the hull as the rattling sound echoed across the aisles of mostly empty seats." 
    "I look out of the window seeing the lush green orb of Fortuna hovering so peacefully in space as it looms ever closer and closer."
    "Captain" "Attention passengers, we are initiating landing, please secure your belt harnesses for reentry into Fortuna Grand Station. We hope you have enjoyed your time on Space Dynamics Tour Shuttle."
    "I sigh as the few remaining passengers that didn't depart back on Katina followed instructions, nothing but old folks or a couple of families with their kids going sightseeing."
    "A mother shushes a fussing toddler, wrapping a blanket around the little raccoon and pulling him close to her chest murmuring soothing words."
    "The landing is easy enough, though I can't deny that it's not intimidating a little to suddenly be surrounded by blue sky and towering forests mixed with the glittering reflection of Solar in the windows of the various hotels and shopping districts that made Fortuna a popular tourist spot."
    "I, however, was here on different business."
    PC "Yeah I've landed at FGS, now I just gotta figure out how to find my way to where the retreat is happening."
    "I sighed at the communicator, the floating head of my best friend [Fr] squinted at me across the connection hologram."
    Fr "You mean to tell me that you have a flyer, and some spare credits but don't have a way to get to the meeting spot? You really are hopeless no wonder you need this retreat course thing to help you get your shit together."
    PC "Thanks, your friendship means a lot to me."
    "Our conversations always went this way, her sarcasm is the forge that honed my wit and I wouldn't have it any other way. She suggested I go to this to try to network with other mercenary teams and learn some things to start my new career and now she's needling me for not being over-prepared for the thing she shoved on me last minute. Classic."
    PC "I'll remember that when I make it rich and famous and accept an award from Lylat's Hero."
    "Her beak gaped at me slightly, gawking as her brown eyes squinted harder, narrowing into a glower."
    Fr "I guess I'll just have to try to die before that so you just martyr me. You can't win this game, [PC]"
    "Her expression was deathly serious for all of three seconds before we both burst out laughing. I get a few strange looks from the last of the old folks tottering out of the visitor center in the station but I don't pay them any mind."
    PC "I suppose I should just rent a vehicle to make it out to the site. or I guess they'll call it the LZ or something, yeah?"
    "The cab hummed slightly as the magrail underneath drove it out to a predetermined drop off depot I had found that was close to where the flyers said the expo was going to happen. As I lean against the glass the warmth of Fortuna started to get to me."
    "Coming from Fichina my flight suit was not meant for the permanent tropical conditions of the jungle planet. Despite the constant warm conditions the trees chose to drop their leaves around this time of year, leaving the roadway shrouded in drifts of gold and green and red."
    "It doesn't take long for second thoughts to start working their havoc in my head, wondering why I decided to live the life of a merc, or why I spent most of my savings to come to this Expo."
    menu merc_reason:
        "Why did I become a mercenary?"
        "Money":
            "The money, of course. At least, the promise of it. It wasn't as promising right now though, not when Star Fox and Star Wolf dominated the scene."
            $ money = True
            #block of code to run
        "Fame":
            "Fame always had it's appeal. Fans, sponsorships, TV time, the whole nine. Star Fox and Star Wolf make it hard when they're always in the news though."
            $ fame = True
            #block of code to run
        "Revenge":
            "There's someone that needs to pay for what they did...but the only way I can get closure is to get as good as Star Fox and Star Wolf are." 
            $ revenge = True

label after_reason:
    "I'm broken out of my thoughts by a flicker of something in the edge of the woods as the cab sped by. If it didn't stand out so starkly I wouldn't have even noticed it in the shadow of the canopy."
    "Given the speed the cab was moving I only caught a glimpse of a blob of bone white at the tree line. I guess people probably came out here and wandered the forests for amusement..."
    "I had heard the in-flight warning about Fortuna's less docile fauna when we were departing, and the brochures had mentioned a few notable critters to keep an eye out for on the edges of the forest but I don't remember any of them being so pale."
    "Cab" "Your destination is coming soon."
    "The autonav chime made me jump, as much as I hate to admit it. The destination in question loomed a little further out but I could see the edge of the fencing and the steam rising from the expo building's roof vents."
        


# This ends the game.

    return
