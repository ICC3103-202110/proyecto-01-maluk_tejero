from actions import Income, ForeignAid, Coup, Duke, Assassin, Ambassador
from actions import Captain, Countess, Hidden
from random import shuffle


class Deck:
    def __init__(self):
        self.__cards = []
        self.__actions = [Income(), ForeignAid(), Coup(), Duke(), Assassin(),
                          Ambassador(), Captain(), Countess(), Hidden()]

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self, value):
        pass

    @property
    def actions(self):
        return self.__actions

    @actions.setter
    def actions(self):
        pass

    def build(self):
        for j in range(3):
            for i in [Duke(), Assassin(), Ambassador(), Captain(), Countess()]:
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

    def add_card_deck(self, card):
        self.cards.append(card)
