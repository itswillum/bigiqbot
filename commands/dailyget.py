from commands import arguments
import currency
from datetime import date

today = date.today()
if today.strftime("%m/%d/%y") == currency.getDailyDate(arguments.currentmessage.author.id):
  arguments.messageReturn = "You have already claimed your daily for today."
else:
  currency.addCurr(arguments.currentmessage.author.id, 50)
  currency.changeDailyDate(arguments.currentmessage.author.id)
  arguments.messageReturn = "You have claimed your daily, you total is now %s" % (currency.getCurr(arguments.currentmessage.author.id))