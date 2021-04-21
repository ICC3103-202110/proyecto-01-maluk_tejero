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
            game.create_all_players(game.deck)
            game.show_players()
            game.start()


if __name__ == '__main__':
    menu()
