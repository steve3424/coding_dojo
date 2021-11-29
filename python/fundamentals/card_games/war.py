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

    def GoToWar(self, p1_card, p2_card):
        print("Time for war!!!")

        p1 = self.players[0]
        p2 = self.players[1]
        p1_stack = [p1_card]
        p2_stack = [p2_card]

        while True:
            i = input()
            # Play 2 cards for war if possible
            for i in range(2):
                if p1.GetNumCards() > 0:
                    p1_stack.append(p1.PlayCard())
                if p2.GetNumCards() > 0:
                    p2_stack.append(p2.PlayCard())
            
            # Print both war stacks
            print(p1.name + ":\t", end='')
            for i,c in enumerate(p1_stack):
                if i == len(p1_stack) - 1:
                    print(c)
                elif i % 2 == 0:
                    print(str(c) + ", ", end='')
                else:
                    print("*, ", end='')
            print(p2.name + ":\t", end='')
            for i,c in enumerate(p2_stack):
                if i == len(p2_stack) - 1:
                    print(c)
                elif i % 2 == 0:
                    print(str(c) + ", ", end='')
                else:
                    print("*, ", end='')
                
            # Find winner
            if p1_stack[-1].val > p2_stack[-1].val:
                print(p1.name + " wins! Look at what they got!")
                print(p1_stack)
                print(p2_stack)
                while len(p1_stack) > 0:
                    p1.AddCardBottom(p1_stack.pop())
                while len(p2_stack) > 0:
                    p1.AddCardBottom(p2_stack.pop())
                break
            elif p1_stack[-1].val < p2_stack[-1].val:
                print(p2.name + " wins! Look at what they got!")
                print(p1_stack)
                print(p2_stack)
                while len(p1_stack) > 0:
                    p2.AddCardBottom(p1_stack.pop())
                while len(p2_stack) > 0:
                    p2.AddCardBottom(p2_stack.pop())
                break
            else:
                print("Tie!")
                if p1.GetNumCards() == 0 and p2.GetNumCards() == 0:
                    print("No more cards to play. Returning cards and reshuffling...")
                    while len(p1_stack) > 0:
                        p1.AddCard(p1_stack.pop())
                    while len(p2_stack) > 0:
                        p2.AddCard(p2_stack.pop())
                    p1.hand.Shuffle(10)
                    p2.hand.Shuffle(10)
                    return
                else:
                    print("War again!")
                    continue

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
            print(f"Round {self.round}")
            if self.round % 10 == 0:
                p1.hand.Shuffle(50)
                p2.hand.Shuffle(50)
            self.round += 1

            print(p1.name + ": ", end='')
            print(p1.hand)
            print(p2.name + ": ", end='')
            print(p2.hand)
            i = input()

            p1_card = p1.PlayCard()
            p2_card = p2.PlayCard()

            print(f"{p1.name} plays:\t{str(p1_card)}")
            print(f"{p2.name} plays:\t{str(p2_card)}")

            if p1_card.val == p2_card.val:
                self.GoToWar(p1_card, p2_card)
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
        
    def __str__(self):
        return "War"