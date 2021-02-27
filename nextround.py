import arguments
import roulettegame

danielVariations = ["Daniel", "daniel", "danal", "Danal", "danel", "Danel"] 

def checkforDaniel(table):
  global roulettegame
  global danielVariations
  for mabyedaniel in roulettegame.playerList:
    if mabyedaniel in danielVariations:
      return [danielVariations.index(mabyedaniel), "true"]
      break
    return ["false", "false"]

if roulettegame.players == True:
  if roulettegame.biased == True and checkforDaniel(roulettegame.playerList)[1] == "true":
    arguments.messageReturn = roulettegame.rouletteGame.killdaniel(checkforDaniel(roulettegame.playerList)[0])
  else:
    arguments.messageReturn = roulettegame.rouletteGame.kill()
else:
  arguments.messageReturn = "You need to start a roulette game"


  



