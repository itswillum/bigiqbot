from commands import arguments
import discord
import bot
from commands import fibcontroller

hasJoined = discord.Embed(title="Join successful", description="You have joined the game of fib, and your cards will be displayed here.", color=0x00ff00)
notRunningGame = discord.Embed(title="That's not a running game.", description="", color=0x00ff00)
notenoughArgs = discord.Embed(title="Not enough arguments", description = '', color = 0x00ff00)

if len(arguments.args) == 2:
  if arguments.args[0] == "fib":
    if int(arguments.args[1]) in fibcontroller.runningGamesNumber:
        if  fibcontroller.runningGamesClasses[fibcontroller.runningGamesNumber.index(int(arguments.args[1]))].joinable == True:
          if arguments.currentmessage.author in fibcontroller.runningGamesClasses[fibcontroller.runningGamesNumber.index(int(arguments.args[1]))].players:
            arguments.messageReturn = "%s, you are already in fib lobby %s" % (arguments.currentmessage.author, arguments.args[1])
          else:	
            fibcontroller.runningGamesClasses[fibcontroller.runningGamesNumber.index(int(arguments.args[1]))].add_player(arguments.currentmessage.author)
            arguments.messageReturn = ['mul', 2,["embed", arguments.currentmessage.author, hasJoined],['ms', fibcontroller.runningGamesClasses[int(arguments.args[1]) - 1].channel, "%s has joined fib lobby %s" % (arguments.currentmessage.author, arguments.args[1])]]
        else:
          arguments.currentmessage = "That game has already started"
    else:
      arguments.messageReturn = ['embed', arguments.currentmessage.channel, notRunningGame]

else:
  arguments.messageReturn = ['embed', arguments.currentmessage.channel, notenoughArgs]