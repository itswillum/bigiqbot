import bot
import requests
import json
import math
import discord

cardsPerhand = 12

currentFibGames = 0

runningGamesNumber = []
runningGamesClasses = []

cardsNum = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]



def cardJsontoRead(num, suit):
  number = "null"
  suiter = "null"
  try:
    int(num)
    number = num
  except:
    if num == "ACE":
      number = "Ace"
    if num == "JACK":
      number = "Jack"
    if num == "QUEEN":
      number = "Queen"
    if num == "KING":
      number = "King"
  if suit == "SPADES":
    suiter = ":spades:"
  if suit == "HEARTS":
    suiter = ":hearts:"
  if suit == "DIAMONDS":
    suiter = ":diamonds:"
  if suit == "CLUBS":
    suiter = ":clubs:"
  return number + suiter
    

def userToUserName(user):
  return user.name + "#" + user.discriminator

def membergo(user, listt):
  for item in listt:
    print(userToUserName(item) + " : " + user)
    if userToUserName(item) == user:
      return listt.index(item)
  return False

def get_deck():
  response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
  json_data = json.loads(response.text)
  return json_data['deck_id']

def draw_cards(deckID, cpp):
  response = requests.get("https://deckofcardsapi.com/api/deck/%s/draw/?count=%d" % (deckID, cpp))
  json_data = json.loads(response.text)
  return json_data




def DealsendToPlayers(players):
  sendingtable = []
  biggersendingtable = []
  deck_id = get_deck()
  cpp = math.floor(52/len(players))
  for player in players:
    sendingValue = draw_cards(deck_id, cpp)
    for card in sendingValue['cards']:
      sendingtable.append(card['value'] + ":%s:" % (card['suit'].lower()))
    biggersendingtable.append(sendingtable)
    sendingtable = []
  for item in biggersendingtable:
    biggersendingtable[biggersendingtable.index(item)] = ['ms', players[biggersendingtable.index(item)], item]
  
  return biggersendingtable

def cardToNumber(table):
  lis = []
  for item in table:
    lis.append(item.split(':')[0])
  return lis

class fib_game():
  def __init__(self, player, channel):
    global currentFibGames
    global runningGamesNumber
    global currentFibGames
    global cardsNum
    currentFibGames += 1
    self.gameId = currentFibGames
    self.players = []
    self.players.append(player)
    self.creator = player
    self.channel = channel
    self.playerCardsNumber = []
    self.playersCards = []
    self.playerCardsNumber.append([])
    self.playersCards.append([])
    self.joinable = True
    self.currentTurn = "null"
    self.turnnumber = 0
    self.votedPlayers = []
    self.currentState = "null"
    self.currentCardNum = cardsNum[0]
    runningGamesClasses.append(self)
    runningGamesNumber.append(self.gameId)
  def next_turn(self):
    global cardsNum
    self.turnnumber += 1
    if self.turnnumber == len(self.players):
      self.turnnumber = 0
    self.currentTurn = self.players[self.turnnumber]
    try:
      self.currentCardNum = cardsNum[cardsNum.index(self.currentCardNum) + 1]
    except:
      self.currentCardNum = cardsNum[0]
    self.currentState = "null"
    self.votedPlayers = []
    return "It is <@%s> 's turn and they are on %s" % (self.players[self.players.index(self.currentTurn)].id, self.currentCardNum)
  def set_deckId(self, deck_id):
    self.deckId = deck_id
  def add_player(self, player):
    self.players.append(player)
    self.playerCardsNumber.append([])
    self.playersCards.append([])
  def UpdatePlayerCards(self, player, table):
    #print(self.players)
    
    self.playersCards[self.players.index(player)] = table
    self.playerCardsNumber[self.players.index(player)] = cardToNumber(table)
  def AddPlayerCard(self, player, table):
    for item in table: 
      self.playersCards[self.players.index(player)].append(item)
    for item in table:
      self.playerCardsNumber[self.players.index(player)].append(cardToNumber(item))
  def DeletePlayerCard(self, player, table):
    for item in table:
      for seconditem in self.playersCards[self.players.index(player)]:
        if seconditem == item:
          self.playersCards[self.players.index(player)].pop(self.playersCards[self.players.index(player)].index(seconditem))
    for item in table:
      for seconditem in self.playerCardsNumber[self.players.index(player)]:
        if seconditem == cardToNumber(item):
          self.playerCardsNumber[self.players.index(player)].pop(self.playerCardsNumber[self.players.index(player)].index(seconditem))
  def playerContains(self, player, item):
    if item in self.playersCards[self.players.index(player)]:
      return True
    else:
      return False
  def findPlayerWith(self, item):
    for player in self.players:
      if self.playerContains(player, item) == True:
        return player
    return False
  def showCards(self, player):
    cardEmbed = discord.Embed(title="FIB %d cards" % (self.gameId), description="These are your cards", color=0xd10a07)
            
    hearts = []
    spades = []
    diamonds = []
    clubs = []
    for item in self.playersCards[self.players.index(player)]:
      if item.split(':')[1] == "spades":
        spades.append(item)
      if item.split(':')[1] == "clubs":
        clubs.append(item)
      if item.split(':')[1] == "hearts":
        hearts.append(item)
      if item.split(':')[1] == "diamonds":
        diamonds.append(item)
    cardEmbed.add_field(name="Spades :spades:", value=', '.join(spades), inline=False)
    cardEmbed.add_field(name="Clubs :clubs:", value=', '.join(clubs), inline=False)
    cardEmbed.add_field(name="Hearts :hearts:", value=', '.join(hearts), inline=False)
    cardEmbed.add_field(name="Diamonds :diamonds:", value=', '.join(diamonds), inline=False)
    return cardEmbed
  def addToDiscard(self, deckID, table):
    bigTable = []
    for item in table:
      num = "null"
      suit = "null"
      if item.split(':')[0] == "10":
        num = "0"
      else:
        num = item[0].upper()
      if item.split(':')[1] == "spades":
        suit = "S"
      if item.split(':')[1] == "hearts":
        suit = "H"
      if item.split(':')[1] == "diamonds":
        suit = "D"
      if item.split(':')[1] == "clubs":
        suit = "C"
      bigTable.append(num + suit)

    requests.get('https://deckofcardsapi.com/api/deck/%s/pile/discard%s/add/?cards=%s') % (deckID,self.gameId, ','.join(bigTable))
def returnPile(deckID):
  response = requests.get('https://deckofcardsapi.com/api/deck/%s/pile/discard/list/' % (deckID))
  json_data = json.loads(response.text)
  table = []
  for item in json_data['piles']['discard']:
    table.append(cardJsontoRead(item['value'], item['suit']))
  return table