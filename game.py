from player import Player
from deck import Deck
from random import choice
from errors import DeadCard


class Game:
    def __init__(self):
        self.__players = []
        self.__deck = Deck()
        self.deck.build()
        self.deck.shuffle_deck()
        self.__log = ["\n\nLog\n"]

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self):
        pass

    @property
    def deck(self):
        return self.__deck

    @deck.setter
    def deck(self):
        pass

    @property
    def log(self):
        return self.__log

    @log.setter
    def log(self):
        pass

    def add_log(self, txt):
        if len(txt) != 0:
            for line in txt:
                self.log.append(line)

    def create_player(self):
        name = str(input("What is your name?"))
        return Player(name)

    def create_all_players(self):
        num_of_players = int(input("How many players would "
                                   "like to play? 3 or 4\n"))
        if num_of_players not in [3, 4]:
            print("Number of players not allowed, "
                  "please choose between 3 or 4\n\n")
            self.create_all_players()
        else:
            for i in range(num_of_players):
                player = self.create_player()
                card1 = self.deck.draw_card()
                card2 = self.deck.draw_card()
                player.add_card(card1)
                player.add_card(card2)
                player.add_hidden_card(self.deck.hide())
                player.add_hidden_card(self.deck.hide())
                self.players.append(player)

    def show_players(self):
        print("\nPlayers:")
        print("Cards shown as * are playable, cards shown with their name are "
              "revealed and cannot be used or put back in the deck")
        for (i, _) in enumerate(self.players):
            card1_h = self.players[i].hand[0].name
            card2_h = self.players[i].hand[1].name
            print(f"{i}: {self.players[i].name} - "
                  f"Coins: {self.players[i].coins} - "
                  f"Hand: {card1_h}, {card2_h}")

    def choose_target(self, player):
        targets = self.players[:]
        targets.remove(player)
        print(f"Choose your target. By index")
        for target in targets:
            if target.alive:
                print(f"{targets.index(target)}. {target.name}")
        target = int(input())
        target = targets[target]
        return target

    def player_turn(self, player):
        if player.coins >= 10:
            return 3
        print(f"\n{player.name} turn")
        player.show_player_open()
        print("\nGeneral Actions")
        print("  0. Income")
        print("  1. Foreign Aid")
        print("  2. Coup")
        print("\nCharacter Actions")
        print("  3. Taxes")
        print("  4. Assassinate")
        print("  5. Exchange")
        print("  6. Steal\n")
        print("7. Show log")
        print("\nChoose your action index")
        return int(input())

    def ask_challenge(self, player, action):
        players_not_in_turn = self.players[:]
        players_not_in_turn.remove(player)
        challengers = []
        for player in players_not_in_turn:
            print(f"{player.name}")
            ask = str(input(f"Do you want to challenge {action.name}? (Y/N)"))
            if ask == "Y":
                challengers.append(player)

        if len(challengers) == 0:
            return False
        challenger = choice(challengers)
        return challenger

    def challenge(self, player, action):
        challenge_success = False
        action = self.deck.actions[action]
        challenger = self.ask_challenge(player, action)
        if challenger:
            player_has_card = player.check_for_card(action)
            if player_has_card:
                print(f"{player.name} has {action.name}")
                print(f"{challenger.name} loses the challenge")
                challenger.reveal_card()
                card_to_deck = player.remove_card_challenged(action)
                self.deck.add_card_deck(card_to_deck)
                self.deck.shuffle_deck()
                added_card = self.deck.draw_card()
                player.add_card(added_card)
                player.add_hidden_card(self.deck.actions[8])
                challenge_success = False
                # There is challenger
                # challenger loses
                # YES INITIAL ACTION
            else:
                print(f"{player.name} does not have {action.name}")
                print(f"{player.name} loses an influence")
                player.reveal_card()
                challenge_success = True
                # There is challenger
                # challenger wins
                # NO INITIAL ACTION
            self.remove_players_from_game()
        return challenge_success

    def ask_counter_action(self, player, action):
        players_not_in_turn = self.players[:]
        players_not_in_turn.remove(player)
        counter_attacker = []
        for player in players_not_in_turn:
            print(f"{player.name}")
            if action.name == "Captain":
                blocker_name = "Ambassador or Captain"
            else:
                blocker_name = action.blocked_by[0].name
            ask = str(input(f"Do you want to counter attack {action.name}"
                            f"? For this you need {blocker_name} (Y/N)"))
            if ask == "Y":
                counter_attacker.append(player)
        if len(counter_attacker) == 0:
            return False
        counter_attacker = choice(counter_attacker)
        return counter_attacker

    def counter_action(self, player, action):
        txt = []
        counter_success = False
        counter_attacker = self.ask_counter_action(player, action)
        if counter_attacker:
            blocker = action.blocked_by
            if len(blocker) > 1:
                print(f"Which blocker do you have?")
                print(f"0. {self.deck.actions[5].name}")
                print(f"1. {self.deck.actions[6].name}")
                blocker_final = int(input()) + 5
            else:
                for i in self.deck.actions:
                    if isinstance(blocker[0], type(i)):
                        blocker_final = self.deck.actions.index(i)
            challenger = self.ask_challenge(
                counter_attacker, self.deck.actions[blocker_final])
            if challenger:
                counter_attacker_has_card = counter_attacker.check_for_card(
                    self.deck.actions[blocker_final])
                if counter_attacker_has_card:
                    print(f"{counter_attacker.name} says he has "
                          f"{self.deck.actions[blocker_final].name}")
                    challenger.reveal_card()
                    self.remove_players_from_game()
                    card_to_deck = counter_attacker.remove_card_challenged(
                        self.deck.actions[blocker_final])
                    if not card_to_deck.usable:
                        raise DeadCard("Dead card can't be returned to deck")
                    self.deck.add_card_deck(card_to_deck)
                    self.deck.shuffle_deck()
                    added_card = self.deck.draw_card()
                    counter_attacker.add_card(added_card)
                    counter_attacker.add_hidden_card(self.deck.actions[8])
                    counter_success = True
                    # There is counterAttacker
                    # There is challenger
                    # Challenger loses
                    # NO INITIAL ACTION

                else:
                    print(f"{counter_attacker.name} does not have "
                          f"{self.deck.actions[blocker_final].name}")
                    print(f"{counter_attacker.name} loses an influence")
                    counter_attacker.reveal_card()
                    self.remove_players_from_game()
                    counter_success = False
                    # There is counterAttacker
                    # There is challenger
                    # Challenger wins
                    # YES INITIAL ACTION

            else:
                if isinstance(action, type(self.deck.actions[4])):
                    player.coins -= 3
                print(f"Counter attack by {counter_attacker.name} with "
                      f"{self.deck.actions[blocker_final].name} "
                      f"was successful")
                counter_success = True
                # There is counterAttacker
                # There is NO challenger
                # NO INITIAL ACTION

        else:
            print(f"{action.name} by {player.name} was not counter attacked.")
            counter_success = False
            # There is NO counterAttacker
            # YES INITIAL ACTION
        return counter_success

    def remove_players_from_game(self):
        for player in self.players:
            if player.hand == player.cards:
                player.kill_player()
                print(f"{player.name} was killed because "
                      f"he has no influence left")
                self.players.remove(player)

    def check_winner(self):
        if len(self.players) == 1:
            return True
        else:
            return False

    def start(self):
        turn = 1
        while len(self.players) > 1:
            txt = [f"Turn {turn}"]
            for player in self.players:
                if self.check_winner():
                    continue
                self.show_players()
                if player.alive:
                    if player.coins >= 10:
                        print(f"\n{player.name} turn")
                        print(f"{player.name} is forced to play Coup because "
                              f"he has 10 or more coins")
                        action = 2
                    else:
                        action = self.player_turn(player)

                    while action == 7:
                        for line in self.log:
                            print(line)
                        action = self.player_turn(player)

                    if action == 0:
                        self.deck.actions[action].act(player)
                        txt.append(f"{player.name} uses Income, "
                                   "receives 1 coin")

                    elif action == 1:
                        txt.append(f"{player.name} uses Foreign Aid")
                        counter_success = self.counter_action(
                            player, self.deck.actions[action])
                        if counter_success:
                            self.remove_players_from_game()
                            continue
                        else:
                            self.deck.actions[action].act(player)

                    elif action == 2:
                        if player.coins < 7:
                            raise ValueError(
                                "Not enough coins. Coins required = 7")
                        target = self.choose_target(player)
                        self.deck.actions[action].act(player, target)
                        txt.append(f"{player.name} used Coup "
                                   f"against {target.name}")

                    elif action == 3:
                        txt.append(f"{player.name} uses Taxes")
                        challenge_success = self.challenge(player, action)
                        if challenge_success:
                            self.remove_players_from_game()
                            continue
                        else:
                            self.deck.actions[action].act(player)
                            txt.append(f"{player.name} receives 3 coins "
                                       f"from taxes.")

                    elif action == 4:
                        txt.append(f"{player.name} uses Assassinate")
                        if player.coins < 3:
                            raise ValueError(
                                "Not enough coins. Coins required = 3")
                        challenge_success = self.challenge(player, action)
                        if challenge_success:
                            self.remove_players_from_game()
                            continue

                        counter_action = self.counter_action(
                            player, self.deck.actions[action])

                        if counter_action:
                            pass
                        else:
                            target = self.choose_target(player)
                            card_killed = self.deck.actions[action].act(player,
                                                                        target)
                            txt.append(f"{target.name} lost an Influence: "
                                       f"{card_killed} to an Assassin")
                            txt.append(f"{player.name} pays 3 coins "
                                       f"for Assassination")

                    elif action == 5:
                        txt.append(f"{player.name} used Exchange")
                        challenge_success = self.challenge(player, action)
                        if challenge_success:
                            self.remove_players_from_game()
                            continue
                        else:
                            self.deck.actions[action].act(player, self.deck)
                            txt.append(f"{player.name} exchanged cards "
                                       f"with the Court Deck")

                    elif action == 6:
                        txt.append(f"{player.name} uses Steal")
                        challenge_success = self.challenge(player, action)
                        if challenge_success:
                            self.remove_players_from_game()
                            continue
                        else:
                            counter_action = self.counter_action(
                                player, self.deck.actions[action])
                            if counter_action:
                                pass
                            else:
                                target = self.choose_target(player)
                                steal = self.deck.actions[action].act(
                                                                player, target)
                                txt.append(f"{player.name} stole {steal} "
                                           f"coins from {target.name}")

                    self.remove_players_from_game()
                    wait = input("Press enter for next turn")
                    print("\n" * 100)
            self.add_log(txt)
            self.add_log(["\n"])
            turn += 1
        print(f"{self.players[0].name} wins")
