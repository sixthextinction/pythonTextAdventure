import sys
#from sys import exit

#boolean shakenDebuff?
#level up mechanics? increase to dex, strength, etc?

#dictionary to store info on amount of treasure a designated treasure room contains
roomHasTreasure =   {
                        "entranceCorridor" : 25,
                        "corridor4" : 70,
                        "corridor6" : 50,
                        "treasureRoom" : 200
                    }
roomHasMonsters =   {
                        "trapRoom"      :   "skeletons",
                        "corridor5"     :   "zombie",
                        "treasureRoom"  :   "guardianBoss"
                    }
#rooms which need percept checks

#associative array to hold object/room descriptions : 
#rooms first
objectDescription = {
                        "startRoom" :       """
                                            Smooth, slippery stone. Superior, if spartan.
                                            Dust and cobwebs populate this room. 
                                            This place is ancient. No one has either ventured down here for years, or escaped to tell the tale.
                                            There is no sound. Each footstep is a crack of thunder in this barren place.
                                            Each clink of your armor a beacon for the denizens that dwell here.

                                            There's a suspiciously pristine door to the right of you, the east, 
                                            While a rusty, dilapidated metal gate covers another entrance on the other side of the room to the northwest.
                                            """,
                        "entranceCorridor" : """
                                            Your first inroads into the Dungeon have yielded this corridor. The coast is clear.
                                            The architecture here echoes that of the first room, and you suspect this is how it is the rest of the way, too.

                                            An arch provides an exit to the south.  
                                            """,
                        "corridor1" :       """
                                            This is a long, long corridor. A solitary sconce with an orb of light provides illumination about halfway down.
                                            Curiously, the architecture here is slightly different. The floor here is comprised of many single, large, rectangular slabs instead of smooth stone.

                                            You can barely make out an exit to the west in the tired, jaundiced glow. The corridor continues.
                                            """,
                        "corridor2" :       """
                                            The unbroken, smooth stone floor is back, and you sigh in relief. You peer around carefully, but there are no enemies in sight.
                                            This seems an exceptionally ordinary room. The wall to your left has a brick outcropping, but that's to be expected in some place as old as this, right? 

                                            There seems to be nothing here but another sconce lighting the way round a corner; another corridor to the northwest.
                                            """,
                        "corridor3" :       """
                                            Another long, boring corridor. 

                                            You see a rusty, foreboding metal gate to the southeast. 

                                            There's a dusty old scroll lying about in an alcove here.
                                            """,
                        "corridor4" :       """
                                            Yet another corridor. You're finally begin to appreciate the architectural genius of this place. You're now certain of how easy it is to get lost here, roaming forever.
                                            Good thing you have a map. You do have a map, right?
                                            Your thoughts are interruted by guttural, inhuman moaning echoing down the stone halls. Flickering shadows on the walls ahead. Bad news.

                                            Whatever it is, it lies to the east. 
                                            """,
                        #this room needs an alternate description post-zombie killing.
                        "corridor5" :       """
                                            The shambling corpse walks towards you.

                                            There's a low ceilinged hallway to the south. 
                                            """,
                        "corridor6" :       """
                                            You can't believe your eyes. Daylight to the west. Filtering in through the widest gate you've seen here so far.
                                            These halls are wider than any other in this place. You check around for danger, but there seems to be none apparent.
                                            Home stretch.

                                            Your ticket out of here is to the west, though your attention is drawn to another diagonal tunnel to the northwest. An evil permeates that tunnel. 
                                            """,
                        #this room needs an alternate description post-guardian killing.
                        "treasureRoom" :    """
                                            The Guardian stands here in this bloody room, among bones and discarded gear of heroes past, a dozen arms tall, metal plates intertwining with chains, dirty leather hood hiding his grotesque visage.
                                            He has been waiting for you. He grins, bare, bloody teeth and all, as he picks up his greatsword. 
                                            A key hangs from a hook on the wall behind him.

                                            Are you prepared? There is no exit except back out, southeast, should you want to regroup. 
                                            """,
                        "trapRoom" :        """
                                            Dark. No sconces. No magelight. The darkness here is thick and suffocating. A different animal altogether. It's an oily ooze, pervading in the air.
                                            Clattering of bones and metal.
                                            This was a trap.
                                            You curse, throwing your lantern on the floor and whipping around.
                                            Three skeletons. Undead protectors of some long-forgotten master. Their swords are curved. 

                                            The door behind you is barred, through sorcery or otherwise, you could not care less. No escape that way.
                                            There is an exit to the northeast, if you can make it there.
                                            """,
                        "deadEndRoom" :     """
                                            Dead end. 

                                            Or is it nearly as grim? There's a draft coming from the south. From...solid wall?
                                            """,
                        # "exitRoom"    :     """
                        #                     Daylight! You ascend the small flight of stairs, push aside an ancient, overgrowth-laden gate, and emerge into the overworld, not unscathed, but wiser and more experienced for your troubles.
                        #                     """,
                    
#now objects :
                        "freedom"           :   """
                                            Daylight! You ascend the small flight of stairs, push aside an ancient, overgrowth-laden gate, 
                                            and emerge into the overworld, not unscathed, 
                                            but wiser and more experienced for your troubles.""",#oh, the humour in having freedom portrayed as an object.
                        "guardianScroll"    :   """
                                            This kills the guardian when recited.
                                                """,


                        "suspiciousDoor"    :  """
                                            You peer at the door, and notice nothing different. You start to give it a gentle push...
                                            ...and immediately shrink back.
                                            That was a close one. There's a hair trigger of a wire connecting the edge to some invisible apparatus inside the wall.
                                            You judiciously cut the wire, and jump as there is a tiny, but piercing, clink from above.
                                            Whatever you have done, seems to have defused the trap.
                                            """,
                        "treasureChest"     :   "Just your everyday large wood-and-metal chest. You can unlock this.",
                        "suspiciousTile"    :   "Your perceptive nature pays off. The unnatural tile architecture hides a pressure trap. You disarm it. Close shave.",
                        "brickOutcropping"  :   "You run your hand across the outcropping, and discover one of the bricks is loose! Pulling on it reveals a secret passage to the west!",
                        "deadEndSouthWall"  :   "You push the south wall, and it falls over almost comically. Huh. Being that perceptive paid off, looks like. You can step through into a new corridor to the south.",
                        "corridor3Gate"     :   "Just your regular everyday metal gate. Which is also, unfortunately, of the locked variety. The lock has long since eroded away, to boot. Drat.",
                        "zombie"            :   "Ghastly un-life stares back at you through maggot infested eyesockets. A mass of rotten flesh, loose coils of intestine, and jagged teeth, shambling towards you, inch by fatal inch. ",
                        "exitGate"          :   "Large, barred gates. Comically oversized chains and a lock fasten it securely in place. It's locked, needless to say. You need a key to get out of here.",
                        "guardianBoss"      :   "A towering mound of interlocking black metal plates and the biggest greatsword you've ever seen (har har). You can make out a hint of his black eyes and slathering fangs under that leather hood, pulled down low.",
                        "exitKey"           :   "The key to your freedom hangs there, glittering in the magelight, as it has for the past few hundred years. Is there a way to get to it, dodging the Guardian?",
                        "skeleton"          :   "A reanimated soldier, moldy bones held together by some unholy magic. It carries a curved sword, and the red misty glow in its otherwise empty orbits, hungers for your blood."
                    }

gettableObjectsList = ["exitKey", "guardianScroll"] #for now.

directionsList = [ "north", "northwest", "west", "southwest", "south", "southeast", "east", "northeast" ]

monstersList   =    [ "skeleton", "zombie", "guardian", "boss" ]


#maps subjects in player commands to an internal gameObject name
subjectToGameObjectMap =    { #only covers mappings that can have a 1:1 resolution. "room" can't, as it can have multiple versions depending on roomName. Resolve that elsewhere.
                            "chest"         :   "treasureChest",
                            "treasure"      :   "treasureChest",
                            "tile"          :   "suspiciousTile",
                            "tiles"         :   "suspiciousTile",
                            "zombie"        :   "zombie",#redundant?
                            "guardian"      :   "guardianBoss",
                            "boss"          :   "guardianBoss",
                            "key"           :   "exitKey",
                            "skeleton"      :   "skeleton",#redundant?
                            "scroll"        :   "guardianScroll"
                            }

#maps objects to rooms they're in, 1 to 1 only
subjectToRoomMap =  {
                        "skeleton"  :   "trapRoom",
                        "zombie"    :   "corridor5",
                        "boss"      :   "treasureRoom",
                        "guardian"  :   "treasureRoom",
                        "key"       :   "treasureRoom",
                        "scroll"    :   "corridor3"
                    }

#list of exits out of each room. KEY is the current roomName, VALUE list's last item is the direction to go back to the room you came from (unless there isn't any as in the case of startRoom or trapRoom).
roomExits = {
                "startRoom"         :       ["northwest", "east"],
                "trapRoom"          :       ["northeast"],
                "deadEndRoom"       :       ["northwest"],                 #make south exit visible only after examining wall(perception check)
                "entranceCorridor"  :       ["south", "northwest", "north"],    #northwest is the rigged door; still needs percept check
                "corridor1"         :       ["west", "east"],
                "corridor2"         :       ["northwest", "southeast"],     #west exit only after a percept check; the western exit through wall is hidden
                "corridor3"         :       ["northeast"],                           #no exits out of this one, rusty metal gate barred
                "corridor4"         :       ["east", "north"],                      #north exit is the same secret tunnel that takes players to corridor2
                "corridor5"         :       ["south", "north"],
                "corridor6"         :       ["west", "northwest", "east"],
                "treasureRoom"      :       ["southeast"]
            }

playerHP = 100  #HP, unused now.
playerGP = 0    #Gold, show in final score
playerInventory = [""] #empty at the start, append stuff as things are picked up.
enemyWasKilledHere = [""] #empty at first, append roomNames as enemies are killed in those rooms
disabledThreats = [""]  #move threats (traps/enemies) here as they are removed from game world
discoveredSecrets = [""] #analogous to disabledThreats for non-threatening stuff that needs perception checks (hidden walls, etc.)

bossKilled = False #needed for score screen. Set to true when killed.
prompt = "What do you do? > "
########################################################################################
def goToRoom(origin, direction):
    #Naiive implementation for now. Use the roomExits list later for an improved one, maybe.
    #--------------------------------------------
    if (origin == "startRoom"):
        if(direction == "northwest"):
            return "trapRoom"
        elif(direction == "east"):
            return "entranceCorridor"
        else:
            return "NaD"#not a direction, ala NaN
    #--------------------------------------------
    elif (origin == "trapRoom"):
        if(direction == "northeast"):
            return "deadEndRoom"
        else:
            return "NaD"
    #--------------------------------------------
    elif (origin == "deadEndRoom"):
        if(direction == "south"):
            return "entranceCorridor"
        elif (direction == "northwest"):
            return "trapRoom"
        else:
            return "NaD"
    #--------------------------------------------
    elif (origin == "entranceCorridor"):
        if (direction == "south"):
            return "corridor1"
        elif (direction == "northwest"):
            return "startRoom"
        elif (direction == "north"):
            return "deadEndRoom"
        else:
            return "NaD"
    #--------------------------------------------
    elif (origin == "corridor1"):
        if (direction == "west"):
            return "corridor2"
        elif (direction == "east"):
            return "entranceCorridor"
        else:
            return "NaD"
    #--------------------------------------------
    elif (origin == "corridor2"):
        if (direction == "northwest"):
            return "corridor3"
        elif (direction == "west"):
            return "corridor4"
        elif (direction == "southeast"):
            return "corridor1"
        else:
            return "NaD"
    #--------------------------------------------
    elif (origin == "corridor3"):
        if (direction == "northeast"):
            return "corridor2"
        else:
            return "NaD"
    #--------------------------------------------
    elif (origin == "corridor4"):
        if (direction == "east"):
            return "corridor5"
        elif (direction == "north"):
            return "corridor2"
        else:
            return "NaD"
    #--------------------------------------------
    elif (origin == "corridor5"):
        if (direction == "south"):
            return "corridor6"
        elif direction == "north":
            return "corridor5"
        else:
            return "NaD"
    #--------------------------------------------
    elif (origin == "corridor6"):
        if (direction == "northwest"):
            return "treasureRoom"
        elif (direction == "west"):
            return "exitRoom"
        elif direction == "east":
            return "corridor5"
        else:
            return "NaD"
    #--------------------------------------------
    elif (origin == "treasureRoom"):
        if (direction == "southeast"):
            return "corridor6"
        else:
            return "NaD"
    #--------------------------------------------
    else:
        return "idunnolol"
########################################################################################
def die(why):
    print " %s Well done!" % why
    showFinalScore()
    sys.exit(0) #this and "import sys" are temporary workarounds to "exit takes no arguments". What's the real cause?
########################################################################################
def dangerAlert():
    print "Careful. Something sinister lurks here...\n"
########################################################################################
def getAltDescription(roomName):
    #here's the general case
    # if roomName in roomHasMonsters:
    #     return objectDescription[roomName]
    # else
    #     return "<alt description>"

    # if roomName == "corridor5":
    #     if roomName in roomHasMonsters:                                     #the zombie is alive still
    #         return objectDescription[roomName]                              #the same description
    #     else:                                                               #zombie killed
    #         return "The quite dead dread zombie lies on the floor. There's a low ceilinged hallway to the south. "         #alternate description, zombie removed   

    # elif roomName == "treasureRoom":
    #     if roomName in roomHasMonsters:
    #         return objectDescription[roomName]
    #     else:
    #         return "<alternate description of a boss-less room. Mention the key.>"

    #rooms with enemies
    returnString = ""

    if roomName == "corridor5":
        returnString = "The quite dead zombie lies on the floor. There's a low ceilinged hallway to the south. " 
    elif roomName == "treasureRoom":
        if "exitKey" in playerInventory:
            returnString =  """
                    The Guardian is nowhere to be found, having been smote out of existence by your scroll.
                    The room retains all of its grim glory, of course, but at least it isn't populated by a hulking, living, breathing tower of metal and fury.

                    The exit is to the southeast, as always. Having obtained the key, you can leave this dungeon now, if you wish.
                    """
        else:
            returnString = """
                    The Guardian is nowhere to be found, having been smote out of existence by your scroll.
                    The room retains all of its grim glory, of course, but at least it isn't populated by a hulking, living, breathing tower of metal and fury.
                    The key still hangs on the hook at the far end of the room.

                    The exit is to the southeast, as always. 
                    """
        
    #rooms with percept checks :
    #todo

    else:
        returnString = "<alternate description of %s>" % roomName

    return returnString
########################################################################################
def isMonster(subject):
    if subject in monstersList:
        return True
    else:
        return False
########################################################################################
def translateSubjectToGameObject(subject, roomName):
    #if subject is a game object, and that gameobject is present in current room,
    if subject in subjectToGameObjectMap and subjectToRoomMap[subject] == roomName: #this lack of symmetry bugs me. Why does subjectToRoomMap[] use subject and not a proper gameObject name?
            return subjectToGameObjectMap[subject]
    #for "examine room" Pretty unnecessary right now, as that special case is handled in coreGameLoop 
    elif subject == "room": 
        return objectDescription[roomName]
    else:
        return "NaO" #not an examinable subject. An errorcode, basically, like NaD.
########################################################################################
def coreGameLoop(roomName, includeDescription, treasureObtained):
    treasurePresent = False

    print "You are in : %s" % roomName

    if (includeDescription):
        #if secret was discovered, or enemy was killed here (leaving a corpse), we need alternate descriptions of the room to reflect those objects still being present
        if (roomName in enemyWasKilledHere): #second one'ss a list. Combine these into something like "roomWasModified"?
            #this function always returns the alt description for a given room (passed as argument)
            #but what if this room has a discoverable secret, AND an enemy, or more of each?
            #secrets not yet discovered/enemies not yet killed cannot be shown prematurely to the player
            print getAltDescription(roomName)
        else:
            print objectDescription[roomName]

    if (roomName in roomHasTreasure): 
        treasurePresent = True
        
    if treasurePresent == True:
        print "There's a treasure chest here."

    #list all exits out of this room
    print "Exits out of here : "
    for exit in roomExits[roomName]:
        print "\t"+exit

    playerChoice = raw_input(prompt)

    #--------------------------------------------------------------------------------------------------------------
    #player wants to do something with the treasure chest :
    #if treasure obrtained, remove room from roomHastreasure list
    if ("chest" in playerChoice or "treasure" in playerChoice) and treasurePresent == True:
        #player wants to examine it :
        if "examine" in playerChoice or "look at" in playerChoice:
            print objectDescription["treasureChest"]
            coreGameLoop(roomName, False, False)
        #player wants to open/unlock it :
        elif "unlock" in playerChoice or "open" in playerChoice:
            goldObtained = roomHasTreasure[roomName]
            print "You obtain %d gold!" % goldObtained
            global playerGP
            playerGP += goldObtained
            del(roomHasTreasure[roomName]) #remove room from roomhasTreasure list
            coreGameLoop(roomName, False, True)
        #could not parse player's intent :
        else:
            print "I don't know what you mean to do with the treasure chest."
            coreGameLoop(roomName, False, False)
    #--------------------------------------------------------------------------------------------------------------
    #player wants to examine the room/gates        
    elif playerChoice == "examine room" or playerChoice == "look around" or playerChoice == "look at room":
        coreGameLoop(roomName, True, False)
    elif playerChoice == "examine gate" or playerChoice == "look at gate":
        if roomName == "startRoom":
            print "The rusty, but stable, gate reveals naught but oily, foreboding darkness beyond."
            coreGameLoop(roomName, False, False)
        elif roomName == "corridor3":
            print "As you approach closer, you realize it's no good. The rusted gate is barred shut, after years of disuse."
            print "There's no exit to the southeast after all. This room is a dead end."
            coreGameLoop(roomName, False, False)
        else:
            print "I don't see a gate here."

    #--------------------------------------------------------------------------------------------------------------
    #trap/reveal checks
    elif playerChoice == "examine wall":
        if roomName == "corridor2":
            print objectDescription["brickOutcropping"]
            discoveredSecrets.append("brickOutcropping")
            roomExits[roomName].append("west")
        elif roomName == "deadEndRoom": 
            print objectDescription["deadEndSouthWall"]
            discoveredSecrets.append("deadEndSouthWall")
            roomExits[roomName].append("south")
        else:
            print "Smooth, ancient stone. The uniformity hurts your eyes if you look around long enough. It's all very disorienting, to be honest."
        coreGameLoop(roomName, False, False)

    elif playerChoice == "examine door" or playerChoice == "look at door":
        if roomName == "startRoom" or roomName == "entranceCorridor": #hmm. reconsider entranceCorridor needing only "examine door" to disarm trap from other side
            print objectDescription["suspiciousDoor"]
            disabledThreats.append("suspiciousDoor") #add rigged door to disabled threats list
        else:
            print "A door, like any other in this dungeon. Dusty, ancient, thick wood."
        coreGameLoop(roomName, False, False)

    elif playerChoice == "examine tile" or playerChoice == "examine tiles" or playerChoice == "examine floor":
        if roomName == "corridor1":
            print objectDescription["suspiciousTile"]
            disabledThreats.append("suspiciousTile") #add suspicious tile to disabled threats list
        else:
            print "The same smooth stone everywhere, layer of dust throughout."
        coreGameLoop(roomName, False, False)

    #--------------------------------------------------------------------------------------------------------------
    #player wants to examine something; the general case
    elif playerChoice[0:playerChoice.find(" ")] == "examine":
        subject = playerChoice[playerChoice.find(" "):]
        subject = subject.lstrip()#remove trailing whitespace
        objectToBeExamined = translateSubjectToGameObject(subject, roomName)#map subject to a gameobject (things in objectDescription dictionary)
        if objectToBeExamined == "NaO":
            #error condition, subject isnt a valid gameObject
            print "No idea what that is, or if it can even be examined."
        else:
            print objectDescription[objectToBeExamined] #couldve just combined these two lines, but splitting for code readability
        coreGameLoop(roomName, False, False)

    #--------------------------------------------------------------------------------------------------------------
    

    #combat handling
    # If enemy killed, append roomName to enemyWasKilledHere list
    # Note: simpler to have the same approach as treasure chests i.e. del(), but not if more enemies are added.

    elif "fight" in playerChoice or "attack" in playerChoice or "hit" in playerChoice or "kill" in playerChoice:
        subject = playerChoice[playerChoice.find(" "):]
        subject = subject.lstrip()#remove trailing whitespace

        if roomName in roomHasMonsters and isMonster(subject) == True:
            if roomName == "trapRoom" and (subject == "skeleton" or subject == "skeletons"):
                die("""
                    You swing your sword at the first skeleton in your way, dismantling it to pieces. 
                    As you turn around to face the others, triumphant, the slain skeleton rises up behind you. 
                    Grinning their death stare, they run you through with their swords.
                    """)
            elif roomName == "corridor5" and (subject == "zombie"):
                print("""
                        You hack at the slow moving dread zombie, lopping off its arms, a leg, and finally its head to make it stop moving. 
                        Wiping a sweat from your brow, you half expect it to rise up...
                        ...but it stays dead. 
                        Phew.
                    """)
                enemyWasKilledHere.append(roomName)# append this room's name to enemyWasKilledHere list. Needed for alt descriptions of rooms post-monster purge

                disabledThreats.append("zombie")#append zombie to disabled threats list for...idk. Maybe to implement "block exit until enemy killed" idea?

                coreGameLoop(roomName, False, False)
            elif roomName == "treasureRoom" and (subject == "guardian" or subject == "boss"):
                die("""
                    The guardian laughs at your pathetic attacks as they bounce off its armor.
                    One swing of its massive zweihander is all it takes to put an end to your adventure.
                    Laying on the bloody floor, all thoughts disappear, as you vaguely wonder why you are looking at your lower body, twitching legs and all, lying halfway across the room.
                    """
                    )
                #guardian boss cant be killed by conventional means.
        else: #player in a room that doesnt have monsters, or subject isnt a monster      
                print "I'm not sure what that is, nor that it can be attacked."
                print "Clearly, this is not the way to go."
                coreGameLoop(roomName, False, False)

    #--------------------------------------------------------------------------------------------------------------
    #pick things up
    elif "get" in playerChoice:
        subject = playerChoice[playerChoice.find(" "):]
        subject = subject.lstrip()#remove leading whitespace
        print "subject : %s"  % subject
        gameObject = translateSubjectToGameObject(subject, roomName)# if subject is an actual game object

        if gameObject in gettableObjectsList and gameObject != "NaO":#the NaO check is useless, but needed for elif/else print statements' distinction
            playerInventory.append(gameObject)
            print "You pick the %s up." % subject
        elif gameObject not in gettableObjectsList and gameObject != "NaO":
            print "The %s is too heavy to pick up and carry around." % gameObject
        else:
            print "I don't know what that is, or if it can even be picked up."

        coreGameLoop(roomName, False, False)

    #--------------------------------------------------------------------------------------------------------------
    #use <inventory item> on <gameObject>
    elif ("use" in playerChoice) and ("with" in playerChoice or "on" in playerChoice):
        #get subject1
        #two steps to get there...
        tempString = playerChoice[playerChoice.find(" "):].lstrip()
        subject1 = tempString[:tempString.find(" ")] 
        print "DEBUG : subject1 = %s" % subject1
        #get subject2
        subject2 = playerChoice[playerChoice.rfind(" "):].lstrip() #range = last occurrence of a space to end of string
        print "DEBUG : subject2 = %s" % subject2

        #subject1 should be in inventory, and subject2 a valid gameobject in same room as player 
        if (subject1 in playerInventory) and (translateSubjectToGameObject(subject2,roomName) != "NaO"):
            print "You wave the %s around in the %s's proximity, and can barely conceal your total lack of surprise as nothing of note happens." % (subject1,subject2)
        elif subject1 == "scroll" and translateSubjectToGameObject(subject2,roomName) == "guardianBoss":
            print """
                        As you recite the words from the scroll, the boss pauses a minute, perplexed.
                        And then screams in agony as light beams burst from inside, eliminating it from existence.
                        You drop to your knees, exhausted. You've done it. The room is clear.
            """
            disabledThreats.append("guardianBoss")
            enemyWasKilledHere.append("treasureRoom")
            global bossKilled
            bossKilled = True
        else:
            print "I either dont own %s or dont know what %s is." % (subject1, subject2)

        coreGameLoop(roomName, False, False)

    #--------------------------------------------------------------------------------------------------------------
    #finally, handle movement in compass directions
    elif playerChoice in directionsList:

        #get destination, based on the room player is currently in + direction entered
        goTo = goToRoom(roomName, playerChoice)

        if goTo == "NaD":
            print "You cannot go in that direction."
            coreGameLoop(roomName, True, False)
        elif goTo == "exitRoom":
            #print "DEBUG : Checking if you have exitKey... % s" % "key" in playerInventory
            if "exitKey" in playerInventory:
                #print some description of your freedom
                print objectDescription["freedom"]
                #gameEndScreen
                showFinalScore()
            else:
                print "You don't have the key to the exit gate. You do have a bad feeling about its resting place, though..."
                coreGameLoop(roomName, False, False)
        else:
            #all processing that relies on percept checks/disabled threats goes here :

            #the rigged door
            if "suspiciousDoor" not in disabledThreats and (roomName == "startRoom" or roomName == "entranceCorridor") and (goTo == "entranceCorridor" or goTo == "startRoom"):#both ways
                die("A rigged trap door blows up in your face.")
            #the trap tile
            elif "suspiciousTile" not in disabledThreats and (roomName == "corridor1") and (goTo == "corridor2"):# no need for both ways as there isnt a way to go to corridor2 without disabling this trap
                die("You fall to your doom, a suspicious tile falling away into the abyss as you step on it. You curse your lack of perceptiveness.")
            #the brick outcropping hiding a west exit
            elif "brickOutcropping" not in discoveredSecrets and roomName == "corridor2" and goTo == "corridor4":
                print "There is no west exit here. As far as you can tell without a close examination, there's a pretty solid brick wall in the way."
                coreGameLoop(roomName, False, False)
            #the wall in deadEndRoom hiding an exit to the south
            elif "deadEndSouthWall" not in discoveredSecrets and roomName == "deadEndRoom" and goTo == "entranceCorridor":
                print "There is exit that way. As far as you can tell, this room is a dead end. A wall blocks the way south."
                coreGameLoop(roomName, False, False)
            #zombie blocking way
            elif "zombie" not in disabledThreats and roomName == "corridor5" and goTo == "corridor6":
                print "The zombie is blocking your way. You have to take him out before going further!"
                coreGameLoop(roomName, False, False)
            #guardian preventing you going back out
            elif "guardianBoss" not in disabledThreats and roomName == "treasureRoom":
                print "The guardian wont let you leave!"       #placeHolder text. Elaborate more later?
                coreGameLoop(roomName, False, False)
            else:
                coreGameLoop(goTo, True, False)
    
    #--------------------------------------------------------------------------------------------------------------
    #cheatCodes, including: roomskip for debug/test, <tba>
    elif playerChoice == "cheat":
        print "Type go roomName to go there, add objectName to add it to inventory, 0 to restart coreGameLoop"
        cheatCode = raw_input(">#> ")
        if "go" in cheatCode and cheatCode[cheatCode.find(" "):].lstrip() in objectDescription:
            coreGameLoop(cheatCode[cheatCode.find(" "):].lstrip(), True, False)
        elif "add" in cheatCode and cheatCode[cheatCode.find(" "):].lstrip() in objectDescription:
            playerInventory.append(cheatCode[cheatCode.find(" "):].lstrip())
        else:
            coreGameLoop(roomName, True, False)

    #--------------------------------------------------------------------------------------------------------------
    #base case; could not parse player's intent
    else:
        print "I don't understand that."
        coreGameLoop(roomName, False, False)    

########################################################################################
def showFinalScore(): #scoresheet
    print "##############################################"
    print "CONGRATULATIONS! You've beaten the game!"
    print "Your final stats were..."
    print "Baubles Begotten         : %d" % playerGP
    #print "hp left                  : %d" % playerHP
    print "Threats Terminated       : %d" % len(disabledThreats) #TODO:award points based on traps disarmed and enemies killed (different point weights)
    print "Guardian Slayer          : %s" % bossKilled
    #add more when implemented: enemies slain, enemies escaped from, was guardian killed? etc.
    print "Thank you for playing!"
    print "##############################################"
########################################################################################   
coreGameLoop("startRoom", True, False) #start it off!
########################################################################################

