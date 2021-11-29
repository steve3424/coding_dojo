from operator import itemgetter

from menu import RunMenu
from war import War

#def PrintGameMenu(games):
#    print("\n******* GAME MENU *******")
#    print("*  Select a game below  *")
#    print("*************************")
#    header_width = 25
#
#    for i, game in enumerate(games):
#        line = f"* [{i + 1}] "
#        line_len = len(line)
#        chars_left = header_width - line_len - 2
#        chars_to_write = len(game[0]) if len(game[0]) <= chars_left else chars_left
#        line += game[0][0:chars_to_write]
#        chars_left -= chars_to_write
#        line += ' ' * chars_left
#        line += " *"
#        print(line)
#    print("* [Ctrl-C] Exit         *")
#    print("*************************")
#
#def ChooseGame(games):
#    while True:
#        PrintGameMenu(games)
#        print("> ", end='')
#        i = input()
#        try:
#            index = int(i)
#            if index < 1 or index > len(games):
#                raise ValueError
#            else:
#                return index
#        except ValueError:
#            print("\nNot an option. Try again")
#            continue

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
    games = [War()]
    game_index = RunMenu("Game Menu", games)
    current_game_obj = games[game_index]
    current_game_obj.GameLoop()

if __name__ == "__main__":
    main()