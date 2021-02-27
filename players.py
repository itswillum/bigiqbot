import arguments
import roulettegame

if roulettegame.welcome == True and roulettegame.players == False:
  arguments.messageReturn = roulettegame.rouletteGame.personPick(arguments.args)
else:
  arguments.messageReturn = "No roulette game has started"