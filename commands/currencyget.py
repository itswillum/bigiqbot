import currency
from commands import arguments

arguments.messageReturn = str(currency.getCurr(arguments.currentmessage.author.id))