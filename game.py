from player import Player
from deck import Deck
import random 

class Game:
    def __init__(self):
        self.__players = []
        self.__deck = Deck()
        self.__log = []
        self.deck.build()
        self.deck.shuffle_deck()
    
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
            card2_h =  self.players[i].hand[1].name
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
        players_not_in_turn = self.players
        players_not_in_turn.remove(player)
        challengers = []
        for player in players_not_in_turn:
            print(f"{player.name}")
            ask = str(input(f"Do you want to challenge {action.name}? (Y/N)"))
            if ask == "Y":
                challengers.append(player)
        if len(challengers)==0:
            return False
        challenger = random.choice(challengers)
        return challenger


    def respond_counteraction(self, player, action):
        print(f"{player.name}")
        ask = str(input(f"Do you want to challenge counteraction {action.name}? (Y/N)"))
        if ask == "Y":
            return True
        else:
            return False


    def start(self):
        while len(self.players) > 1:
            for player in self.players:
                print(self.players)
                if player.alive:
                    action = self.player_turn(player)
                    if action in [0, 1, 3]:
                        self.deck.actions[action].act(self.deck.actions[action], player)
                    elif action in [2, 4, 6]:
                        target = self.choose_target(player)
                        self.deck.actions[action].act(self.deck.actions[action], player, target)
                    elif action in [5]:
                        self.deck.actions[action].act(self.deck.actions[action], player, self.deck)
                    player.show_player_open()







                    



