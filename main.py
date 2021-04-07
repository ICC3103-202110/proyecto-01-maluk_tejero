from player import Player
from deck import Deck

players = []


def print_menu_and_select():
    print("\nSelecciona una de las siguientes opciones:")
    print("1. Start game")
    print("2. Show players")
    print("3. None")
    print('4. None')
    print("0. Exit")
    return int(input())


def create_deck():
    deck = Deck()
    deck.shuffle_deck()
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
            player.add_hidden_card(deck.hide())
            player.add_hidden_card(deck.hide())
            players.append(player)



def show_players():
    print("\nPlayers:")
    for (i, _) in enumerate(players):
        card1 = players[i].cards[0]
        card2 = players[i].cards[1]
        players[i].reveal_card(0)
        card1_h = players[i].hand[0]
        card2_h =  players[i].hand[1]
        print(f"{i}: {players[i].name} - Coins: {players[i].coins} - Cards: {card1.name}, {card2.name} - Hand: {card1_h.name}, {card2_h.name}")


def menu():
    while True:
        selection = print_menu_and_select()
        if selection == 0:
            break
        if selection == 1:
            deck = create_deck()
            create_all_players(deck)
        if selection == 2:
            show_players()
        if selection ==3:
            pass
        if selection == 4:
            pass


if __name__ == '__main__':
    menu()
