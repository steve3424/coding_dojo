from cards import Deck, Player

class War:
    def __init__(self):
        cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["\u2660", "\u2663", "\u2665", "\u2666"]
        self.game_name = "War"
        self.deck = Deck(cards, suits)
        self.players = [Player("Jay"), Player("Ray")]
        self.round = 1

    def DealCards(self):
        num_players = len(self.players)
        i = 0
        while len(self.deck.cards) > 0:
            card = self.deck.cards.pop()
            p = self.players[i % num_players]
            p.AddCard(card)
            i += 1

    def GoToWar(self):
        pass

    def GameLoop(self):
        print("Getting ready for war between:")
        for p in self.players:
            print(p.name)

        print("Shuffling...")
        self.deck.Shuffle()

        print("Dealing...")
        self.DealCards()

        p1 = self.players[0]
        p2 = self.players[1]

        while True:
            print(p1.name)
            print(p1.hand)
            print(p2.name)
            print(p2.hand)
            i = input()

            print(f"Round {self.round}")

            p1_card = p1.PlayCard()
            p2_card = p2.PlayCard()

            print(f"{p1.name} plays:\t{str(p1_card)}")
            print(f"{p2.name} plays:\t{str(p2_card)}")

            if p1_card.val == p2_card.val:
                print("should go to war")
                p1.AddCardBottom(p1_card)
                p2.AddCardBottom(p2_card)
            elif p1_card.val > p2_card.val:
                print(f"{p1.name} wins")
                p1.AddCardBottom(p1_card)
                p1.AddCardBottom(p2_card)
            else:
                print(f"{p2.name} wins")
                p2.AddCardBottom(p1_card)
                p2.AddCardBottom(p2_card)

            print(f"{p1.name} score:\t{len(p1.hand.cards)}")
            print(f"{p2.name} score:\t{len(p2.hand.cards)}")

            if len(p1.hand.cards) == 0:
                print(f"{p2.name} wins!")
                break
            if len(p2.hand.cards) == 0:
                print(f"{p1.name} wins!")
                break