from commands import arguments
from commands import fibcontroller

if arguments.args[0] == "fib":
  if int(arguments.args[1]) in fibcontroller.runningGamesNumber:
    game = fibcontroller.runningGamesClasses[int(arguments.args[1]) - 1]
    if game.creator == arguments.currentmessage.author:
      fibcontroller.runningGamesNumber[fibcontroller.runningGamesClasses.index(game)] = -1
      game = "Closed"
      arguments.messageReturn = "Closed fib lobby %s" % (arguments.args[1])
      
    else:
      arguments.messageReturn = "%s, you are not the leader of this lobby" % (arguments.currentmessage.author)
  else:
    arguments.messageReturn = "Not a running game"