from commands import arguments
from commands import roulettegame
import discord
import bot

alreadyStarted = discord.Embed(title="Roulette game already started", description="Do `%splayers` to set the players, or `%snext` to continue." % (bot.prefix, bot.prefix), color=0x00ff00)


if len(arguments.args) == 1:
  if arguments.args[0] == "biased":
    roulettegame.biased = True
if roulettegame.welcome == False:

  arguments.messageReturn = roulettegame.rouletteGame.SendWelcome()
else:
  arguments.messageReturn = ['embed', arguments.currentmessage.channel,alreadyStarted]