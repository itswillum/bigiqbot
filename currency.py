from commands import arguments
from replit import db
from datetime import date

def setUp(person):
  today = date.today()
  db[person] = {
    'currency':'0',
    'last_daily':'%s' % (today.strftime("%m/%d/%y"))
  }

def getCurr(person):
  if person in db.keys():
    return db[person]['currency']
  else:
    setUp(person)
    return db[person]['currency']

def getDailyDate(person):
  if person in db.keys():
    return db[person]['last_daily']
  else:
    setUp(person)
    return db[person]['last_daily']

def addCurr(person, amount):
  if person in db.keys():
    value = int(db[person]['currency'])
    value += amount
    db[person] = {
      'currency':'%d' % (value),
      'last_daily':'%s' % (db[person]['last_daily'])
    }
    return db[person]['currency']
  else:
    setUp(person)
    value = int(db[person]['currency'])
    value += amount
    db[person] = {
      'currency':'%d' % (value),
      'last_daily':'%s' % (db[person]['last_daily'])
    }
    return db[person]['currency']

def changeDailyDate(person):
  today = date.today()
  if person in db.keys():
    db[person] = {
      'currency':'%s' % (db[person]['currency']),
      'last_daily':'%s' % (today.strftime("%m/%d/%y"))
    }
  else:
    setUp(person)
    db[person] = {
      'currency':'%s' % (db[person]['currency']),
      'last_daily':'%s' % (today.strftime("%m/%d/%y"))
    }