from commands import arguments
import discord
import bot

#arguments.messageReturn = "http://bit.ly/3kun8Fy"
if len(arguments.args) == 1:
  if arguments.args[0] == "fib":
    fibHelp = discord.Embed(title="How to play", description=" ", color=0x00ff00)
    fibHelp.add_field(name="%sjoin fib [id]" % (bot.prefix), value="Joins a game of fib in the channel. If you can't join,t he game probably already started.", inline=False)
    fibHelp.add_field(name="%sstart fib [id]" % (bot.prefix), value="Starts the game of fib once everyone has joined; can only be run by the person who created the round. ", inline=False)
    fibHelp.add_field(name="%sfib [id] input" % (bot.prefix), value="This command should be run in your dms after you get your list of cards. If the game of fib is 'fib 1,' and you want to place a King of spades and a 6 of hearts, type `fib 1 input ks 6h`.", inline=False)
    fibHelp.add_field(name="%scards" % (bot.prefix), value="Sends the most up-to-date hand in your dms.", inline=False)
    fibHelp.add_field(name="%send" % (bot.prefix), value="Ends the game of fib. It can only be run by the creator.", inline=False)
		
    arguments.messageReturn = ['embed', arguments.currentmessage.channel,fibHelp] 
  if arguments.args[0] == "trump":
    trumpHelp = discord.Embed(title="Command: `%strump`" % (bot.prefix), description="The correct way to use this command is `%strump <query>` (without the <>). It'll search to see he tweeted anything containing that query and return it." % (bot.prefix),color=0x00ff00, inline=False)
    arguments.messageReturn  = ['embed', arguments.currentmessage.channel,trumpHelp]
 
else:
  helpEmbed = discord.Embed(title="Commands", description="Do `%shelp [command]` for more info." % (bot.prefix), color=0x00ff00)
  helpEmbed.add_field(name="%shelp" % (bot.prefix), value="displays this message", inline=False)
  helpEmbed.add_field(name="%sroulette" % (bot.prefix), value="Starts a game of russian roulette, follow the instructions given", inline=False)
  helpEmbed.add_field(name="%sweather" % (bot.prefix), value="also coming soon", inline=False)
  helpEmbed.add_field(name="%strump" % (bot.prefix), value="Returns a random tweet from Trump's twitter account.", inline=False) 
  helpEmbed.add_field(name="%sfib" % (bot.prefix), value="Starts a game of fib. Do `%shelp fib` for more info." % (bot.prefix), inline=False) 
  helpEmbed.add_field(name="%sflip" % (bot.prefix), value="Flips a coin, returns the side." , inline=False)
  arguments.messageReturn = ['embed', arguments.currentmessage.channel,helpEmbed]
#if return = string its a message else it is an embed - luke freimanis.toupper() 2/27/21 5:44:40 PM EST (GMT-5) 	39.46212758103058, -77.43392750619147 
#the error is in main.py