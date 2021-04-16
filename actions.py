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

    def act(self, player, target)
        if player.coins >= self.coinsRequired:
            player.coins -= 3
            target.remove_card()

        else:
            print(f"Not enough coins. Coins required = {coinsRequired}")
            

class Ambassador(Action):
    name = "Ambassador"
    action = "Exchange"
    description = "Exchange cards with Court Deck"
    blocks = "Captain"


class Captain(Action):
    name = "Captain"
    action = "Steal"
    description = "Take 2 coins from another player"
    blocks = "Captain - Steal"


class Countess(Action):
    name = "Countess"
    blocks = "Assassin"


class Hidden(Action):
    name = "*"
    description = "Hidden card"
