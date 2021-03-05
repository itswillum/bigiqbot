from commands import arguments
from replit import db

try:
  arguments.messageReturn = str(db[arguments.currentmessage.author.id])
except:
  db[arguments.currentmessage.author.id] = 0
  arguments.messageReturn = '0'
