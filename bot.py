import os
from commands import arguments
commandList = []

prefix = "-"

class command():
  global commandList
  listenerc = ""
  namec = ""
  fileoutputc = ""
  def __init__(self, listener, fileoutput, name):
    self.listenerc = listener
    self.namec = name
    self.fileoutputc = fileoutput
    commandList.append(self)

def runCommand(program, fullmessage, message):
  arguments.messageReturn = "No Message"
  if os.path.exists("commands/" + program.fileoutputc):
    for word in fullmessage:
      if fullmessage.index(word) != 0:
        arguments.args.append(word)
      arguments.currentmessage = message
    exec(open("commands/" + program.fileoutputc).read())
    arguments.args = []
    arguments.currentmessage = ""
    return arguments.messageReturn
  else:
    print("No File Stupid Head")


def check_commands(message, fullmessage):
  for item in commandList:
    if item.listenerc == fullmessage[0]:
       return runCommand(item, fullmessage, message)
def check_first(fullmessage):
  for item in commandList:
    if item.listenerc == fullmessage[0]:
       return True
  return False
def load_commands(): #commands
  command('weather', "weather.py", "WeatherShow")
  command('gamer', 'gamer.py', 'Gamer')
  command('trump', "donaldtrump.py", "Trump")
  command('help', 'help.py', "Help")
  command('roulette', 'roulette.py', "RouletteStart")
  command('players', 'players.py', "PlayerSelect")
  command('next', 'nextround.py', "NextRound")
  command('prefix', 'prefix.py', "ChangePrefix")
  command('annoy', 'annoy.py', "yay")
  command('fib', 'fibstart.py', "FibStart")
  command('join', 'join.py', "JoinGame")
  command('start', 'start.py', "GameStart")
  command('ping', 'ping.py', "ping")
  command('flip', 'coinflip.py', "CoinFlip")
  command('suggest', 'suggest.py', 'issue')
  command('end', 'endgame.py', "EndGame")
  command('cur', 'currencyget.py', "Currency")
  command('daily', 'dailyget.py', "DailyReward")
  command('sadness', 'sadness.py', "FreeStuff")
  command('invite','invite.py',"Invite")