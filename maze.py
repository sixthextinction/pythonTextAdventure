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

                                            You grow wary as you see the rusty, foreboding metal gate to the east.
                                            """,
                        "corridor4" :       """
                                            Yet another corridor. You're finally begin to appreciate the architectural genius of this place. You're now certain of how easy it is to get lost here, roaming forever.
                                            Good thing you have a map. You do have a map, right?
                                            Your thoughts are interruted by guttural, inhuman moaning echoing down the stone halls. Flickering shadows on the walls ahead. Bad news.

                                            Whatever it is, it lies to the east. 
                                            """,
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
                    
#now objects :

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
                        "corridor3Gate"     :   "Just your regular everyday metal gate. Which is also, unfortunately, of the locked variety. The lock has long since eroded away, to boot. Drat.",
                        "zombie"            :   "Ghastly un-life stares back at you through maggot infested eyesockets. A mass of rotten flesh, loose coils of intestine, and jagged teeth, shambling towards you, inch by fatal inch. ",
                        "exitGate"          :   "Large, barred gates. Comically oversized chains and a lock fasten it securely in place. It's locked, needless to say. You need a key to get out of here.",
                        "guardianBoss"      :   "A towering mound of interlocking black metal plates and the biggest greatsword you've ever seen (har har). You can make out a hint of his black eyes and slathering fangs under that leather hood, pulled down low.",
                        "exitKey"           :   "The key to your freedom hangs there, glittering in the magelight, as it has for the past few hundred years. Is there a way to get to it, dodging the Guardian?",
                        "skeleton"          :   "A reanimated soldier, moldy bones held together by some unholy magic. It carries a curved sword, and the red misty glow in its otherwise empty orbits, hungers for your blood."
                    }

directionsList = [ "north", "northwest", "west", "southwest", "south", "southeast", "east", "northeast" ]

monstersList   =    [ "skeleton", "zombie", "guardian", "boss" ]

subjectToGameObjectMap =    { #only covers mappings that can have a 1:1 resolution. "room" can't, as it can have multiple versions depending on roomName. Resolve that elsewhere.
                            "chest"         :   "treasureChest",
                            "treasure"      :   "treasureChest",
                            "tile"          :   "suspiciousTile",
                            "tiles"         :   "suspiciousTile",
                            "zombie"        :   "zombie",#redundant?
                            "guardian"      :   "guardianBoss",
                            "boss"          :   "guardianBoss",
                            "key"           :   "exitKey",
                            "skeleton"      :   "skeleton"#redundant?
                            }
subjectToRoomMap =  {
                        "skeleton"  :   "trapRoom",
                        "zombie"    :   "corridor5",
                        "boss"      :   "treasureRoom",
                        "guardian"  :   "treasureRoom",
                        "key"       :   "treasureRoom"
                    }
playerHP = 100  #HP
playerGP = 0    #Gold

#treasureObtained = False

perceptionCheck = False #default, resets for each room
prompt = "What do you do? > "
########################################################################################
def goToRoom(origin, direction):
    #simple implementation for now...
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
        else:
            return "NaD"
    #--------------------------------------------
    elif (origin == "entranceCorridor"):
        if (direction == "south"):
            return "corridor1"
        else:
            return "NaD"
    #--------------------------------------------
    elif (origin == "corridor1"):
        if (direction == "west"):
            return "corridor2"
        else:
            return "NaD"
    #--------------------------------------------
    elif (origin == "corridor2"):
        if (direction == "northwest"):
            return "corridor3"
        elif (direction == "west"):
            return "corridor4"
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
        else:
            return "NaD"
    #--------------------------------------------
    elif (origin == "corridor5"):
        if (direction == "south"):
            return "corridor6"
        else:
            return "NaD"
    #--------------------------------------------
    elif (origin == "corridor6"):
        if (direction == "northwest"):
            return "treasureRoom"
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
    sys.exit(0) #this and "import sys" are temporary workarounds to "exit takes no arguments". What's the real cause?
########################################################################################
def dangerAlert():
    print "Careful. Something sinister lurks here...\n"
########################################################################################
def getAltDescription(roomName):
    return "Alternate %r description here." % roomName
########################################################################################
def isMonster(subject):
    if subject in monstersList:
        return True
    else:
        return False
########################################################################################
def mapSubjectToGameObject(subject, roomName):
    # print "*** DEBUG : subject %s in subjectToGameObjectMap? : %r" % (subject, subject in subjectToGameObjectMap)
    # print "*** DEBUG : Again, manually this time. ""guardian"" in subjectToGameObjectMap? : %r" % ("guardian" in subjectToGameObjectMap)
    # print "*** DEBUG : Wtf? Ok. Try this : subjectToGameObjectMap[guardian] : %s" % (subjectToGameObjectMap["guardian"])
    # print "*** DEBUG : Alright, getting somewhere. subject == <space>guardian? %r : " % (subject == " guardian")
    # print "*** DEBUG : Almost there. subject == guardian? %r : " % (subject == "guardian")

    #there's the problem. A rogue whitespace just before the subject string.
    #lets fix that :
    #subject = subject.lstrip() #remove leading whitespaces (empty array passed)

    #prevent examining gameObjects not in the room the player is currently in.
    # Do this by maintaining an associative array. 
    #ex. subjectToRoomMap = { "skeleton" : "trapRoom", "zombie" : "corridor5"} and so on.
    #only if subjectToRoomMap["skeleton"] == roomName, return subjectToGameObjectMap[subject]

    if subject in subjectToGameObjectMap and subjectToRoomMap[subject] == roomName:
            # print "*** DEBUG : subject : %s" % subject
            # print "*** DEBUG : roomName : %s" % roomName
            # print "*** DEBUG : mapSubjectToGameObject() returning : %s" % subjectToGameObjectMap[subject]
            return subjectToGameObjectMap[subject]
    elif subject == "room":
        # print "*** DEBUG : subject : %s" % subject
        # print "*** DEBUG : roomName : %s" % roomName
        # print "*** DEBUG : mapSubjectToGameObject() returning : %s" % objectDescription[roomName]
        return objectDescription[roomName]
    else:
        # print "*** DEBUG : subject : %s" % subject
        # print "*** DEBUG : roomName : %s" % roomName
        # print "*** DEBUG : mapSubjectToGameObject() returning : NaO" 
        return "NaO" #not an examinable subject. An errorcode, basically, like NaD.
########################################################################################
def coreGameLoop(roomName, includeDescription, treasureObtained):
    treasurePresent = False

    print "You are in : %s" % roomName

    if (includeDescription):
        if (perceptionCheck == True):
            print getAltDescription(roomName)
        else:
            print objectDescription[roomName]
    if (roomName in roomHasTreasure) and (treasureObtained == False):
        treasurePresent = True
        print "There's a treasure chest here."

    playerChoice = raw_input(prompt)

    #SUGGESTION : More efficient action processing system 
    #   action  = playerChoice[0:playerChoice.find(" ")]    //substring until a space 
    #   subject = playerChoice[playerChoice.find(" "):]     //substring from space til end for the object being referred to
    #   if action in list_of_valid_actions:                //check if its a valid action
    #       send off object for processing
    # ^^^ maybe like so?

    #player wants to do something with the treasure chest :
    if ("chest" in playerChoice or "treasure" in playerChoice) and treasurePresent == True:
        #player wants to examine it :
        if "examine" in playerChoice or "look at" in playerChoice:
            print objectDescription["treasureChest"]
            coreGameLoop(roomName, False, False)
        #player wants to unlock it :
        elif "unlock" in playerChoice:
            #treasureObtained = True
            goldObtained = roomHasTreasure[roomName]
            print "You obtain %d gold!" % goldObtained
            global playerGP
            playerGP += goldObtained
            coreGameLoop(roomName, False, True)
        #could not parse player's intent :
        else:
            print "I don't know what you mean to do with the treasure chest."
            coreGameLoop(roomName, False, False)

    #player wants to examine the room        
    elif playerChoice == "examine room" or playerChoice == "look around" or playerChoice == "look at room":
        coreGameLoop(roomName, True, False)

    #trap/reveal checks
    elif playerChoice == "examine wall":
        if roomName == "corridor2":
            global perceptionCheck
            perceptionCheck = True #percept check succeeded!
            print objectDescription["brickOutcropping"]
        else:
            print "Smooth, ancient stone. The uniformity hurts your eyes if you look around long enough. It's all very disorienting, to be honest."
        coreGameLoop(roomName, False, False)

    elif playerChoice == "examine door":
        if roomName == "startRoom":
            global perceptionCheck
            perceptionCheck = True #percept check succeeded!
            print objectDescription["suspiciousDoor"]
        else:
            print "A door, like any other in this dungeon. Dusty, ancient, thick wood."
        coreGameLoop(roomName, False, False)
    elif playerChoice == "examine tile" or playerChoice == "examine tiles" or playerChoice == "examine floor":
        if roomName == "corridor1":
            global perceptionCheck
            perceptionCheck = True
            print objectDescription["suspiciousTile"]
        else:
            print "tilez. Floorz. Hur dur."
        coreGameLoop(roomName, False, False)

    #player wants to examine something; the general case
    elif playerChoice[0:playerChoice.find(" ")] == "examine":
        subject = playerChoice[playerChoice.find(" "):]
        subject = subject.lstrip()#remove trailing whitespace
        #print "***DEBUG : registered general case examine. Subject was : %s" % subject
        #this is a test :
        objectToBeExamined = mapSubjectToGameObject(subject, roomName)#map subject to a gameobject (things in objectDescription dictionary)
        if objectToBeExamined == "NaO":
            #error condition, subject isnt a valid gameObject
            print "No idea what that is, or if it can even be examined."
        else:
            print objectDescription[objectToBeExamined] #couldve just combined these two lines, but splitting for code readability
        coreGameLoop(roomName, False, False)

    

    #combat handling
    elif "fight" in playerChoice or "attack" in playerChoice or "hit" in playerChoice:
        subject = playerChoice[playerChoice.find(" "):]
        subject = subject.lstrip()#remove trailing whitespace

        if roomName in roomHasMonsters and isMonster(subject) == True:
            if roomName == "trapRoom" and (subject == "skeleton" or subject == "skeletons"):
                die("You swing your sword at the first skeleton in your way, dismantling it to pieces. As you turn around to face the others, triumphant, the slain skeleton rises up behind you. Grinning their death stare, they run you through with their flechettes.")
            elif roomName == "corridor5" and (subject == "zombie"):
                print("""
                        You hack at the slow moving dread zombie, lopping off its arms, a leg, and finally its head to make it stop moving. 
                        Wiping a sweat from your brow, you half expect it to rise up...
                        ...but it stays dead. 
                        Phew.
                    """)
                coreGameLoop(roomName, False, False)
            elif roomName == "treasureRoom" and (subject == "guardian" or subject == "boss"):
                die("""
                    The guardian laughs at your pathetic attacks as they bounce off its armor.
                    One swing of its massive zweihander is all it takes to put an end to your adventure,
                    as lying on the bloody floor, all thoughts disappear, and you can only vaguely wonder why you are looking at your lower body, twitching legs and all, lying halfway across the room.
                    """
                    )
        else: #player in a room that doesnt have monsters, or subject isnt a monster      
                print "I'm not sure what that is, nor that it can be attacked."
                print "Clearly, this is not the way to go."
                coreGameLoop(roomName, False, False)


    #finally, handle movement in compass directions
    elif playerChoice in directionsList:
        goTo = goToRoom(roomName, playerChoice)

        

        if goTo == "NaD":
            print "You cannot go in that direction."
            coreGameLoop(roomName, True, False)
        else:
            #do perceptionCheck etc. processing here:
            if perceptionCheck == False and roomName == "startRoom" and goTo == "entranceCorridor":
                die("A rigged trap door blows up in your face.")
            else:
                global perceptionCheck
                perceptionCheck = False
                coreGameLoop(goTo, True, False)
        
    #could not parse player's intent
    else:
        print "I don't understand that."
        coreGameLoop(roomName, False, False)    

########################################################################################
def showFinalScore(): #scoresheet
    print ""
########################################################################################   
coreGameLoop("startRoom", True, False) #start it off!
########################################################################################

