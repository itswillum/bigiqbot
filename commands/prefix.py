from commands import arguments
import bot

if len(arguments.args) > 0:
  bot.prefix = arguments.args[0]
  arguments.messageReturn = "Changed prefix to %s" % (arguments.args[0])
else:
  arguments.messageReturn = "No arguments passed"