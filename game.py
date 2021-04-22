from player import Player
from deck import Deck
from random import choice


class Game:
    def __init__(self):
        self.__players = []
        self.__deck = Deck()
        self.deck.build()
        self.deck.shuffle_deck()
        self.__log = []

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self):
        pass

    @property
    def deck(self):
        return self.__deck

    @deck.setter
    def deck(self):
        pass

    @property
    def log(self):
        return self.__log

    @log.setter
    def log(self):
        pass

    def add_log(self, txt):
        log.append(txt)

    def create_player(self):
        name = str(input("What is your name?"))
        return Player(name)

    def create_all_players(self, deck):
        num_of_players = int(input("How many players would like to play? 3 or 4\n"))
        if num_of_players not in [3, 4]:
            create_all_players()
        else:
            for i in range(num_of_players):
                player = self.create_player()
                card1 = deck.draw_card()
                card2 = deck.draw_card()
                player.add_card(card1)
                player.add_card(card2)
                player.add_hidden_card(deck.hide())
                player.add_hidden_card(deck.hide())
                self.players.append(player)

    def show_players(self):
        print("\nPlayers:")
        for (i, _) in enumerate(self.players):
            card1_h = self.players[i].hand[0].name
            card2_h = self.players[i].hand[1].name
            print(f"{i}: {self.players[i].name} - Coins: {self.players[i].coins} - Hand: {card1_h}, {card2_h}")

    def show_player_open(self, player):
        cards = ""
        for pos in range(len(player.cards)):
            cards += f"{player.cards[pos].name}, "
        cards = cards[:-2]
        print(f"{player.name} - Coins: {player.coins} - Cards: {cards}")

    def choose_target(self, player):
        targets = self.players[:]
        targets.remove(player)
        print(f"Choose your target")
        for target in targets:
            if target.alive:
                print(f"{targets.index(target)}. {target.name}")
        target = int(input())
        target = targets[target]
        return target

    def player_turn(self, player):
        if player.coins >= 10:
            return 3
        print(f"\n{player.name} turn")
        player.show_player_open()
        print("Choose your action")
        print("\nGeneral Actions")
        print("  0. Income")
        print("  1. Foreign Aid")
        print("  2. Coup")
        print("\nCharacter Actions")
        print("  3. Taxes")
        print("  4. Assassinate")
        print("  5. Exchange")
        print("  6. Steal")
        return int(input())

    def ask_challenge(self, player, action):
        players_not_in_turn = self.players[:]
        players_not_in_turn.remove(player)
        challengers = []
        for player in players_not_in_turn:
            print(f"{player.name}")
            ask = str(input(f"Do you want to challenge {action.name}? (Y/N)"))
            if ask == "Y":
                challengers.append(player)

        if len(challengers) == 0:
            return False
        challenger = choice(challengers)
        return challenger

    def challenge(self, player, action, options):
        allow_challenge = True
        if action in options:
            challenger = self.ask_challenge(player, self.deck.actions[action])
            if challenger:
                player_has_card = player.check_for_card(self.deck.actions[action])
                if player_has_card:
                    print(f"{player.name} has {self.deck.actions[action].name}")
                    challenger.reveal_card()
                    card_to_deck = player.remove_card_challenged(self.deck.actions[action])
                    self.deck.add_card_deck(card_to_deck)
                    self.deck.shuffle_deck()
                    added_card = self.deck.draw_card()
                    player.add_card(added_card)
                    player.add_hidden_card(self.deck.actions[8])
                    # counter attack
                else:
                    print(f"{player.name} does not have {self.deck.actions[action].name}")
                    player.reveal_card()
                    allow_challenge = False
        return allow_challenge

    def counter_action(self):
        pass

    def start(self):
        while len(self.players) > 1:
            for player in self.players:
                self.show_players()
                if player.alive:
                    if player.coins >= 10:
                        print(f"\n{player.name} turn")
                        action = 2
                    else:
                        action = self.player_turn(player)

                    if action in [0, 1, 3]:
                        allow_challenge = self.challenge(player, action, [3])
                        if allow_challenge:
                            self.deck.actions[action].act(player)
                    elif action in [2, 4, 6]:
                        if action == 4 and player.coins < 3:
                            raise ValueError("Not enough coins. Coins required = 3")
                        if action == 2 and player.coins < 7:
                            raise ValueError("Not enough coins. Coins required = 7")
                        target = self.choose_target(player)
                        allow_challenge = self.challenge(player, action, [4, 6])
                        if allow_challenge:
                            self.deck.actions[action].act(player, target)
                    elif action in [5]:
                        allow_challenge = self.challenge(player, action, [5])
                        if allow_challenge:
                            self.deck.actions[action].act(player, self.deck)
                    player.show_player_open()
