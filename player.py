class Player:
    def __init__(self, name):
        self.__name = name
        self.__coins = 2
        self.__cards = []
        self.__hand = []
        self.__alive = True

    @property
    def name(self):
        return self.__name

    @property
    def coins(self):
        return self.__coins

    @coins.setter
    def coins(self, value):
        if value < 0:
            self.__coins = 0
        else:
            self.__coins = value

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self):
        pass

    def add_card(self, card):
        self.cards.append(card)

    @property
    def hand(self):
        return self.__hand

    @hand.setter
    def hand(self):
        pass

    def add_hidden_card(self, Hidden):
        self.hand.append(Hidden)

    def reveal_card(self):
        print(self.name)
        for i in range(len(self.cards)):
            print(f"{i}.- {self.cards[i].name}")
        position = int(input("Choose card index to reveal\n"))
        if not self.cards[position].usable:
            raise DeadCard("This card is dead")
        self.cards[position].kill_card()
        self.hand[position] = self.cards[position]

    @property
    def alive(self):
        return self.__alive

    @alive.setter
    def alive(self):
        pass

    def kill_player(self):
        self.__alive = False

    def remove_card(self):
        for i in range(len(self.cards)):
            print(f"{i}.- {self.cards[i].name}")
        index = int(input("Choose card index to remove\n"))
        self.cards.pop(index)
        self.hand.pop(index)

    def remove_card_challenged(self, card):
        influences = []
        for i in self.cards:
            influences.append(type(i))
        index = influences.index(type(card))
        self.cards.pop(index)
        self.hand.pop(index)
        return card

    def show_player_open(self):
        cards = ""
        for pos in range(len(self.cards)):
            n = self.cards[pos].name
            cards += f"{n}, "
        cards = cards[:-2]
        print(f"{self.name} - Coins: {self.coins} - Cards: {cards}")

    def check_for_card(self, card):
        actions = []
        card = type(card)
        for influence in self.cards:
            actions.append(type(influence))
        if card in actions:
            return True
        else:
            return False
