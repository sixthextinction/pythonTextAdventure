class Scene(object):
    """
    Rooms and score/death screens
    """

    def __init__(self):
        self.description        = ""
        self.altDescription     = ""
        self.name               = ""

class Room(Scene):
    def __init__(self):
        """Some terminology, first.
        "monstersAndThreats" are NPCs and GameObjects which can kill the player if not disabled in some way (kill/disarm)
        "secrets" are GameObjects which don't kill the player, but can be examind to change the room in some way (just secret passages for now)
        "items" are GameObjects which are neither of the above. (exitKey, guardianScroll, treasureChest)
        """
        super(Room, self).__init__()
        self.treasureAmount     = 0  
        self.monsters           = {} #threatName (GameObject/GameCharacter instance)    :   bool_disabled (Boolean)
        self.traps              = {} #threatName (GameObject/GameCharacter instance)    :   bool_disabled (Boolean)
        self.secrets            = {} #secretName (GameObject instance)                  :   bool_discovered (Boolean)
        self.exits              = {} #exitName   (string)                               :   roomName (Room/Screen instance)
        self.items              = {} #itemName   (GameObject instance)                  :   bool_obtained/bool_limited_interactions_over(meaning treasureChests, basically) (Boolean) 
class Screen(Scene):
    def __init__(self):
        super(Screen, self).__init__()
        self.reason             = "" #wtf is this for?
