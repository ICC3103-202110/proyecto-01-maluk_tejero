from actions import Duke, Assassin, Ambassador, Captain, Countess
from random import shuffle

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    

    def build(self):
        for i in [Duke.name, Assassin.name, Ambassador.name, Captain.name, Countess.name]:
            for j in range(3):
                self.cards.append(i)
    

    def shuffle_deck(self):
        shuffle(self.cards)


    def show_deck(self):
        for i in self.cards:
            print(i)
    
    
    def draw_card(self):
        card = self.cards[0]
        self.cards.pop(0)
        return card
