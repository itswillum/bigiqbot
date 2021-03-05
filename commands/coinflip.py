
from commands import arguments
import requests
from replit import db


if len(arguments.args) == 2:
  try:
    int(arguments.args[0])
    db[arguments.currentmessage.author.id] = str(int(db[arguments.currentmessage.author.id]) - int(arguments.args[0]))
    response = requests.get('http://flipacoinapi.com/json').text
    if arguments.args[1] == "h" and response == '"Heads"':
      db[arguments.currentmessage.author.id] = str(int(db[arguments.currentmessage.author.id]) + int(arguments.args[0]) * 2)
      arguments.messageReturn = "%s ------- yay good job" % (response.split('"')[1])
    elif arguments.args[1] == "t" and response == '"Tails"':
      db[arguments.currentmessage.author.id] = str(int(db[arguments.currentmessage.author.id]) + int(arguments.args[0]) * 2)
      arguments.messageReturn = "%s -------- Yay good job" % (response.split('"')[1])
    else:
      arguments.messageReturn = "%s -------- Haha you suck" % (response.split('"')[1])

  except Exception as e:
    raise e
    arguments.messageReturn = "Thats not a number to bet"
else:
  response = requests.get('http://flipacoinapi.com/json')
  arguments.messageReturn = response.text.split('"')[1]
