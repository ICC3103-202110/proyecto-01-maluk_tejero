from player import Player


players = []


def create_player():
    name = str(input("What is your name?"))
    players.append(Player(name))

def create_all_players():
    num_of_players = int(input("How many players would like to play? 3 or 4\n"))
    if num_of_players not in [3, 4]:
        create_all_players()
    else:
        for i in range(num_of_players):
            create_player()

def show_players():
    print("\nPlayers:")
    for (i, _) in enumerate(players):
        print(f"{i}: {players[i].name} - {players[i].coins}")


if __name__ == '__main__':
    create_all_players()
    show_players()
