class Actor(object):
    """An Actor in this game is every animate and inanimate thing.
    Subclasses : PC/NPC/Object
    (Monsters are NPC's)
    """

    def __init__(self):
        self.name           = ""
        self.description    = ""
        self.HP             = 1     # does this mean game objects (key, chests, scroll) can potentially be "killed"/destroyed, if implmented later?
                                    # HP is 1 for everyone that can be killed in one hit; current combat system isn't a fleshed out AD-HP based one. That would be more RPG-ish than I'd like for this text-adventure project right now. 
        self.GP             = 0     # does this mean an Actor (instance of PC/NPC/Object) can potentially drop gold when killed, if implemented later?
        self.inventory      = []    # If NPC's and GameObjects have this too, does this mean monsters and game items (chests, other container types) can drop stuff when killed?
        self.attackDamage   = 1     # PC, NPC, AND GameObjects can attack! Great for traps.
        
class GameCharacter(Actor):
    """Player and non-player characters, aka animate objects. Inherits from Actor.
    """
    def __init__(self):
        super(GameCharacter,self).__init__()
        self.score = 0
        self.isPlural = 0 # all but armies of enemies(e.g an enemy cluster of 3 skeletons) are isPlural = 0

class GameObject(Actor):
    """inanimate objects."""

    def __init__(self):
        super(GameObject, self).__init__()
        self.isGettable = False