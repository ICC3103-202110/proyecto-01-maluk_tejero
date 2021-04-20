from errors import *

class Action:
    name = ""
    description = ""
    blocks = ""
    coinsRequired = 0
    

class Income(Action):
    name = "Income"
    description = "The player gets a coin."

    def act(self, player):
        player.coins += 1
        print(f"{player.name} used Income, receives 1 coin.")


class ForeignAid(Action):
    name = "Foreign Aid"
    description = "The player gets 2 coins (This action can be blocked by the Duke)."
    
    def act(self, player):
        player.coins += 2
        print(f"{player.name} receives 2 coins.")


class Coup(Action):
    name = "Coup"
    description = "Pay 7 coins, choose player to lose influence"
    coinsRequired = 7

    def act(self, player, target)
        if player.coins < self.coinsRequired:
            print(f"Not enough coins. Coins required = {coinsRequired}")
            raise ValueError("Not enough coins")
        if not target.alive:
            print(f"Target is not alive")
            raise InvalidTarget
        player.coins -= coinsRequired
        target.remove_card()



class Duke(Action):
    name = "Duke"
    action = "Tax"
    description = "Take 3 coins."
    blocks = "Foreign Aid"

    def act(self, player):
        player.coins += 3
        print(f"{player.name} used Tax. He stole 3 coins.")


class Assassin(Action):
    name = "Assassin"
    action = "Assassinate"
    description = "Pay 3 coins, choose player to lose influence"
    coinsRequired = 3

    def act(self, player, target):
        if player.coins >= self.coinsRequired:
            player.coins -= self.coinsRequired
            print(target.name)
            target.remove_card()

        else:
            print(f"Not enough coins. Coins required = {coinsRequired}")
            raise ValueError("Not enough coins")

class Ambassador(Action):
    name = "Ambassador"
    action = "Exchange"
    description = "Exchange cards with Court Deck"
    blocks = "Captain"

    def act(self, player, deck):
        start_cards = len(player.cards)
        player.add_card(deck.draw_card())
        player.add_card(deck.draw_card())
        player.add_hidden_card(deck.actions[8])
        player.add_hidden_card(deck.actions[8])
        end_cards = len(player.cards)
        while end_cards != start_cards:
            player.remove_card()
            end_cards = len(player.cards)
        



class Captain(Action):
    name = "Captain"
    action = "Steal"
    description = "Take 2 coins from another player"
    blocks = "Captain - Steal"

    def act(self, player, target):
        if target.coins >= 2:
            steal = 2
        elif target.coins <= 1:
            steal = target.coins
        
        target.coins -= steal
        player.coins += steal


class Countess(Action):
    name = "Countess"
    description = "Blocks assassination"
    blocks = "Assassin"


class Hidden(Action):
    name = "*"
    description = "Hidden card"
