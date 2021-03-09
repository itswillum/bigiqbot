from commands import arguments
import currency

if currency.getCurr(arguments.currentmessage.author.id) == '0':
  currency.addCurr(arguments.currentmessage.author.id, 10)
  arguments.messageReturn = "You got lucky this time, now don't ask again"
else:
  arguments.messageReturn = "Bruh, you still have currency. GREEDY"