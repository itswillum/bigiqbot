import os
import arguments
commandList = []

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

def runCommand(program, message, channel):
  if os.path.exists(program.fileoutputc):
    for word in message:
      if message.index(word) != 0:
        arguments.args.append(word)
    exec(open(program.fileoutputc).read())
    arguments.args = []
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