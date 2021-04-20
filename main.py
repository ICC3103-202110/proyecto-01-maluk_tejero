from game import Game


def print_menu_and_select():
    print("\nSelecciona una de las siguientes opciones:")
    print("1. Start game")
    print("2. Show players")
    print("3. Show player 1")
    print('4. Show player 2')
    print('5. Show player 3')
    print("0. Exit")
    return int(input())


def menu():
    game = Game()
    while True:
        selection = print_menu_and_select()
        if selection == 0:
            break
        if selection == 1:
            game.deck.show_deck()
            game.create_all_players(game.deck)
        if selection == 2:
            game.show_players()
        if selection == 3:
            game.players[0].show_player_open()
            game.deck.actions[5].act(game.deck.actions[5], game.players[0], game.deck)
            game.players[0].show_player_open()
        if selection == 4:
            game.players[1].show_player_open()
            game.deck.actions[0].act(game.deck.actions[0], game.players[1])
            game.players[1].show_player_open()
        if selection == 5:
            game.players[2].show_player_open()
            


if __name__ == '__main__':
    menu()
