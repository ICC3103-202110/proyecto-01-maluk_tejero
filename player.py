class Player:
    def __init__(self, name):
        self.__name = name
        self.__coins = 2
        self.__cards = []
        self.__hand = []
    

    @property
    def name(self):
        return self.__name
    

    @property
    def coins(self):
        return self.__coins
    

    @coins.setter
    def coins(self, value):
        if self.__coins + value < 0:
            self.__coins = 0
        else:
            self.__coins += value
    

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
    

    def reveal_card(self, position):
        self.hand[position] = self.cards[position]
