from deck import Deck

class Player:
    def __init__(self, name):
        self.__name = name
        self.__coins = 2
        self.__cards = []
    

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
    
