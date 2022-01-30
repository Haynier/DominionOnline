import random

class Player:
    def __init__(self):
        self.deck = [TreasureCard('Copper', 0, 1)] * 7 + [VictoryCard("Estate",2,1)] * 3
        self.hand = []
        self.discard = []
        self.points = 3
    
    def shuffle(self):
        self.deck = self.discard
        random.shuffle(self.deck)
        self.discard = []
    
    def draw(self, n):
        if len(self.deck) >= n:
            self.hand += self.deck[0:n]
            self.deck = self.deck[n:]
        else:
            x = n-len(self.deck)
            self.hand += self.deck
            self.shuffle()
            self.draw(x)

    def discardCards(self,cards):
        for card in cards:
            self.hand.remove(card)
            self.discard += [card]

    def trash(self, cards):
        for card in cards:
            self.hand.remove(card)
            if type(card) == VictoryCard or type(card) == CurseCard:
                self.points -= card.worth

    def gain(self, card, toHand = False):
        if toHand == True:
            self.hand += [card]
        else:
            self.discard += [card]
        if type(card) == VictoryCard or type(card) == CurseCard:
            self.points += card.worth

class Card:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

class TreasureCard(Card):
   def __init__(self, name, cost, value): 
       super().__init__(self, name, cost)
       self.value = value

class VictoryCard(Card):
    def __init__(self, name, cost, worth):
        super().__init__(self, name, cost)
        self.worth = worth

class CurseCard(Card):
    def __init__(self, name):
        self.name = name
        self.worth = -1

class ActionCard(Card):
    def __init__(self, name, cost, description, action):
        super().__init__(self, name, cost)
        self.description = description
        self.action = action

    
class Game:
    def __init__(self, players, cardpiles):
        self.players = players
        self.supply = cardpiles + [(TreasureCard('Copper', 0, 1), 100), (TreasureCard('Silver', 3, 2), 100), (TreasureCard('Gold', 6, 3), 100), (VictoryCard('Estate', 2, 1), 24), (VictoryCard('Duchy', 5, 3), 12), (CurseCard('Curse'), 10000)]
        if len(players) == 2:
            self.supply += [(VictoryCard('Province', 8, 6), 8)]
        else:
            self.supply += [(VictoryCard('Province', 8, 6), 12)]
        self.trash = []
    
    