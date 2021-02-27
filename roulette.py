import arguments
import roulettegame

if len(arguments.args) == 1:
  if arguments.args[0] == "biased":
    roulettegame.biased = True
arguments.messageReturn = roulettegame.rouletteGame.SendWelcome()