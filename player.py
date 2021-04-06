class Player:
    def __init__(self, name):
        self.__name = name
        self.__coins = 2
    
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
