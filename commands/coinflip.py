
from commands import arguments
import requests
from replit import db
import currency


if len(arguments.args) == 2:
  if arguments.args[0] == "h" or arguments.args[0] == "t":
    try:
      int(arguments.args[1])
      if int(currency.getCurr(arguments.currentmessage.author.id)) >= int(arguments.args[1]):
        currency.addCurr(arguments.currentmessage.author.id, int(arguments.args[1]) * -1)
        response = requests.get('http://flipacoinapi.com/json')
        result = response.text.split('"')[1]
        if arguments.args[0] == "h" and result == "Heads":
          currency.addCurr(arguments.currentmessage.author.id, int(arguments.args[1]) * 2)
          arguments.messageReturn = "It was heads and you were correct. Your total is now %s" % (currency.getCurr(arguments.currentmessage.author.id))
        elif arguments.args[0] == "t" and result == "Tails":
          currency.addCurr(arguments.currentmessage.author.id, int(arguments.args[1]) * 2)
          arguments.messageReturn = "It was tails and you were correct. Your total is now %s" % (currency.getCurr(arguments.currentmessage.author.id))
        else:
          arguments.messageReturn = "Haha you lose"
      else:
        arguments.messageReturn = "You don't have enough points"
    except Exception as e:
      raise e
      arguments.messageReturn = "Not a valid number"
  else:
    arguments.messageReturn = "You need to pick heads or tails"
else:
  response = requests.get('http://flipacoinapi.com/json')
  arguments.messageReturn = response.text.split('"')[1]
