import sys
import Scene
class Game(object):
#################################################################################################################################################
    def __init__(self, mazeEngineInstance):
        # debugMsg = "DEBUG : taking %r as an argument" % mazeEngine
        # debugMsg = "DEBUG : So, mazeEngine.startRoom = %r " % mazeEngine.startRoom
        self.engineInstance = mazeEngineInstance
        # debugMsg = "DEBUG : now, engineInstance.startRoom = %r" % self.engineInstance.startRoom
            
        self.core_game_loop(self.engineInstance.startRoom) 
#################################################################################################################################################
    def core_game_loop(self, currentRoom):

        # Stuff to print out information about room
        # Comment in/out as needed.
        #
        # print "######################################################################"
        # print "CURRENT ROOM NAME             : %s"           %      currentRoom.name
        # print "TREASURE AMT IN %s                   :  %d"      %      (currentRoom.name, currentRoom.treasureAmount)
        # print "ITEMS IN %s                   : "             %      currentRoom.name
        # for item in currentRoom.items:
        #     #the status of item,  basically
        #     print "\t%s. Taken? : %s" %(item.name, currentRoom.items[item])
        # if len(currentRoom.items) == 0:
        #     print "\tNone"

        # print "MONSTERS IN %s : " % currentRoom.name
        # for monster in currentRoom.monsters:
        #     #the status of threat,  basically
        #     print "\t%s. Disabled? : %s" %(monster.name, currentRoom.monsters[monster])
        # if len(currentRoom.monsters) == 0:
        #     print "\tNone"

        # print "TRAPS IN %s : " % currentRoom.name
        # for monster in currentRoom.traps:
        #     #the status of threat,  basically
        #     print "\t%s. Disabled? : %s" %(trap.name, currentRoom.traps[trap])
        # if len(currentRoom.threats) == 0:
        #     print "\tNone"

        # print "SECRETS in %s : " % currentRoom.name
        # for secret in currentRoom.secrets:
        #     #status of secret
        #     print "\t%s. Discovered? : %s" % (secret.name, currentRoom.secrets[secret])
        # if len(currentRoom.secrets) == 0:
        #     print "\tNone"
        # print "######################################################################"
        

        print "_____________________________________________________________________"

        roomDescToPrint = ""
        if self.engineInstance.player.HP >= 1 and isinstance(currentRoom, Scene.Room) == True: 
            if (False not in currentRoom.monsters.values() and len(currentRoom.monsters)!=0) or (False not in currentRoom.traps.values() and len(currentRoom.traps)!=0) or (False not in currentRoom.secrets.values() and len(currentRoom.secrets)!=0):
                roomDescToPrint = currentRoom.altDescription
            else:
                roomDescToPrint = currentRoom.description
        playerChoice = ""
        nextRoom = ""
        subject = "" # subject of a verb i.e. "x" in "examine x", for example

        debugMsg = "DEBUG : Enter directions to go to that room, 'quit' to end test.\n"
        self.debug(debugMsg)

        # Add the presence of any items in this room (gettable/chests, whatever) to the room description about to be printed
        # FIX BUG : this section needs to trigger for an "examine room" input too
        # ADD : also triggers for visible monsters (for s in currentRoom.monsters?)

        # check if currentRoom is instance of Scene (Separate processing needed for that)
        if isinstance(currentRoom, Scene.Screen) == False:
            for s in currentRoom.items:
                    #if item s was NOT picked up/opened up i.e. it's still in currentroom.items
                    if (currentRoom.items.get(s) == False):
                        roomDescToPrint += "\n%s" % self.engineInstance.tackOnSceneDescriptions[s]


            # Finally, print the room description
            print roomDescToPrint

            # Print a list of all exits to and from this room if HP >=1
            if self.engineInstance.player.HP >= 1: 
                self.printExits(currentRoom)

            # Start the player input-game cycle loop 
            while (True): 

                if self.engineInstance.player.HP < 1: 
                    print "YOU DIED. FINAL SCORE : %d" % self.engineInstance.player.score
                    print "GOLD ACQUIRED : %d" % self.engineInstance.player.GP
                    sys.exit(0)

                playerChoice = raw_input("> ")
                
                #if playerChoice == reload (debug option)
                # if playerChoice == "reload":
                #     print "_____________________________________________________________________"
                #     self.core_game_loop(currentRoom)

                #if playerChoice = exit
                if playerChoice == "quit" or playerChoice == "exit":
                    #print something and then quit
                    print "_____________________________________________________________________"
                    print "Thank you for playing OOPMaze!"
                    sys.exit(0)
                    break

                #if playerChoice = examine something
                elif playerChoice[:playerChoice.find(" ")] == "examine":
                    subject = playerChoice[playerChoice.find(" "):].lstrip()
                    self.examine(currentRoom, subject)
                    self.printExits(currentRoom)

                # if playerChoice = get something
                elif playerChoice[:playerChoice.find(" ")] == "get":
                    subject = playerChoice[playerChoice.find(" "):].lstrip()

                    debugMsg = "subject= %s" % subject
                    self.debug(debugMsg)

                    self.get(currentRoom, subject)
                    self.printExits(currentRoom)

                # if playerChoice = use x with y/use x on y
                elif playerChoice[:playerChoice.find(" ")] == "use":        # "use"
                        s = playerChoice[playerChoice.find(" "):].lstrip()  # "x with y"
                        subject = s[:s.find(" ")]                           # "x"
                        s = s[s.find(" "):].lstrip()                        # "with y"
                        predicate = s[s.find(" "):].lstrip()                # "y"
                        self.use(currentRoom, subject, predicate)
                        self.printExits(currentRoom)
                # if playerChoice = open chest, or get treasure. 

                elif playerChoice == "open chest":
                    # straightforward. Grab predefined treasure amount for this room, add it to player's GP score.
                    if currentRoom.treasureAmount == 0:
                        print "Can't see any treasure in this room."
                    else:
                        self.engineInstance.player.GP += currentRoom.treasureAmount
                        print "Obtained %d gold!" % currentRoom.treasureAmount
                        # set currenRoom.treasureAmount to 0, since it's been obtained already
                        currentRoom.treasureAmount = 0

                #if playerChoice = "exits" (possibly flesh this out more)
                elif playerChoice == "exits":
                    self.printExits(currentRoom)

                #if playerChoice = "inventory"
                elif playerChoice == "inventory":
                    self.printInventory(self.engineInstance)

                #if playerChoice = a direction
                elif playerChoice in currentRoom.exits:
                    # default case. Overwrite nextRoom later if necessary after monster/trap checks
                    nextRoom = currentRoom.exits[playerChoice]

                    # check for monsters
                    # if >=1 monster still present as unresolved threats
                    if False in currentRoom.monsters.values() and currentRoom not in self.engineInstance.escapableRooms: # and roomName not in listOfEscapableRooms
                        # print the monsters that prevent you from leaving
                        print "Can't leave yet, the presence of the "
                        for monster in currentRoom.monsters:
                            if currentRoom.monsters[monster] == False:
                                print "%s," % monster.name
                        print "prevents you from leaving"
                        # overwrite nextRoom in this case
                        nextRoom = currentRoom

                    # check for traps
                    # if this (direction, room) pair triggers a trap,
                    if (playerChoice, currentRoom) in self.engineInstance.directionalThreats:
                        # first, for convenience, retrieve the actual threat  (trap GameObject) in a variable
                        threatInQuestion = self.engineInstance.directionalThreats[(playerChoice,currentRoom)]
                        # then, check if this trap was disarmed
                        if currentRoom.traps[threatInQuestion] == False:
                            # it wasn't, so it goes boom. Damage player.
                            print "It's a trap! You fell for the %s!" % threatInQuestion.name # need alternate, "common" names
                            # possibly add trap specific output text here
                            self.engineInstance.player.HP -= 1
                            # overwrite nextRoom in this case
                            nextRoom = currentRoom
                        # It WAS disarmed; safe passage. nextRoom won't be overwritten in this case, and is still the default value.
                        else:
                            print "You've disabled the %s, it is safe to proceed %s" % (threatInQuestion.name,playerChoice)
                            
                    self.core_game_loop(nextRoom)

                # Testing a HP reduction from another function
                elif playerChoice == "die":
                    self.die()

                # attack/hit/kill commands
                
                elif (playerChoice[:playerChoice.find(" ")] == "kill") or (playerChoice[:playerChoice.find(" ")] == "attack") or (playerChoice[:playerChoice.find(" ")] == "hit"):
                    subject = playerChoice[playerChoice.find(" "):].lstrip()
                    damageDealt = 1
                    debugMsg = "subject = %s" % subject
                    self.debug(debugMsg)

                    debugMsg = "subject in self.engineInstance.nameMap? = %s" % (subject in self.engineInstance.nameMap)
                    self.debug(debugMsg)
                    debugMsg = "self.engineInstance.nameMap = %r " % (self.engineInstance.nameMap[subject].name) 
                    self.debug(debugMsg)

                    if subject in self.engineInstance.nameMap and self.engineInstance.nameMap[subject] in currentRoom.monsters:
                        translatedObject = self.engineInstance.nameMap[subject]
                        translatedObject.HP -= damageDealt
                        print "You swing your sword and hit the %s for %d damage." % (subject, damageDealt) # hardcoded for 1 dmg
 
                        if translatedObject.HP == 0:
                            print "The %s is dead!" % subject
                            # mark monster as disabled
                            currentRoom.monsters[translatedObject] = True
                            # give player points for killing monster
                            if translatedObject.isPlural == 0:
                                self.engineInstance.player.score += 20 
                            else:
                                self.engineInstance.player.score += 40 # more points for killing clusters of enemies (if even possible) instead of enemies who are alone
                        else:
                            # monster counterattacks
                            self.counterattack(translatedObject)
                            

                    elif subject in self.engineInstance.nameMap and self.engineInstance.nameMap[subject] not in currentRoom.monsters:
                        print "I don't see a %s here." % subject
                    else:
                        print " I don't know what a %s is." % subject
                #base case
                else:
                    print "\tI don't know what that means."
                    self.core_game_loop(currentRoom)

        # currentRoom IS an instance of Screen, not Room
        else:
            print "Encountered a SCREEN : %s" % currentRoom.name
            print "screen says : %s" % currentRoom.description
            if currentRoom == self.engineInstance.victoryScreen:
                # show score
                print "FINAL SCORE : %d" % self.engineInstance.player.score
                print "GOLD ACQUIRED : %d" % self.engineInstance.player.GP
                sys.exit(0)
            elif currentRoom == self.engineInstance.deathScreen:
                sys.exit(0)
            else:
                # for custom screens, used for purposes other than victory or death
                pass # for now
            # sys.exit(0)
            # No single exit statement at the end of this else block, as you might want to still stay in the core game loop whilst displaying a screen (in the middle of the dungeon)
        

#################################################################################################################################################
    def die(self):
        #test for functionality of an hp reduction from another function
        self.engineInstance.player.HP -=1
#################################################################################################################################################
    def counterattack(self, monster):
        #if monster.HP >= 1:
        if monster.isPlural == 0:
            print "The %s counterattacks!" % monster.name
        else:
            print "The %s counterattack!" % monster.name

        self.engineInstance.player.HP -= 1
#################################################################################################################################################

    def examine(self, currentRoom, subject):
        """
        Examines a subject,
        and either resolves it if its a trap (examining a trap more closely would disable it, or let you avoid it)
        or prints a string; the description of the gameObject translated from 'subject',
        after checking for the subject's presence in the 'currentRoom' object (instance of Room class) 
        (can't look at an object that isn't in the room. Print a "I cant see this" message in that case.)
        """

        retString = ""
        debugMsg = ""

        #debugMsg = "DEBUG : stage 1 : type(retString) = %s" % type(retString)

        # translate the subject string into a GameObject instance (say, translatedObject) that the engine recognizes.
        # if subject is in this Engine instance's nameMap (a dict that maps string/subject to gameObject)...
        if (subject in self.engineInstance.nameMap):
            # ...then retrieve the actual gameObject instance the subject is equivalent to
            translatedObject = self.engineInstance.nameMap[subject]

            # debugMsg = "DEBUG : translatedObject name = %s" % translatedObject.name
            # self.debug(debugMsg)

            # 1) if examined object is a monster/threat or an item...
            if (translatedObject in currentRoom.monsters) or (translatedObject in currentRoom.items) or (translatedObject in currentRoom.traps): 
                # ...just get its description
                retString = translatedObject.description

                # debugMsg = "DEBUG : stage 2 : type(retString) = %s" % type(retString)
                # self.debug(debugMsg)

                # and if trap, disarm
                if translatedObject in currentRoom.traps:  
                    #... mark that threat as disabled
                    currentRoom.traps[translatedObject] = True 
                    # give player points for disarming trap
                    self.engineInstance.player.score += 10                                

            # 2) if examined object is a secret...
            elif (translatedObject in currentRoom.secrets):
                # first, get its description...
                retString = translatedObject.description

                # debugMsg = "DEBUG : stage 2 : type(retString) = %s" % type(retString)
                # self.debug(debugMsg)
                
                # then, if the secret has not been discovered yet...
                if (currentRoom.secrets[translatedObject] == False):
                    # using dicts
                    # retrieve the room this secret passage leads to...
                    leadsTo = self.engineInstance.leadsTo[translatedObject]
                    print "leads to : %r" % leadsTo.name
                    # retrieve the direction that that room, discovered through a secret passage, leads from...
                    direction = self.engineInstance.leadsFrom[leadsTo]
                    print "leads from direction : %r" % direction
                    # add that direction to the currentroom's exits list.
                    currentRoom.exits[direction] = leadsTo
                    # finally, mark secret as discovered
                    currentRoom.secrets[translatedObject] = True
                    # give player points for discovering secret
                    self.engineInstance.player.score += 20  

                # else, if secret has been discovered already...
                else:
                    #print an alternate "discovered this already" version of its description
                    retString = "[altrenate description of secret %s discovered already]" % translatedObject.name
            else:
                retString = "Can't see a %s here." % subject
#-------------------------------------------------------------------------------------------------------------------------
        # The following sections deal with possibilites when subject IS NOT in this Engine instance's nameMap (a dict that maps string/subject to gameObject)
        # These might include general words like "room", "wall", "floor" etc. which should be handled, perhaps via recursion (as is the case with 'wall' or 'tile')

        #3) special examine cases
        #3A) "examine room"
        elif subject == "room":
            # A little debug section
            # if currentRoom.name == "deadEndRoom":
                # debugMsg = "DEBUG1           : (False not in currentRoom.monsters.values()?"
                # debugMsg = "DEBUG1 RESULT    : %s" % (False not in currentRoom.monsters.values())
                # debugMsg = "DEBUG2           : len(currentRoom.monsters)!=0?"
                # debugMsg = "DEBUG2 RESULT    : %s" % (len(currentRoom.monsters)!=0)
                # debugMsg = "DEBUG1B          : (False not in currentRoom.traps.values()?"
                # debugMsg = "DEBUG1B RESULT   : %s" % (False not in currentRoom.traps.values())
                # debugMsg = "DEBUG2B          : len(currentRoom.traps)!=0?"
                # debugMsg = "DEBUG2B RESULT   : %s" % (len(currentRoom.traps)!=0)
                # debugMsg = "DEBUG3           : (False not in currentRoom.secrets.values()?"
                # debugMsg = "DEBUG3 RESULT    : %s" % (False not in currentRoom.secrets.values())
                # debugMsg = "DEBUG4           : len(currentRoom.secrets)!=0?"
                # debugMsg = "DEBUG4 RESULT    : %s" % (len(currentRoom.secrets)!=0)
                # First of all, if room has no threats left, print the alternate description.
                # Else, print the standard description.

            # if every threat/secret has been disabled/discovered,
            # Print an alt description of the room
            # NOTE : I define "every threat/secret being disabled/discovered" here as having no Falses among those dict's values.
            # Also implement a check for non-zero length of the room's monsters/traps/secrets dicts (i.e., make sure the room wasn't free of monsters/trheats/secrets to begin with.)
            if (False not in currentRoom.monsters.values() and len(currentRoom.monsters)!=0) or (False not in currentRoom.traps.values() and len(currentRoom.traps)!=0) or (False not in currentRoom.secrets.values() and len(currentRoom.secrets)!=0):
                debugMsg = "DEBUG : currentroom.name = %s" % currentRoom.name
                self.debug(debugMsg)

                # NOTE :
                # An explicit cast to str is needed here, or retString will be treated as a tuple going forward, preventing concatenation with strings
                debugMsg = "DEBUG : *** ALTERNATE DESC! ***"
                self.debug(debugMsg)
                retString = str(currentRoom.altDescription)

            # else, just the regular description will do
            else:
                debugMsg = "DEBUG : *** REGULAR DESC! ***"
                self.debug(debugMsg)
                debugMsg = "DEBUG : currentroom.name = %s" % currentRoom.name
                self.debug(debugMsg)
                retString = str(currentRoom.description)


            # After that, tack on description strings for the discovery of each secret/resolution of each threat/a general change in an item
            # Loop 1, for secrets :
            for s in currentRoom.secrets:
                #secrets need to have a name attribute (s.name here) for this to work...
                if (currentRoom.secrets[s] == True):
                    #Add a new line reflecting the resolution of this threat/secret to the room description.
                    retString += "\n%r" % self.engineInstance.tackOnSceneDescriptions[s]     

            # Loop 1b, for doors/gates :
            # for s in currentRoom.doors:
            #     if (currentRoom.doors[s] == True):
            #         retString += "\n%r" % self.engineInstance.tackOnSceneDescriptions[s]

            # Loop 2, for monsters (threats) :
            for s in currentRoom.monsters:

                debugMsg = "DEBUG : s.name = %s, disabledStatus = %s" % (s.name, currentRoom.monsters[s])
                self.debug(debugMsg)
                
                if (currentRoom.monsters[s] == True):
                    #Add a new line reflecting the resolution of this threat/secret to the room description.
                    retString += "\n%s" % self.engineInstance.tackOnSceneDescriptions[s]  
            # Loop 2B, for traps (threats) :
            for s in currentRoom.traps:

                debugMsg = "DEBUG : s.name = %s, disabledStatus = %s" % (s.name, currentRoom.traps[s])
                self.debug(debugMsg)
                
                if (currentRoom.traps[s] == True):
                    #Add a new line reflecting the resolution of this threat/secret to the room description.
                    retString += "\n%s" % self.engineInstance.tackOnSceneDescriptions[s]  

            # why was this section commented out??
            # Loop 3, for items:
            for s in currentRoom.items:
                #if item s was NOT picked up i.e. it's still in currentroom.items
                if (currentRoom.items[s] == False) :
                    retString += "\n%s" % self.engineInstance.tackOnSceneDescriptions[s]

#-------------------------------------------------------------------------------------------------------------------------
        # Ugh this is ugly hardcoding. Use dicts defined in Engine.py for resolving 'wall' and 'door' and stuff, THEN do the recursive self.examine call as usual.
        #3B) "examine wall"
        elif subject == "wall":
            if currentRoom == self.engineInstance.deadEndRoom:
                self.examine(currentRoom, "deadEndWall")
            elif currentRoom == self.engineInstance.corridor2:
                self.examine(currentRoom, "brickOutcropping") # call self.examine again, this time with the proper GameObject instance name
            else:
                retString = "generic description of a wall"
#-------------------------------------------------------------------------------------------------------------------------
        #3C) "examine door"
        elif subject == "door":
            if currentRoom == self.engineInstance.startRoom:
                self.examine(currentRoom, "riggedDoor")
            else:
                retString = "generic description of a door"
#-------------------------------------------------------------------------------------------------------------------------
        #BASE CASE) couldnt decipher user's intended examine
        else:
            retString = "I don't know what that is."
#-------------------------------------------------------------------------------------------------------------------------
        #debugMsg = "DEBUG : retString = %s" % retString
        #self.debug(debugMsg)

        # Print the final description string to be printed for "examine x" after all that description-searching and tacking-on.
        print "\t%s" % (retString)
##############################################################################################################
    def get(self, currentRoom, subject):
        """Pick up an object and add it to the player's inventory,
        Provided a) the item is recognizable (exists in EngineInstance's nameMap),
        b) it's in the same room as the player to begin with,
        c) it hasn't been picked up and added to inventory already,
        and d) it is gettable """
        if subject in self.engineInstance.nameMap:
            translatedObject = self.engineInstance.nameMap[subject]
            print "TranslatedObject = %r" % translatedObject.name
            # thing is in the same room as player
            if translatedObject in currentRoom.items:
                # has been obtained already
                if translatedObject in self.engineInstance.player.inventory:
                    print "I already have a %s" % translatedObject.name
                # hasn't been obtained
                else:
                    if translatedObject.isGettable == True:
                        # add object to inventory
                        self.engineInstance.player.inventory.append(translatedObject)
                        # remove it from the room's objects list (mark it as obtained)
                        currentRoom.items[translatedObject] = True
                        print "Picked up the %s" % translatedObject.name
                        # give player points for picking up item
                        self.engineInstance.player.score += 5  
                    else:
                        print "I can't pick up the %s" % translatedObject.name
            # thing not in room
            else:
                print "I don't see a %s here." % translatedObject.name
        # thing not in nameMap, no idea what it is
        else:
            print "I don't know what a %s is" % subject
##############################################################################################################
    def use(self, currentRoom, subject, predicate):
        """use subject with/on predicate
        Checks :
        0) subject and predicate have entries in engineInstance.nameMap
        1) subject is in player inventory
        2) predicate is either in player inventory, or in currentRoom (items or monsters/traps)
        3) subject and predicate together make a valid useable pair 
        """
        # check if both subject and predicate have valid nameMap entries, and retrieve them if so
        if subject in self.engineInstance.nameMap and predicate in self.engineInstance.nameMap:
            translatedSubjectObject     = self.engineInstance.nameMap[subject]
            translatedPredicateObject   = self.engineInstance.nameMap[predicate]

            # debugMsg =  "DEBUG : translatedSubjectObject = %s, translatedPredicateObject = %s" % (translatedSubjectObject.name, translatedPredicateObject.name)
            # self.debug(debugMsg)

            # check if subject and predicate make a valid use pair, as defined in itemUsageEffects dict
            if (translatedSubjectObject,translatedPredicateObject) in self.engineInstance.itemUsageEffects:
                # fetch that effect, if so
                itemUsageEffect = self.engineInstance.itemUsageEffects[(translatedSubjectObject,translatedPredicateObject)]
                # check if subject is in player inventory, and predicate is an item in the room
                if ((translatedSubjectObject in self.engineInstance.player.inventory) and (translatedPredicateObject in currentRoom.monsters or translatedPredicateObject in currentRoom.traps or translatedPredicateObject in currentRoom.items)):                   
                    
                    # Usage #1 = 'Kill'
                    if itemUsageEffect == 'kill':
                        # mark this monster as disabled
                        currentRoom.monsters[translatedPredicateObject] = True
                        print "The %s dies, you've done it!" % translatedPredicateObject.name
                        # give player points for killing monster
                        self.engineInstance.player.score += 20
                        # if boss, 10 more points
                        # if (translatedPredicateObject in list_of_bosses) : self.engineInstance.player.score += 10   

                    # Usage #2 = 'Unlock'
                    elif itemUsageEffect == 'unlock':
                        # add direction this unlocks to the list of exits for currentRoom
                        # this mapping is found in Engine.py, as the leadsTo/leadsFrom dict pair
                        leadsTo = self.engineInstance.leadsTo[translatedPredicateObject]
                        direction = self.engineInstance.leadsFrom[leadsTo]
                        currentRoom.exits[direction] = leadsTo
                        print "You've unlocked it. The way %s is now open." % direction
                        # give player points for correct usage 
                        self.engineInstance.player.score += 3 

                    # other elifs go here, as they're added on to the game later.
                    # TODO 

                    # Usage : BASE CASE = Idklol, maybe the last mapping that wasnt covered by the if/elifs ?
                    else:
                        pass
                # if subject isn't in player inventory, or predicate isn't in the player's current room
                # can add more checks later for better player feedback formatting i.e. which one of the pair is missing
                else:
                    print "I don't know what to do with those."
            # The objects are valid GameObjects, but they don't make a valid use pair
            else:
                print "I can't use those two together."

        # subject or predicate (or both) has no valid nameMap entry; not recognized as valid GameObjects
        else:
            print "I don't know a %s or a %s" % (subject,predicate)

##############################################################################################################    
    def debug(self, message):
        #prints whatever debug message/log message is sent here (adds an overhead due to a function call for each debug message, unfortunately)
        print message
##############################################################################################################  
    def printExits(self, currentRoom):
        """prints exits from this room, invoked by "exits" command by player"""

        print "Exits from this room : "
        for exit in currentRoom.exits:
            print "\t%s" % exit
##############################################################################################################  
    def printInventory(self, engineInstance):
        """prints contents of player inventory, invoked by "inventory" player command"""
        print "Contents of my inventory : "
        for item in engineInstance.player.inventory:
            print "\t%s" % item.name  
##############################################################################################################  
