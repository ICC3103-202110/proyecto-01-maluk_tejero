from errors import InvalidTarget


class Action:
    name = ""
    description = ""
    blocks = ""
    coinsRequired = 0

    def __init__(self):
        self.__usable = True

    @property
    def usable(self):
        return self.__usable

    @usable.setter
    def usable(self):
        pass

    def kill_card(self):
        self.__usable = False


class Income(Action):
    name = "Income"
    description = "The player gets a coin."

    def act(self, player):
        player.coins += 1
        print(f"{player.name} used Income, receives 1 coin.")


class Coup(Action):
    name = "Coup"
    description = "Pay 7 coins, choose player to lose influence"
    coinsRequired = 7

    def act(self, player, target):
        if not target.alive:
            print(f"Target is not alive")
            raise InvalidTarget
        player.coins -= self.coinsRequired
        print(f"{target.name} loses an influence due to Coup "
              f"played by {player.name}")
        target.reveal_card()


class Duke(Action):
    name = "Duke"
    action = "Tax"
    description = "Take 3 coins."
    blocks = "Foreign Aid"

    def act(self, player):
        player.coins += 3
        print(f"{player.name} used Tax. He received 3 coins.")


class ForeignAid(Action):
    name = "Foreign Aid"
    description = "The player gets 2 coins (This action can "\
                  "be blocked by the Duke)."
    blocked_by = [Duke()]

    def act(self, player):
        player.coins += 2
        print(f"{player.name} used Foreign Aid, receives 2 coins.")


class Countess(Action):
    name = "Countess"
    description = "Blocks assassination"
    blocks = "Assassin"


class Assassin(Action):
    name = "Assassin"
    action = "Assassinate"
    description = "Pay 3 coins, choose player to lose influence"
    coinsRequired = 3
    blocked_by = [Countess()]

    def act(self, player, target):
        if player.coins >= self.coinsRequired:
            player.coins -= self.coinsRequired
            print(f"{target.name} lost an Influence to an Assassin")
            target.reveal_card()


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
        print(f"{player.name} used Exchange to swap cards with the Court Deck")


class Captain(Action):
    name = "Captain"
    action = "Steal"
    description = "Take 2 coins from another player"
    blocks = "Captain"
    blocked_by = [Ambassador(), "Captain"]

    def act(self, player, target):
        if target.coins >= 2:
            steal = 2
        elif target.coins <= 1:
            steal = target.coins
        print(f"{player.name} stole {steal} coins from {target.name}")
        target.coins -= steal
        player.coins += steal
        return steal


class Hidden(Action):
    name = "*"
    description = "Hidden card"
