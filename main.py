from player import Player
from deck import Deck

players = []


def print_menu_and_select():
    print("\nSelecciona una de las siguientes opciones:")
    print("1. Create deck")
    print("2. Create players")
    print("3. Show players")
    print('4. None')
    print("0. Exit")
    return int(input())


def create_deck():
    deck = Deck()
    deck.shuffle_deck()
    deck.show_deck()
    return deck

def create_player():
        name = str(input("What is your name?"))
        return Player(name)


def create_all_players(deck):
    num_of_players = int(input("How many players would like to play? 3 or 4\n"))
    if num_of_players not in [3, 4]:
        create_all_players()
    else:
        for i in range(num_of_players):
            player = create_player()
            card1 = deck.draw_card()
            card2 = deck.draw_card()
            player.add_card(card1)
            player.add_card(card2)
            players.append(player)
        


def show_players():
    print("\nPlayers:")
    for (i, _) in enumerate(players):
        print(f"{i}: {players[i].name} - Coins: {players[i].coins} - Cards: {players[i].cards}")


def menu():
    while True:
        selection = print_menu_and_select()
        if selection == 0:
            break
        if selection == 1:
            deck = create_deck()
        if selection == 2:
            create_all_players(deck)
        if selection ==3:
            show_players()
        if selection == 4:
            pass
            
if __name__ == '__main__':
    menu()