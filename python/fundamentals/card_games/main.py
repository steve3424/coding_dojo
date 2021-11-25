from operator import itemgetter

from war import War

def PrintGameMenu(games):
    print("\n******* GAME MENU *******")
    print("*  Select a game below  *")
    print("*************************")
    header_width = 25

    for i, game in enumerate(games):
        line = f"* [{i + 1}] "
        line_len = len(line)
        chars_left = header_width - line_len - 2
        chars_to_write = len(game[0]) if len(game[0]) <= chars_left else chars_left
        line += game[0][0:chars_to_write]
        chars_left -= chars_to_write
        line += ' ' * chars_left
        line += " *"
        print(line)
    print("* [Ctrl-C] Exit         *")
    print("*************************")

def ChooseGame(games):
    while True:
        PrintGameMenu(games)
        print("> ", end='')
        i = input()
        try:
            index = int(i)
            if index < 1 or index > len(games):
                raise ValueError
            else:
                return index
        except ValueError:
            print("\nNot an option. Try again")
            continue

def DealCards(deck, players, cards_per_player=None):
    num_players = len(players)
    if cards_per_player:
        for i in range(cards_per_player * num_players):
            card = deck.GetTopCard()
            player = players[i % num_players]
            player.AddCard(card)
    else:
        i = 0;
        while(len(deck.cards) > 0):
            card = deck.GetTopCard()
            player = players[i % num_players]
            player.AddCard(card)
            i += 1

def main():

    games = [("War", War()), ("Rummy", None), ("Long name hopefully long enough too long", None)]
    game_index = ChooseGame(games) - 1
    current_game_obj = games[game_index][1]
    current_game_obj.GameLoop()

    #cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    #suits = ["\u2660", "\u2663", "\u2665", "\u2666"]
    #main_deck = Deck(cards, suits)
    #main_deck.Shuffle(50)

    #players = [Player("Jay"), Player("Ray")]


    #game = ChooseGame()
    #while not game:
    #    print("\nInput not understood. Try again...")
    #    game = ChooseGame()
    
    #print(f"Dealing for {}")
    #DealCards(main_deck, players)
    #round = 1
    #while game:
    #    print(f"Round {round}")
    #    print("Press enter to play")
    #    print("Press 1 to show scores")
    #    c = input()
    #    if c == '':
    #        played = []
    #        for p in players:
    #            card = p.PlayCard()
    #            played.append((card, p))
    #            print(f"{p.name} plays {str(card)}")
    #        print(max(played, key=lambda x: x[0].val))
    
    #        round += 1
    #    elif c == '1':
    #        for p in players:
    #            print(f"{p.name}: {len(p.deck.cards)}")
    #    else:
    #        game = False

if __name__ == "__main__":
    main()