class Action:
    name = ""
    description = ""
    blocks = ""
    coinsRequired = 0
    

class Income(Action):
    name = "Income"
    description = "The player gets a coin."

    def play(self, player):
        player.coins += 1


class ForeignAid(Action):
    name = "Foreign Aid"
    description = "The player gets 2 coins (This action can be blocked by the Duke)."
    
    def play(self, player):
        player.coins += 2


class Coup(Action):
    name = "Coup"
    description = "Pay 7 coins, choose player to lose influence"
    coinsRequired = 7


class Duke(Action):
    name = "Duke - Tax"
    description = "Take 3 coins."
    blocks = "Foreing Aid"

    def play(self, player):
        player.coins += 3


class Assassin(Action):
    name = "Assassin - Assassinate"
    description = "Pay 3 coins, choose player to lose influence"
    coinsRequired = 3


class Ambassador(Action):
    name = "Ambassador - Exchange"
    description = "Exchange cards with Court Deck"
    blocks = "Captain - Steal"


class Captain(Action):
    name = "Captain - Steal"
    description = "Take 2 coins from another player"
    blocks = "Captain - Steal"

    def play(self, player, target = None):
        if target == None:
            raise None

        steal = 0
        if target.coins >=


class Countess(Action):
    name = "Countess"
    blocks = "Assassin - Assassinate"
