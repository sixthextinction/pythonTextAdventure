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

#associative array to do roomDescription['roomName'] later
roomDescription =   {
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

                                            There seems to be nothing here but another sconce lighting the way round a corner; another corridor to the north.
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
                                            Yet another corridor. You're finally begin to appreciate the architectural genius of this place. You're now certain of how easy it is to get lost here, roaming forever.
                                            Good thing you have a map. You do have a map, right?
                                            Your thoughts are interruted by guttural, inhuman moaning echoing down the stone halls. Flickering shadows on the walls ahead. Bad news.

                                            Whatever it is, it lies to the east. 
                                            """,
                        "corridor6" :       """
                                            You can't believe your eyes. Daylight to the west. Filtering in through the widest gate you've seen here so far.
                                            These halls are wider than any other in this place. You check around for danger, but there seems to be none apparent.
                                            Home stretch.

                                            Your ticket out of here is to the west. 
                                            """,
                        "treasureRoom" :    """
                                            The Guardian stands here in this bloody room, among bones and discarded gear of heroes past, a dozen arms tall, metal plates intertwining with chains, dirty leather hood hiding his grotesque visage.
                                            He has been waiting for you. He grins, bare, bloody teeth and all, as he picks up his greatsword. 
                                            A key hangs from a hook on the wall behind him.

                                            Are you prepared? There is no exit. 
                                            """,
                        "trapRoom" :        """
                                            Dark. No sconces. No magelight. The darkness here is thick and suffocating. A different animal altogether. It's an oily ooze, pervading in the air.
                                            Clattering of bones and metal.
                                            This was a trap.
                                            You curse, throwing your lantern on the floor and whipping around.
                                            Three skeletons. Undead protectors of some long-forgotten master. Their swords are curved. 

                                            The door behind you is barred, through sorcery or otherwise, you could not care less. No escape that way.
                                            There is an exit to the northeast, if you can make it there.
                                            """
                    }
#associative array to do objectDescription(objectID)
objectDescription = {
                        "suspiciousDoor"    :  """
                                            You peer at the door, and notice nothing different. You start to give it a gentle push...
                                            ...and immediately shrink back.
                                            That was a close one. There's a hair trigger of a wire connecting the edge to some invisible apparatus inside the wall.
                                            You judiciously cut the wire, and jump as there is a tiny, but piercing, clink from above.
                                            Whatever you have done, seems to have defused the trap.
                                            """,
                        "treasureChest"     :   "Just your everyday large wood-and-metal chest. You can unlock this.",
                        "suspiciousTiles"   :   "Your perceptive nature pays off. The unnatural tile architecture hides a pressure trap. You disarm it. Close shave.",
                        "brickOutcropping"  :   "You run your hand across the outcropping, and discover one of the bricks is loose! Pulling on it reveals a secret passage!",
                        "corridor3Gate"     :   "Just your regular everyday metal gate. Which is also, unfortunately, of the locked variety. The lock has long since eroded away, to boot. Drat.",
                        "zombie"            :   "Ghastly un-life stares back at you through maggot infested eyesockets. A mass of rotten flesh, loose coils of intestine, and jagged teeth, shambling towards you, inch by fatal inch. ",
                        "exitGate"          :   "Large, barred gates. Comically oversized chains and a lock fasten it securely in place. It's locked, needless to say. You need a key to get out of here.",
                        "guardianBoss"      :   "A towering mound of interlocking black metal plates and the biggest greatsword you've ever seen (har har). You can make out a hint of his black eyes and slathering fangs under that leather hood, pulled down low.",
                        "exitKey"           :   "The key to your freedom hangs there, glittering in the magelight, as it has for the past few hundred years. Is there a way to get to it, dodging the Guardian?"
                    }

playerHP = 100  #HP
playerGP = 0    #Gold

#treasureObtained = False

perceptionCheck = False #default, resets for each room
prompt = "What do you do? > "
########################################################################################
def goToRoom(origin, direction):
    print ""
########################################################################################
def die(why):
    print " %s Well done!" % why
    sys.exit(0) #this and "import sys" are temporary workarounds to "exit takes no arguments". What's the real cause?
########################################################################################
def dangerAlert():
    print "Careful. Something sinister lurks here...\n"
########################################################################################
def coreGameLoop(roomName, includeDescription, treasureObtained):
    treasurePresent = False

    if (includeDescription):
        print roomDescription[roomName]
    if (roomName in roomHasTreasure) and (treasureObtained == False):
        treasurePresent = True
        print "There's a treasure chest here."

    playerChoice = raw_input(prompt)

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

