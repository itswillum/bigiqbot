from commands import arguments
from commands import roulettegame
import discord

roulettegamenotstartedEmbed = discord.Embed(title="No roulette game has started", description=" ", color=0x00ff00)


if roulettegame.welcome == True and roulettegame.players == False:
  arguments.messageReturn = roulettegame.rouletteGame.personPick(arguments.args)
else:
  arguments.messageReturn = ['embed', arguments.currentmessage.channel,roulettegamenotstartedEmbed]