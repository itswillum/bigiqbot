from commands import arguments
from commands import fibcontroller
import bot
import discord
#too 5Head for me
if len(arguments.args) == 2:
  if arguments.args[0] == "fib":
    if int(arguments.args[1]) in fibcontroller.runningGamesNumber:
      if fibcontroller.runningGamesClasses[fibcontroller.runningGamesNumber.index(int(arguments.args[1]))].creator == arguments.currentmessage.author:
        if fibcontroller.runningGamesClasses[fibcontroller.runningGamesNumber.index(int(arguments.args[1]))].joinable == True:
          Game = fibcontroller.runningGamesClasses[fibcontroller.runningGamesNumber.index(int(arguments.args[1]))]
          Game.joinable = False
          value = fibcontroller.DealsendToPlayers(Game.players)
          for player in value:
            Game.UpdatePlayerCards(player[1], value[value.index(player)][2])
          compmessage = ['mul', len(value) + 1, ['ms', arguments.currentmessage.channel, "%s has started fib in lobby %s --------------- It's %s turn and they are on Ace(s)" % (arguments.currentmessage.author, arguments.args[1], "<@%s>" % (Game.findPlayerWith("ACE:spades:").id))]]
          Game.currentTurn = Game.findPlayerWith("ACE:spades:")
          Game.turnnumber = Game.players.index(Game.findPlayerWith("ACE:spades:"))
          #for personm in value:
            #compmessage.append(personm)
          
          
          for sending in value:
            cardEmbed = discord.Embed(title="FIB %d cards" % (Game.gameId), description="These are your cards", color=0xd10a07)
            
            hearts = []
            spades = []
            diamonds = []
            clubs = []
            for item in sending[2]:
              if item.split(':')[1] == "spades":
                spades.append(item)
              if item.split(':')[1] == "clubs":
                clubs.append(item)
              if item.split(':')[1] == "hearts":
                hearts.append(item)
              if item.split(':')[1] == "diamonds":
                diamonds.append(item)
            cardEmbed.add_field(name="Spades :spades:", value=', '.join(spades), inline=False)
            cardEmbed.add_field(name="Clubs :clubs:", value=', '.join(clubs), inline=False)
            cardEmbed.add_field(name="Hearts :hearts:", value=', '.join(hearts), inline=False)
            cardEmbed.add_field(name="Diamonds :diamonds:", value=', '.join(diamonds), inline=False)
          
            compmessage.append(['embed', sending[1], cardEmbed])
         
          arguments.messageReturn = compmessage
        else:
          arguments.messageReturn = "That lobby has already started"
          
      else:
        arguments.messageReturn = "%s You are not the creator of this lobby" % (arguments.currentmessage.author)
    else:
      arguments.messageReturn = "That is not a current lobby"
else:
  arguments.messageReturn = "You need more arguments"