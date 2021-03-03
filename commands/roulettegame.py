#import os
import random
import bot

welcome = False
players = False

playerList = []

biased = False

deathThings = ["killed flat like a pancake", "shot to death", "eaten alive", "stabbed multiple times", "going coocoo for clorox", "watching all the simpsons seasons straight", "eating 1000 apples at once", "lost at sea"]

danielVariations = ["Daniel", "daniel", "danal", "Danal", "danel", "Danel", "<@347804260077142030>"] 

class rouletteGame():
  def __init__():
    pass
  def SendWelcome():
    global welcome
    global playerList
    welcome = True
    playerList = []
    return "Welcome to totally not biased russian roulette. Type `%splayers` followed by the player names to enter." % (bot.prefix)
  def personPick(table):
    global players
    players = True
    global playerList
    playerList = table
    return "Welcome to your doom -- %s" % (', '.join(table)) + "------- Type `%snext` to start" % (bot.prefix)
  def kill():
    global playerList
    randomInt  = random.randrange(0, len(playerList))
    players = playerList
    deadPerson = players[randomInt]
    players.pop(randomInt)
    playerList = players
    randomdeath = random.randrange(0, len(deathThings))
    if len(playerList) == 1:
      rouletteGame.restart()
      return "%s was %s.  %s remain" % (deadPerson, deathThings[randomdeath], ', '.join(players)) + "---------" + " %s is the last one standing" % (playerList[0])
    else:
      return "%s was %s.  %s remain" % (deadPerson, deathThings[randomdeath], ', '.join(players))
  def restart():
    global welcome
    global players
    global biased
    welcome = False
    players = False
    biased = False
  def killdaniel(indexx):
    global playerList
    randomInt  = playerList.index(danielVariations[indexx])
    players = playerList
    deadPerson = players[randomInt]
    players.pop(randomInt)
    playerList = players
    randomdeath = random.randrange(0, len(deathThings))
    if len(playerList) == 1:
      rouletteGame.restart()
      return "%s was %s.  %s remain" % (deadPerson, deathThings[randomdeath], ', '.join(players)) + "---------" + " %s is the last one standing" % (playerList[0])
    else:
      return "%s was %s.  %s remain" % (deadPerson, deathThings[randomdeath], ', '.join(players))
