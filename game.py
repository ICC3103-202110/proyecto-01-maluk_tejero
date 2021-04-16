from player import Player
from deck import Deck

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
        targets = game.players
        targets.remove(player)
        targets_str = ""
        for target in targets:
            targets_str += f"{target.name}, "
        target_str = target_str[:-2]
        print(target_str)
        target = input(f"Choose your target")
        return target
    
    def from_target_to_playerObject(self, target):
        for player in players:
            if player.name == target:
                return player




    def Start(self):
        while len(players) > 1:
            pass

