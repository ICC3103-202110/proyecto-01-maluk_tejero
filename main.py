from game import Game


def print_menu_and_select():
    print("\nSelecciona una de las siguientes opciones:")
    print("1. Start game")
    print("0. Exit")
    return int(input())


def menu():
    game = Game()
    while True:
        selection = print_menu_and_select()
        if selection == 0:
            break
        if selection == 1:
            game.create_all_players()
            for player in game.players:
                print("\n" * 100)
                x = input(f"Press enter to show {player.name} hand")
                player.show_player_open()
                x = input("Press enter to continue")
            print("\n" * 100)
            game.start()


if __name__ == '__main__':
    menu()
