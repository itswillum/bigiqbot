from replit import db
import sys
from datetime import date

#This is for a complete db breakdown. This will only be activated from the console

def clear():
  for key in db.keys():
    today = date.today()
    db[key] = {
      'currency':'0',
      'last_daily':'%s' % (today.strftime("%m/%d/%y"))
    }
def setPerson(id, amount):
  db[id] = {
    'currency':'%s' % (amount)
  }
  print(db[id]['currency'])

def show():
  print(db[sys.argv[2]][0])

if sys.argv[1] == "clear":
  clear()
if sys.argv[1] == "set":
  setPerson(sys.argv[2], sys.argv[3])
if sys.argv[1] == "show":
  show()
if sys.argv[1] == "showkeys":
  for item in db.keys():
    print(item)

