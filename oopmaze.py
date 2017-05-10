import Engine
import Game

mazeEngineInstance = Engine.Engine() #  send over an instance of our Engine class which sets up the game's skeleton (internal data structures)

#Start it off!
mazeGameInstance = Game.Game(mazeEngineInstance)

