from replit import db
import sys

#This is for a complete db breakdown. This will only be activated from the console

def clear():
  for key in db.keys():
    db[key] = 0
def setPerson(id, amount):
  db[id] = amount

if sys.argv[1] == "clear":
  clear()
if sys.argv[1] == "set":
  setPerson(sys.argv[2], sys.argv[3])