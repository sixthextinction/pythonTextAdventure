#============================================================================================================================================================================
class Scene(object):
    """
    Rooms and score/death screens
    """

    def __init__(self):
        self.description        = ""
        self.name               = ""

class Room(Scene):
    def __init__(self):
        self.hasTreasure        = False
        self.treasureAmount     = 0  
        self.monstersAndThreats = {} #threatName    :   bool_disabled
        self.secrets            = {} #secretName    :   bool_discovered
        self.exits              = {} #exitName      :   roomName
        self.items              = {} #itemName      :   bool_obtained/bool_limited_interactions_over (basically I mean treasure chests with the latter)

class Screen(Scene):
    def __init__(self):
        self.reason             = ""

#============================================================================================================================================================================
class Engine(object):
    """
    # Should create instances of each Scene (rooms, screens) and Actor (player, monsters, items)
    # Should create each Scene instance as they're entered into, or all at the start?
    # Primary method here : core_game_loop()
    """

    def __init__(self):
        self.createAllScenes()                  #class : Room/Screen
        self.addAllSceneDescriptions()          #class : Room/Screen
        self.addAllTreasures()                  #class : Room

        self.createAllItems()                   #class : Actor
        self.addAllItemDescriptions()           #class : Actor
        self.addAllItems()                      #class : Room

        self.createAllCharacters()              #class : Actor
        self.addAllCharacterDescriptions()      #class : Actor

        self.addAllThreats()                    #class : Room
        self.addAllSecrets()                    #class : Room
        self.addAllExits()                      #class : Room

    def start(self):
        self.core_game_loop(self.startRoom) #pass startRoom as currentRoom to start things off

    def core_game_loop(self, currentRoom):
        #stuff to test if this works
        print "currentRoom NAME             : %s"           %   currentRoom.name
        print "currentRoom DESCRIPTION      : %s"           %   currentRoom.description
        print "currentRoom TREASURES        : %s"           %   currentRoom.hasTreasure
        print "currentRoom ITEMS            : %s"           %   currentRoom.items
        print "currentRoom MONSTERS_THREATS : %s"           %   currentRoom.monstersAndThreats
        print "currentRoom SECRETS          : %s"           %   currentRoom.secrets
        print "currentRoom EXITS            : %s"           %   currentRoom.exits

        print "\n DEBUG : Enter directions to go to that room, 'exit' to end test.\n"
        playerChoice = ""
        nextRoom = ""
        while (playerChoice != "exit"):
            playerChoice = raw_input("> ")
            nextRoom = currentRoom.exits[playerChoice]
            self.core_game_loop(nextRoom)

    def createAllScenes(self):
        """
        Create instances (each room, each screen) for Room and Screen classes (children classes of Scene)
        """

        #Rooms
        self.startRoom          = Room()
        self.startRoom.name     = "startRoom"
        self.trapRoom           = Room()
        self.trapRoom.name      = "startRoom"
        self.deadEndRoom        = Room()
        self.deadEndRoom.name   = "deadEndRoom"
        self.corridor0          = Room()
        self.corridor0.name     = "corridor0"
        self.corridor1          = Room()
        self.corridor1.name     = "corridor1"
        self.corridor2          = Room()
        self.corridor2.name     = "corridor2"
        self.corridor3          = Room()
        self.corridor3.name     = "corridor3"
        self.corridor4          = Room()
        self.corridor4.name     = "corridor4"
        self.corridor5          = Room()
        self.corridor5.name     = "corridor5"
        self.corridor6          = Room()
        self.corridor6.name     = "corridor6"
        self.treasureRoom       = Room()
        self.treasureRoom.name  = "treasureRoom"
        #Screens
        self.deathScreen        = Screen()
        self.deathScreen.name   = "deathScreen"
        self.victoryScreen      = Screen()
        self.victoryScreen.name = "victoryScreen"
        self.scoreScreen        = Screen()
        self.scoreScreen.name   = "scoreScreen"
        
    def addAllSceneDescriptions(self):
        """
        Add the description attribute to all Room and Screen instances.
        """

        #Rooms 
        self.startRoom.description      = """
                                            Smooth, slippery stone. Superior, if spartan.
                                            Dust and cobwebs populate this room. 
                                            This place is ancient. No one has either ventured down here for years, or escaped to tell the tale.
                                            There is no sound. Each footstep is a crack of thunder in this barren place.
                                            Each clink of your armor a beacon for the denizens that dwell here.

                                            There's a suspiciously pristine door to the right of you, the east, 
                                            While a rusty, dilapidated metal gate covers another entrance on the other side of the room to the northwest.
                                            """

        self.trapRoom.description      = """
                                            Dark. No sconces. No magelight. The darkness here is thick and suffocating. A different animal altogether. It's an oily ooze, pervading in the air.
                                            Clattering of bones and metal.
                                            This was a trap.
                                            You curse, throwing your lantern on the floor and whipping around.
                                            Three skeletons. Undead protectors of some long-forgotten master. Their swords are curved. 

                                            The door behind you is barred, through sorcery or otherwise, you could not care less. No escape that way.
                                            There is an exit to the northeast, if you can make it there.
                                            """

        self.deadEndRoom.description   = """
                                            Dead end. 

                                            Or is it nearly as grim? There's a draft coming from the south. From...solid wall?
                                            """

        self.corridor0.description   =      """
                                            Your first inroads into the Dungeon have yielded this corridor. The coast is clear.
                                            The architecture here echoes that of the first room, and you suspect this is how it is the rest of the way, too.

                                            An arch provides an exit to the south. 
                                            """

        self.corridor1.description   =      """
                                            This is a long, long corridor. A solitary sconce with an orb of light provides illumination about halfway down.
                                            Curiously, the architecture here is slightly different. The floor here is comprised of many single, large, rectangular slabs instead of smooth stone.

                                            You can barely make out an exit to the west in the tired, jaundiced glow. The corridor continues.
                                            """

        self.corridor2.description   =      """
                                            The unbroken, smooth stone floor is back, and you sigh in relief. You peer around carefully, but there are no enemies in sight.
                                            This seems an exceptionally ordinary room. The wall to your left has a brick outcropping, but that's to be expected in some place as old as this, right? 

                                            There seems to be nothing here but another sconce lighting the way round a corner; another corridor to the northwest.
                                            """

        self.corridor3.description   =      """
                                            Another long, boring corridor. 

                                            You see a rusty, foreboding metal gate to the southeast. 

                                            There's a dusty old scroll lying about in an alcove here.
                                            """
                                            
        self.corridor4.description   =      """
                                            Yet another corridor. You're finally begin to appreciate the architectural genius of this place. You're now certain of how easy it is to get lost here, roaming forever.
                                            Good thing you have a map. You do have a map, right?
                                            Your thoughts are interruted by guttural, inhuman moaning echoing down the stone halls. Flickering shadows on the walls ahead. Bad news.

                                            Whatever it is, it lies to the east. 
                                            """
                                            
        self.corridor5.description   =      """
                                            The shambling corpse walks towards you.

                                            There's a low ceilinged hallway to the south. 
                                            """
        self.corridor6.description   =      """
                                            You can't believe your eyes. Daylight to the west. Filtering in through the widest gate you've seen here so far.
                                            These halls are wider than any other in this place. You check around for danger, but there seems to be none apparent.
                                            Home stretch.

                                            Your ticket out of here is to the west, though your attention is drawn to another diagonal tunnel to the northwest. An evil permeates that tunnel. 
                                            """

        self.treasureRoom.description   =      """
                                            The Guardian stands here in this bloody room, among bones and discarded gear of heroes past, a dozen arms tall, metal plates intertwining with chains, dirty leather hood hiding his grotesque visage.
                                            He has been waiting for you. He grins, bare, bloody teeth and all, as he picks up his greatsword. 
                                            A key hangs from a hook on the wall behind him.

                                            Are you prepared? There is no exit except back out, southeast, should you want to regroup. 
                                            """   

        #Screens                   
        self.deathScreen.description    = "YOU DIED."
        self.victoryScreen.description  = "YOU WIN!"
        self.scoreScreen.description    = "YOUR SCORE : "
        
    def addAllTreasures(self):
        """
        Add the treasure attribute to all Room instances.
        """

        #only need to specify rooms with treasure here
        self.corridor0.hasTreasure          = True
        self.corridor0.treasureAmount       = 25
        self.corridor4.hasTreasure          = True
        self.corridor4.hasTreasure          = 70
        self.corridor6.hasTreasure          = True
        self.corridor6.hasTreasure          = 60
        self.treasureRoom.hasTreasure       = True
        self.treasureRoom.hasTreasure       = 200

    def createAllItems(self):
        """
        Create instances (each item) of GameObject class (which is a child class of Actor)
        """

        #GameObjects that are gettable 
        self.guardianScroll             =   GameObject()
        self.guardianScroll.isGettable  =   True
        self.exitKey                    =   GameObject()
        self.exitKey.isGettable         =   True
        #GameObjects that are threats
        self.suspiciousDoor             =   GameObject()
        self.suspiciousTile             =   GameObject()
        #GameObjects that are secrets
        self.deadEndRoomSouthWall       =   GameObject()
        self.corridor2WestWall          =   GameObject()
        #GameObjects that can be interacted with (examine, open, etc?)
        self.corridor0treasureChest     =   GameObject()
        self.corridor4treasureChest     =   GameObject()
        self.corridor6treasureChest     =   GameObject()
        self.treasureRoomtreasureChest  =   GameObject()

    def addAllItemDescriptions(self):
        """
        Add description attribute to each GameObject instance
        """

        #GameObjects that are gettable 
        self.guardianScroll.description = "Dusty, yellowed parchment rolled into a scroll, shimmering arcane letters. This kills the guardian when recited."
        self.exitKey.description        = "The key to your freedom hangs there, glittering in the magelight, as it has for the past few hundred years. Is there a way to get to it, dodging the Guardian?"
        #GameObjects that are threats
        self.suspiciousDoor.description = """
                                            You peer at the door, and notice nothing different. You start to give it a gentle push...
                                            ...and immediately shrink back.
                                            That was a close one. There's a hair trigger of a wire connecting the edge to some invisible apparatus inside the wall.
                                            You judiciously cut the wire, and jump as there is a tiny, but piercing, clink from above.
                                            Whatever you have done, seems to have defused the trap.
                                            """
        self.suspiciousTile.description = "Your perceptive nature pays off, as you realize the unnatural tile architecture hides a pressure trap. You disarm it. Close shave."
        #GameObjects that are secrets
        self.deadEndRoomSouthWall       = "You push the south wall, and it falls over almost comically. Huh. Being that perceptive paid off, looks like. You can step through into a new corridor to the south."
        self.corridor2WestWall          = "You run your hand across the outcropping, and discover one of the bricks is loose! Pulling on it reveals a secret passage to the west!"
        #GameObjects that can be interacted with (examine, open, etc?)
        self.treasureChest              = "Just your everyday oversized wood-and-metal chest. You can open this up, looks like."

    def addAllItems(self):
        """Add interactive items(GameObject instances) that are NOT threats AND NOT secrets in each room"""

        #only interactive (treasure chests, or other containers to be added later)
        self.corridor0.items =      {
                                    self.corridor0treasureChest     :   False
                                    }
        self.corridor4.items =      {
                                    self.corridor4treasureChest     :   False
                                    }
        self.corridor6.items =      {
                                    self.corridor6treasureChest     :   False
                                    }
        self.treasureRoom.items =   {
                                    self.treasureRoomtreasureChest  :   False
                                    }
        #gettable
        self.corridor3.items =      {
                                    self.guardianScroll             :   False
                                    } 
        self.treasureRoom.items =   {
                                    self.exitKey                    :   False
                                    } 

    def createAllCharacters(self):
        """create instances of PC/NPC classes, which are both subclasses of Actor
        Right now, any character with HP > 1 cant be killed in one hit. Keep in mind when adding characters later.
        """ 

        #PC
        self.player             =   PC()
        #NPC
        self.skeletons          =   NPC()
        self.skeletons.HP       =   3 #purely arbitrary. Why not, there are 3 skeletons. 
        self.zombie             =   NPC()
        self.guardianBoss       =   NPC()
        self.guardianBoss.HP    =   1000 #purely arbitrary 

    def addAllCharacterDescriptions(self):
        """assign description attribute to all PC/NPC class instances"""

        #PC
        #self.player.description     =   "You."  
        #NPC
        self.zombie.description         = "Ghastly un-life stares back at you through maggot infested eyesockets. A mass of rotten flesh, loose coils of intestine, and jagged teeth, shambling towards you, inch by fatal inch. "
        self.skeletons.description      = "Reanimated soldiers, moldy bones held together by some unholy magic. They carry curved swords, and the red misty glow in their otherwise empty orbits, hungers for your blood." 
        self.guardianBoss.description   = "A towering mound of interlocking black metal plates and the biggest greatsword you've ever seen (har har). You can make out a hint of his black eyes and slathering fangs under that leather hood, pulled down low."                                                                                                    

    def addAllThreats(self):
        """Add the PC/NPC instances to each Room instance
        Needless to say, monsters will be from NPC instances and threats from GameObject ones"""

        #reminder : format for the dict here is threatName : disabledStatus
        self.startRoom.monstersAndThreats       =   {
                                                self.suspiciousDoor         :   False
                                                    }
        self.trapRoom.monstersAndThreats        =   {
                                                self.skeletons              :   False
                                                    }
        self.corridor1.monstersAndThreats       =   {
                                                self.suspiciousTile         :   False
                                                    }
        self.corridor5.monstersAndThreats       =   {
                                                self.zombie                 :   False
                                                    }
        self.treasureRoom.monstersAndThreats    =   {
                                                self.guardianBoss           :   False
                                                    }

    def addAllSecrets(self):
        """Add all secrets (instances of GameObject) to each Room instance"""

        #reminder : format for the dict here is secretName : discoveredStatus
        self.deadEndRoom.secrets        =       {   self.deadEndRoomSouthWall   :   False   }
        self.corridor2.secrets          =       {   self.corridor2WestWall      :   False   }

    def addAllExits(self):
        """add all exits to and from Room instances"""

        self.startRoom.exits    =   {   "east"      :   self.corridor0, 
                                        "northwest" :   self.trapRoom   
                                    }
        self.trapRoom.exits     =   {   "northeast" :   self.deadEndRoom    
                                    }
        self.deadEndRoom.exits  =   {   "south"     :   self.corridor0     
                                    }
        self.corridor0.exits    =   {   "north"     :   self.deadEndRoom, 
                                        "west"      :   self.startRoom, 
                                        "south"     :   self.corridor1 
                                    }
        self.corridor1.exits    =   {   "west"      :   self.corridor2, 
                                        "east"      :   self.corridor0  
                                    }
        self.corridor2.exits    =   {   "northwest" :   self.corridor3, 
                                        "west"      :   self.corridor4, 
                                        "east"      :   self.corridor1
                                    }
        self.corridor3.exits    =   {   "northeast" :   self.corridor2
                                    }
        self.corridor4.exits    =   {   "north"     :   self.corridor2,
                                        "east"      :   self.corridor5
                                    }
        self.corridor5.exits    =   {   "west"      :   self.corridor4,
                                        "south"     :   self.corridor6
                                    }
        self.corridor6.exits    =   {   "west"      :   self.victoryScreen,
                                        "northwest" :   self.treasureRoom
                                    }
        self.treasureRoom       =   {   "southeast" :   self.corridor6
                                    }
#============================================================================================================================================================================
class Actor(object):
    """An Actor in this game is every animate and inanimate thing.
    Subclasses : PC/NPC/Object
    (Monsters are NPC's)
    """

    def __init__(self):
        self.description = ""
        self.HP = 1 #does this mean game objects (key, chests, scroll) can potentially be "killed"/destroyed, if implmented later?
                    #HP is 1 for everyone that can be killed in one hit; current combat system isn't a fleshed out AD-HP based one. That would be more RPG-ish than I'd like for this text-adventure project right now. 
        self.GP = 0 #does this mean an Actor (instance of PC/NPC/Object) can potentially drop gold when killed, if implemented later?
        
class PC(Actor):
    """Player character, inherits from Actor.
    """

    def __init__(self):
        self.inventory = {} #If NPC's have this too, does this mean both PC and monsters can drop stuff when killed?
        self.attackDamage = 1

class NPC(Actor):
    """Non player character, inherits from Actor
    Basically just monsters here for now."""

    def __init__(self):
        self.attackDamage = 1

class GameObject(Actor):
    """inanimate objects."""

    def __init__(self):
        self.isGettable = False
#============================================================================================================================================================================
#Start it off!
mazeGameEngine = Engine()
mazeGameEngine.start()