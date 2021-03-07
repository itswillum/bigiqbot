from commands import arguments
from replit import db

def setUp(person):
  db[person] = {
    'currency':'0'
  }

def getCurr(person):
  if person in db.keys():
    return db[person]['currency']
  else:
    setUp(person)
    return db[person]['currency']

def addCurr(person, amount):
  if person in db.keys():
    value = int(db[person]['currency'])
    value += amount
    db[person] = {
      'currency':'%d' % (value)
    }
    return db[person]['currency']
  else:
    setUp(person)
    db[person][0] += amount
    return db[person]['currency']

