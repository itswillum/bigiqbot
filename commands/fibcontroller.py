import bot
import requests
import json
import math

cardsPerhand = 12

currentFibGames = 0

runningGamesNumber = []
runningGamesClasses = []

cardsNum = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]



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
    global cardNum
    self.turnnumber += 1
    if self.turnnumber == len(self.players):
      self.turnnumber = 0
    self.currentCardNum = cardNum[cardsNum.index(self.currentCardNum) + 1]
    self.currentState = "null"
    self.votedPlayers = []
    return "It is <@%s> turn and they are on %s" % (self.players[self.currentTurn].id, self.currentCardNum)
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
      for seconditem in self.playersCards[self.player.index(player)]:
        if seconditem == item:
          self.playersCards[self.player.index(player)].pop(self.playersCards[self.player.index(player)].index(seconditem))
    for item in table:
      for seconditem in self.playersCardsNumber[self.player.index(player)]:
        if seconditem == cardToNumber(item):
          self.playersCardsNumber[self.player.index(player)].pop(self.playersCardsNumber[self.player.index(player)].index(seconditem))
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