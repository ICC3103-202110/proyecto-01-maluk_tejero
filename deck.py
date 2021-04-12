from actions import Duke, Assassin, Ambassador, Captain, Countess, Hidden
from random import shuffle

class Deck:
    def __init__(self):
        self.__cards = []
        
    @property
    def cards(self):
        return self.__cards
    
    @cards.setter
    def cards(self, value):
        pass


    def build(self):
        for i in [Duke, Assassin, Ambassador, Captain, Countess]:
            for j in range(3):
                self.cards.append(i)
    

    def shuffle_deck(self):
        shuffle(self.cards)


    def show_deck(self):
        for i in self.cards:
            print(i.name)
    
    
    def draw_card(self):
        card = self.cards[0]
        self.cards.pop(0)
        return card
    
    def hide(self):
        return Hidden
