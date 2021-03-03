from commands import arguments
import bot
import discord
from commands import fibcontroller

def isAllItem(item, table):
  cards = {
    "Ace":"a",
    "Jack":"j",
    "Queen":"q",
    "King":"k"
  }
  nitem = ""
  sucess = False
  try:
    int(item)
    sucess = True
  except:
    sucess = False
  if sucess:
    nitem = int(item)
  else:
    nitem = cards[item]
  for thing in table:
    if not thing[0] == str(nitem):
      return "fib"
  
  return "truth"

def codeToRead(code):
  if len(code) == 2:
    value = 0
    suit = 0
    try:
      int(code[0])
      value = code[0]
    except ValueError:
      if code[0].lower() == "j":
        value = "JACK"
      if code[0].lower() == "q":
        value = "QUEEN"
      if code[0].lower() == "k":
        value = "KING"
      if code[0].lower() == "a":
        value = "ACE"
      if value == 0:
        return "not_code"
    if code[1].lower() == "s":
      suit = ":spades:"
    if code[1].lower() == "h":
      suit = ":hearts:"
    if code[1].lower() == "d":
      suit = ":diamonds:"
    if code[1].lower() == "c":
      suit = ":clubs:"
    if suit == 0:
      return "not_code"
    return value + suit
    

  else:
    suit = 0
    if code[0] == "1" and code[1] == "0":
      if code[2] == "s":
        suit = ":spades:"
        return "10" + suit
      if code[2] == "d":
        suit = ":diamonds:"
        return "10" + suit
      if code[2] == "c":
        suit = ":clubs:"
        return "10" + suit
      if code[2] == "h":
        suit = ":hearts:"
        return "10" + suit
    return "not_code"

def checkForCard(table, gameId, player):
  global fibcontroller
  global codeToRead
  cla = fibcontroller.runningGamesClasses[int(gameId) - 1]
  apptable = []
  for item in table:
    apptable.append(cla.playerContains(player, codeToRead(item)))
  return apptable

if len(arguments.args) > 0:
  if int(arguments.args[0]) in fibcontroller.runningGamesNumber:
    if arguments.args[1] == "input":
      if fibcontroller.runningGamesClasses[int(arguments.args[0]) - 1].currentTurn == arguments.currentmessage.author:
        print("YEP")
        value2 = checkForCard(arguments.args[2:], arguments.args[0], arguments.currentmessage.author)
        if False in value2:
          nopelist = []
          index = -1
          for item in value2:
            index += 1
            if item == False:
              nopelist.append(arguments.args[index + 2])
            arguments.messageReturn = "You do not have the following cards %s ----- Please try again" % (', '.join(nopelist))
      
          
            
        else:
            fibcontroller.runningGamesClasses[int(arguments.args[0]) - 1].currentTurn = "voting"
            fibcontroller.runningGamesClasses[int(arguments.args[0]) - 1].currentState = isAllItem(fibcontroller.runningGamesClasses[int(arguments.args[0]) - 1].currentCardNum, arguments.args[2:])
            fibcontroller.runningGamesClasses[int(arguments.args[0]) - 1].votedPlayers.append(arguments.currentmessage.author)
            print(fibcontroller.runningGamesClasses[int(arguments.args[0]) - 1].currentState)
            print(fibcontroller.runningGamesClasses[int(arguments.args[0]) - 1].currentCardNum)
            arguments.messageReturn = ['mul', 2, ['ms', arguments.currentmessage.author, "Your response has been recorded and shared to the group"], ['ms', fibcontroller.runningGamesClasses[int(arguments.args[0]) - 1].channel, "%s has placed %d %s" % (arguments.currentmessage.author, len(arguments.args) - 2, fibcontroller.runningGamesClasses[int(arguments.args[0]) - 1].currentCardNum)]]
      else:
        arguments.messageReturn = "Not your turn IDOT"
    else:
      game = fibcontroller.runningGamesClasses[int(arguments.args[0]) - 1]
      if game.currentTurn == "voting":
        if not arguments.currentmessage.author in game.votedPlayers:
          if arguments.args[1] == "f":
            if game.currentState == "fib":
              arguments.messageReturn = ['mul', 2,['ms', game.channel, "%s has called a fib and they were correct" % (arguments.currentmessage.author)], ['ms', game.channel, game.next_turn()]]
            else:
              arguments.messageReturn = ['mul', 2,['ms', game.channel, "%s has called a fib and they were not correct" % (arguments.currentmessage.author)], ['ms', game.channel, game.next_turn()]]
          if arguments.args[1] == "t":
            game.votedPlayers.append(arguments.currentmessage.author)
            playerList  = []
            for player in game.players:
              if not player in game.votedPlayers:
                playerList.append(player.name)
            if len(game.votedPlayers) == len(game.players):
              if game.currentState == "truth":
                arguments.messageReturn = ['mul', 2,['ms', game.channel, "Everyone has called truth and they were all correct"], ['ms', game.channel, game.next_turn()]]
              else:
                arguments.messageReturn = ['mul', 2,['ms', game.channel, "Everyone has called truth but it was a fib"], ['ms', game.channel, game.next_turn()]]
            else:
              arguments.messageReturn = "%s has called a truth waiting on %s" % (arguments.currentmessage.author, ', '.join(playerList))
        else:
          arguments.messageReturn = "%s, you have already voted" % (arguments.currentmessage.author)
      else:
        arguments.messageReturn = "It is not voting time"
else:
  if len(arguments.args) == 0:
    
    newGame = fibcontroller.fib_game(arguments.currentmessage.author, arguments.currentmessage.channel)
    #print("Data: Classes = %s, Numbers= %s, NewID = %d, NewPlayers = %s" % (fibcontroller.runningGamesClasses, fibcontroller.runningGamesNumber, newGame.gameId, newGame.players))

    gameStarted = discord.Embed(title="Game started", description="%s has started a game of Fib, type `%sjoin fib %d` to join" % (arguments.currentmessage.author, bot.prefix, newGame.gameId), color=0x00ff00)
    gameCreated = discord.Embed (title='Game Created', description = 'You have started a fib game, your game updates will be here.', color=0x00ff00)

    arguments.messageReturn = ['mul', 2, ['embed', arguments.currentmessage.channel, gameStarted], ['embed', arguments.currentmessage.author, gameCreated]]
