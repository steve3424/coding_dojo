from operator import itemgetter

from menu import RunMenu
from war import War

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