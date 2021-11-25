from random import randint

class Player:
    def __init__(self, name):
        self.points = []
        self.score = 0
        self.name = name
        self.hand = Deck()

    def AddCard(self, card):
        self.hand.AddCard(card)

    def AddCardBottom(self, card):
        self.hand.AddCardBottom(card)

    def PlayCard(self):
        return self.hand.GetTopCard()

    def GetNumCards(self):
        return len(self.hand.cards)

    def __str__(self) -> str:
        return (f"{self.name}\n"
                f"{len(self.hand.cards)}\n"
                f"{str(self.hand)}\n")

    def __repr__(self) -> str:
        return str(self)

class Card:
    def __init__(self, val, suit, face):
        self.val = val
        self.suit = suit
        self.face = face

    def __repr__(self) -> str:
        return f"{self.face}-{self.suit}"

class Deck:
    def __init__(self, cards=None, suits=None):
        self.cards = []
        if cards and suits:
            for s in suits:
                for i,c in enumerate(cards):
                    self.cards.append(Card(i, s, c))

    def GetTopCard(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None
    
    def AddCard(self, card):
        self.cards.append(card)
    
    def AddCardBottom(self, card):
        self.cards.insert(0, card)

    def Sort(self):
        self.cards.sort(key=lambda x: x.val)
        self.cards.sort(key=lambda x: x.suit)

    def Shuffle(self, num_shuffles=1):
        num_cards = len(self.cards)
        if num_cards > 1:
            num_passes = num_shuffles if num_shuffles > 0 else 1
            for i in range(num_passes):
                for i in range(len(self.cards)):
                    new_pos = randint(0, num_cards - 1)
                    temp = self.cards[new_pos]
                    self.cards[new_pos] = self.cards[i]
                    self.cards[i] = temp

    def __str__(self) -> str:
        return str(self.cards)
