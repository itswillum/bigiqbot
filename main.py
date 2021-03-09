import discord
import os
import keep_alive
import bot

client = discord.Client()

bot.load_commands()


@client.event
async def on_ready():
  print("{0.user} beep boop".format(client))
  await client.change_presence(status=discord.Status.idle, activity=discord.Game(name=f"{len(client.guilds)} servers"))


@client.event
async def on_message(message):
  global going
  global waiting
  global playerContents
  global biased
  global prefix
  if message.author == client.user:
    return
  
  if message.content.split()[0][0] == bot.prefix:
    fullMessage = message.content.split()
    fullMessage[0] = fullMessage[0][1:]
    if bot.check_first(fullMessage) == True:
      newMessage = bot.check_commands(message, fullMessage)
      if type(newMessage) is str: 
        await message.channel.send(newMessage)
      else:
        if type(newMessage) is list:
          if newMessage[0] == "ms":
            await newMessage[1].send(newMessage[2])
          if newMessage[0] == "embed":
            await newMessage[1].send(embed=newMessage[2])
          if newMessage[0] == "mul":
            index = 1
            for i in range(newMessage[1]):
              index += 1
              item = newMessage[index]
              if item[0] == "ms":
                await item[1].send(item[2])
              if item[0] == "embed":
                await item[1].send(embed=item[2])



      
keep_alive.keep_alive()
client.run(os.getenv('TOKEN'))

