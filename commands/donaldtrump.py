
import json
import requests
import random
from commands import arguments
import discord

noMatches = discord.Embed(title="There are no matches.", description="Try a different query.", color=0x00ff00)

response = requests.get("https://www.tronalddump.io/search/quote?query=%s" % ((arguments.args[0])))
json_data = json.loads(response.text)
if json_data['count'] == 0:
  arguments.messageReturn = "There are no matches"
else:
  randomInt = random.randrange(0, json_data['count'])
  arguments.messageReturn = json_data['_embedded']['quotes'][randomInt]['value'] + " - " + json_data['_embedded']['quotes'][randomInt]['_embedded']['source'][0]['url']
