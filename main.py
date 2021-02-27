import discord
import os
import keep_alive
import bot

client = discord.Client()


prefix = "-"


bot.load_commands()

@client.event
async def on_ready():
  print("{0.user} is now online".format(client))


@client.event
async def on_message(message):
  global going
  global waiting
  global playerContents
  global biased
  global prefix
  if message.author == client.user:
    return
  

  if message.content.split()[0][0] == prefix:
    fullMessage = message.content.split()
    fullMessage[0] = fullMessage[0][1:]
    if bot.check_first(fullMessage) == True:
      await message.channel.send(bot.check_commands(message.channel, fullMessage))

      
keep_alive.keep_alive()
client.run(os.getenv('TOKEN'))
#importantissimo ^^
