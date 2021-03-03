from commands import arguments
from commands import roulettegame
import discord
import bot 

danielVariations = ["Daniel", "daniel", "danal", "Danal", "danel", "Danel"] 

needsToStart = discord.Embed(title="You need to start a roulette game.", description="`%sstart`" % (bot.prefix), color=0x00ff00)

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
  arguments.messageReturn = ['embed', arguments.currentmessage.channel,needsToStart]

