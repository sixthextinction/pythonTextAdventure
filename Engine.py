import Scene
import Actor

class Engine(object):
    """
    # Should create instances of each Scene (rooms, screens) and Actor (player, monsters, items)
    # Should create each Scene instance as they're entered into, or all at the start?
    """
#################################################f#############################################################
    def __init__(self):
        self.nameMap = {}                       # dict that maps common names to objects for everything in the game (GameCharacters and GameObjects both)
        self.tackOnSceneDescriptions = {}       # dict specifiying what strings to tack onto room descs as an item in it is discovered/changed. format of this dict = secretName : <str>
        self.leadsTo = {}                       # dict that maps secret (GameObject) : room (Room)
        self.leadsFrom = {}                     # dict that maps room (Room) : direction (string)
        self.itemUsageEffects = {}              # dict with a 2-tuple as key. Maps items used together to an effect
        self.directionalThreats = {}            # dict with a 2-tuple as key. Maps direction/starting room pair to a trap that makes going in that direction from that room a threat
        self.escapableRooms = []          # list of rooms that allow movement to other rooms even with monsters present

        self.createAllScenes()                  # create all Room/Scene instances 
        self.addAllSceneDescriptions()          # add the description attribute to the above instances
        self.addAllSceneAltDescriptions()       # add the altDescription attribute to the above instances

        self.createAllGameObjects()             # create all GameObject instances
        self.addAllGameObjectDescriptions()     # add the description attribute to the above instances

        self.createAllCharacters()              # create all GameCharacter instances
        self.addAllCharacterDescriptions()      # add the description attribute to the above instances

        self.addAllItems()                      # adds GameObject instances that are NOT threats/secrets/exits (i.e, the gettable objects like keys/scrolls, and treasureChests) (aka items) as members of the items dict attribute of Room instances.
        self.addAllTreasures()                  # assigns integer value to treasureAmount attribute of Room instances(i.e. sets the amount of treasure in each room. 0 value = no treasure chest in room ) 
        self.addAllThreats()                    # adds GameCharacter instances (specifically, monsters/traps) as members of the monsters or traps dict attribute of Room instances.
        self.addAllSecrets()                    # adds GameObject instances (specifically, hidden walls/passages) (aka secrets) as members of the secrets dict attribute of Room instances.
        self.addAllExits()                      # adds directionString : Room/Scene instance key-value pairs (i.e. exits from a room and to which room they lead) to the exits dict attribute of Room instances 
        
        self.createNameMap()                    # create the aforementioned nameMap
        self.createTackOnSceneDescriptions()    # create the aforementioned tackOnSceneDescriptions
        self.createLeadsTo()                    # create the aforementioned leadsTo dict
        self.createLeadsFrom()                  # create the aforementioned leadsFrom dict
        self.createItemUsageEffects()           # create the aforementioned itemUsageEffects dict
        self.createDirectionalThreats()         # create the aforementioned directionalThreats dict
        self.createEscapableRooms()             # create the aforementioned listOfEscapableRooms list
        # self.start()   
##############################################################################################################
    def createAllScenes(self):
        """
        Create instances (each room, each screen) for Room and Screen classes (children classes of Scene)
        """

        #Rooms
        self.startRoom          = Scene.Room()
        self.startRoom.name     = "startRoom"
        self.trapRoom           = Scene.Room()
        self.trapRoom.name      = "startRoom"
        self.deadEndRoom        = Scene.Room()
        self.deadEndRoom.name   = "deadEndRoom"
        self.corridor0          = Scene.Room()
        self.corridor0.name     = "corridor0"
        self.corridor1          = Scene.Room()
        self.corridor1.name     = "corridor1"
        self.corridor2          = Scene.Room()
        self.corridor2.name     = "corridor2"
        self.corridor3          = Scene.Room()
        self.corridor3.name     = "corridor3"
        self.corridor4          = Scene.Room()
        self.corridor4.name     = "corridor4"
        self.corridor5          = Scene.Room()
        self.corridor5.name     = "corridor5"
        self.corridor6          = Scene.Room()
        self.corridor6.name     = "corridor6"
        self.treasureRoom       = Scene.Room()
        self.treasureRoom.name  = "treasureRoom"
        #Screens
        self.deathScreen        = Scene.Screen()
        self.deathScreen.name   = "deathScreen"
        self.victoryScreen      = Scene.Screen()
        self.victoryScreen.name = "victoryScreen"
##############################################################################################################   
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
##############################################################################################################
    def addAllSceneAltDescriptions(self):
        """Alt descriptions = descriptons of rooms that are used instead of the actual description, when some conditions are met"""

        self.corridor4.altDescription   =      """
                                            Yet another corridor. You're finally begin to appreciate the architectural genius of this place. You're now certain of how easy it is to get lost here, roaming forever.
                                            Good thing you have a map. You do have a map, right?
                                                
                                            The corridor continues to the east.
                                            """
                                            
        self.corridor5.altDescription   =      """
                                            Yet another corridor.

                                            There's a low ceilinged hallway to the south. 
                                            """
        self.corridor6.altDescription   =      """
                                            Still daylight to the west. Beyond that huge gate.
                                            These halls are wider than any other in this place. You check around for danger, but there seems to be none apparent.
                                            Home stretch.

                                            Your ticket out of here is to the west. 
                                            """

        self.deadEndRoom.altDescription   = """
                                            You once thought this was a dead end room. Spotting the draft was a nice bit of perceptiveness.
                                            """
        self.corridor2.altDescription     = """
                                            The wall to the west fell over, the secret passage stands ready for your traversal.
                                            """
        #mentions of the key should be in tackOn descriptions, based on if its present in room or not.
        self.treasureRoom.altDescription   =      """
                                            The Guardian's room now stands empty.

                                            The exit is back out to the southeast. 
                                            """ 
        
##############################################################################################################        
    def addAllTreasures(self):
        """
        Add the treasure attribute to all Room instances.
        """

        #only need to specify rooms with treasure here
        #self.corridor0.treasure                 = True #dont need this. Bloat. Also, checking a room for treasure is ALREADY done by checking for presence of a chest
        self.corridor0.treasureAmount           = 25

        self.corridor4.treasureAmount           = 70
  
        self.corridor6.treasureAmount           = 60

        self.treasureRoom.treasureAmount        = 200
##############################################################################################################
    def createAllGameObjects(self): 
        """
        Create instances (each item) of GameObject class (which is a child class of Actor)
        """

        #GameObjects that are gettable 
        self.guardianScroll             =   Actor.GameObject()
        self.guardianScroll.name        =   "T'Shal Scroll"
        self.guardianScroll.isGettable  =   True

        self.exitKey                    =   Actor.GameObject()
        self.exitKey.name               =   "Large Gate Key"
        self.exitKey.isGettable         =   True
        #GameObjects that are threats
        self.suspiciousDoor             =   Actor.GameObject()
        self.suspiciousDoor.name        =   "Suspicious Door"

        self.suspiciousTile             =   Actor.GameObject()
        self.suspiciousTile.name        =   "Suspicious Tile"
        #GameObjects that are secrets
        self.deadEndRoomSouthWall       =   Actor.GameObject()
        self.deadEndRoomSouthWall.name  =   "South Wall"

        self.corridor2WestWall          =   Actor.GameObject()
        self.corridor2WestWall.name     =   "West Wall"
        #GameObjects that can be interacted with (open, etc?)
        self.treasureChest              =   Actor.GameObject()
        self.treasureChest.name         =   "Treasure Chest"
        #unlockable doors/gates go here too
        self.exitGate                   =   Actor.GameObject()
        self.exitGate.name              =   "Large Gate"
##############################################################################################################
    def addAllGameObjectDescriptions(self): 
        """
        Add description attribute to each GameObject instance
        """

        #GameObjects that are gettable 
        self.guardianScroll.description             = "Dusty, yellowed parchment rolled into a scroll, shimmering arcane letters. This kills the guardian when recited."
        self.exitKey.description                    = "The key to your freedom, glittering in the magelight."
        #GameObjects that are threats
        self.suspiciousDoor.description             = """
                                                         You peer at the door, and notice nothing different. You start to give it a gentle push...
                                                         ...and immediately shrink back.
                                                         That was a close one. There's a hair trigger of a wire connecting the edge to some invisible apparatus inside the wall.
                                                         You judiciously cut the wire, and jump as there is a tiny, but piercing, clink from above.
                                                         Whatever you have done, seems to have defused the trap.
                                                         """
        self.suspiciousTile.description             = "Your perceptive nature pays off, as you realize the unnatural tile architecture hides a pressure trap. You disarm it. Close shave."
        #GameObjects that are secrets
        self.deadEndRoomSouthWall.description       = "You push the south wall, and it falls over almost comically. Huh. Being that perceptive paid off, looks like. You can step through into a new corridor to the south."
        self.corridor2WestWall.description          = "You run your hand across the outcropping, and discover one of the bricks is loose! Pulling on it reveals a secret passage to the west!"
        #GameObjects that can be interacted with
        self.treasureChest.description     = "Just your everyday oversized wood-and-metal chest. You can open this up, looks like."
        self.exitGate.description           = "Rusty metal gate, huge lock on the front. You hope its metal intestines haven't given out. You'll be in the rather precarious position of slow starvation if you can't unlock it."
##############################################################################################################
    def addAllItems(self):
        """Add interactive items(GameObject instances) that are NOT threats AND NOT secrets in each room"""

        #containers
        self.corridor0.items =      {
                                    self.treasureChest              :   False
                                    }
        self.corridor4.items =      {
                                    self.treasureChest              :   False
                                    }
        self.corridor6.items =      {
                                    self.treasureChest              :   False
                                    }
        self.treasureRoom.items =   {
                                    self.treasureChest              :   False
                                    }
        #doors/gates
        self.corridor6.items =      {
                                    self.exitGate                   :   False#?
                                    }
        #gettable
        self.corridor3.items =      {
                                    self.guardianScroll             :   False
                                    } 

        self.treasureRoom.items =   {
                                    self.exitKey                    :   False
                                    }
        # self.treasureRoom.items[self.exitKey] = False   #bonus : syntax for append 
##############################################################################################################                                  
    def createAllCharacters(self):
        """create instances (PC, NPC's) of Character class, which is a subclass of Actor
        Right now, any character with HP > 1 cant be killed in one hit. Keep in mind when adding characters later.
        """ 

        #PC
        self.player             =   Actor.GameCharacter()
        self.player.name        =   "player"

        #NPC
        self.skeletons          =   Actor.GameCharacter()
        self.skeletons.name     =   "Guardian Skeletons"
        self.skeletons.HP       =   3 # purely arbitrary. Why not, there are 3 skeletons.
        self.skeletons.isPlural =   1 # 3 in one cluster 

        self.zombie             =   Actor.GameCharacter()
        self.zombie.name        =   "Zombie"

        self.guardianBoss       =   Actor.GameCharacter()
        self.guardianBoss.name  =   "Guardian"
        self.guardianBoss.HP    =   1000 #purely arbitrary 
##############################################################################################################
    def addAllCharacterDescriptions(self):
        """assign description attribute to all PC/NPC class instances"""

        #PC
        self.player.description         =   "You."  
        #NPC
        self.zombie.description         = "Ghastly un-life stares back at you through maggot infested eyesockets. A mass of rotten flesh, loose coils of intestine, and jagged teeth, shambling towards you, inch by fatal inch. "
        self.skeletons.description      = "Reanimated soldiers, moldy bones held together by some unholy magic. They carry curved swords, and the red misty glow in their otherwise empty orbits, hungers for your blood." 
        self.guardianBoss.description   = "A towering mound of interlocking black metal plates and the biggest greatsword you've ever seen (har har). You can make out a hint of his black eyes and slathering fangs under that leather hood, pulled down low."                                                                                                    
##############################################################################################################
    def addAllThreats(self):
        """Add the PC/NPC instances to each Room instance
        Needless to say, monsters will be from NPC instances and threats from GameObject ones"""

        #reminder : format for the dict here is threatName : disabledStatus
        self.startRoom.traps                    =   {
                                                self.suspiciousDoor         :   False
                                                    }
        self.trapRoom.monsters                  =   {
                                                self.skeletons              :   False
                                                    }
        self.corridor1.traps                    =   {
                                                self.suspiciousTile         :   False
                                                    }
        self.corridor5.monsters                 =   {
                                                self.zombie                 :   False
                                                    }
        self.treasureRoom.monsters              =   {
                                                self.guardianBoss           :   False
                                                    }
##############################################################################################################
    def addAllSecrets(self):
        """Add all secrets (instances of GameObject) to each Room instance"""

        #reminder : format for the dict here is gameObject (that happens to be a secret) : discoveredStatus
        self.deadEndRoom.secrets        =       {   self.deadEndRoomSouthWall   :   False   }
        self.corridor2.secrets          =       {   self.corridor2WestWall      :   False   }
##############################################################################################################
    def createLeadsTo(self):
        """Creates dict for which secret/unlockable passage lead to which rooms, when discovered"""

        self.leadsTo = { 
                        self.deadEndRoomSouthWall       :       self.corridor0,
                        self.corridor2WestWall          :       self.corridor4,
                        self.exitGate                   :       self.victoryScreen
                        }
##############################################################################################################
    def createLeadsFrom(self):
        """Creates dict for which directions are to be added to the room's exits list when a secret is discovered/door is unlocked"""

        self.leadsFrom = { 
                        self.corridor0                  :       "south",
                        self.corridor4                  :       "west",
                        self.victoryScreen              :       "west"
                        }
##############################################################################################################
    def addAllExits(self):
        """add all exits to and from Room instances"""
        """ Commented out lines indicate secrets that must be examined to add them to the room's exits list """

        self.startRoom.exits    =   {   "east"      :   self.corridor0, 
                                        "northwest" :   self.trapRoom   
                                    }
        self.trapRoom.exits     =   {   "northeast" :   self.deadEndRoom    
                                    }
        self.deadEndRoom.exits  =   {   #"south"     :   self.corridor0     
                                    }
        self.corridor0.exits    =   {   "north"     :   self.deadEndRoom, 
                                        "west"      :   self.startRoom, 
                                        "south"     :   self.corridor1 
                                    }
        self.corridor1.exits    =   {   "west"      :   self.corridor2, 
                                        "east"      :   self.corridor0  
                                    }
        self.corridor2.exits    =   {   "northwest" :   self.corridor3, 
                                        #"west"      :   self.corridor4, 
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
        self.corridor6.exits    =   {   #"west"      :   self.victoryScreen,
                                        "northwest" :   self.treasureRoom,
                                        "east"      :   self.corridor5
                                    }
        self.treasureRoom.exits =   {   "southeast" :   self.corridor6
                                    }
##############################################################################################################
    def createTackOnSceneDescriptions(self):
        """strings tacked on at the end of "examine room" playerChoice if certain conditions are met"""

        self.tackOnSceneDescriptions = {
        # Format = Name of thing discovered/changed             :       str to tack on
        # These will be tacked on only when there's a discovery of this secret/disabling of this threat (i.e currentroom.items[this secret/trap/monster] == True)
        # secrets
        self.deadEndRoomSouthWall   :  "The wall has fallen over, and a mostly-clear passage to the south lies in front of you.",
        self.corridor2WestWall      :  "The brick wall hiding a secret passage was a nice touch, but you were too smart for it. Good job. A path to the west greets you.",
        # traps
        self.suspiciousDoor         :  "Quite perceptive of you to discover the rigged door. Giving yourself a pat on the back, you now look at a safe door leading east.",
        self.suspiciousTile         :  "You know which perilous tile to skip over now, the way west is safe.",
        # monsters
        self.zombie                 :   "The zombie lies here, now quite dead. For good, you nervously add, internally.",
        self.guardianBoss           :   "All that remains of the Guardian is a few flakes of ash.",
        
        # These will be tacked on only when they've NOT been picked up/been interacted with (i.e. currentroom.items[this item] == False)
        # items
        self.exitKey                :   "There's a glittering key hanging by a hook on the wall opposite you.",
        self.guardianScroll         :   "There's a dusty old scroll lying in an alcove here, on a tablet with inscriptions.",
        self.treasureChest          :   "There's a treasure chest lying about here.",
        self.exitGate               :   "The rusty iron gate with its even rustier lock still sits there, menacing, yet inviting, considering the daylight wafting in behind."
        }
##############################################################################################################
    def createNameMap(self):
        #not happy with this. 
        #maybe implement auto generation in the future?

        self.nameMap = {
        #proper
        "scroll"            :   self.guardianScroll,
        "key"               :   self.exitKey,
        "tile"              :   self.suspiciousTile,
        "tiles"             :   self.suspiciousTile,
        "chest"             :   self.treasureChest,
        "treasure"          :   self.treasureChest,
        "skeleton"          :   self.skeletons,
        "skeletons"         :   self.skeletons,
        "zombie"            :   self.zombie,
        "boss"              :   self.guardianBoss,
        "guardian"          :   self.guardianBoss,
        #custom
        "deadEndWall"       :   self.deadEndRoomSouthWall,
        "brickOutcropping"  :   self.corridor2WestWall,
        "riggedDoor"        :   self.suspiciousDoor,
        "gate"              :   self.exitGate
        }
##############################################################################################################
    def createItemUsageEffects(self):
        # NOTE: in this dict, keys = the name attribute of GameObject instances
        # maps an item pair to the effect it produces when used together.
        # e.g. key, door = unlock

        self.itemUsageEffects = {
        #('guardianScroll','guardianBoss') : 'kill'
        (self.guardianScroll, self.guardianBoss)              : 'kill',
        (self.exitKey, self.exitGate)                         : 'unlock'
        }
##############################################################################################################
    def createDirectionalThreats(self):
        # NOTE: in this dict, keys = the name attribute of GameObject instances
        # maps a direction/starting room pair to the threat that makes going  towards that direction from that starting room a threat
        # e.g. east, startRoom = suspiciousDoor
        self.directionalThreats = {

        ("east", self.startRoom)                                :   self.suspiciousDoor,
        ("west", self.corridor1)                                :   self.suspiciousTile

        }
##############################################################################################################
    def createEscapableRooms(self):
        self.escapableRooms = [
            self.trapRoom
        ]
##############################################################################################################
   