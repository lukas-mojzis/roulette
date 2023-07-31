import random, math, time, datetime

class Player:
    def __init__(self):
        # Give player default amount of money
        self.money = 1000

    def dollars(self, number):
        # Return singular "dollar" if amount is 1, otherwise return plural "dollars"
        if number == 1:
            return "dollar"
        return "dollars"

class Welcome:
    def __init__(self):
        # Instantiate global "player" object and start mechanism with "print_welcome" function
        global player
        player = Player()

        self.print_welcome()

    def print_welcome(self):
        print(f"\nWelcome to the casino! You have arrived with {player.money:,} {player.dollars(player.money)}.")

        # Print highscore if it exists
        try:
            with open("highscore.txt") as highscore:
                print(f"\nYour best ever result was when you left the casino with {int(highscore.readline().strip()):,} dollars on {highscore.readline()}.")
        except FileNotFoundError:
            pass

        time.sleep(1)
        
        # Continue mechanism by instantiating "setup" object
        setup = Setup()

class Setup:
    def __init__(self):
        self.game_type_choice()

    def game_type_choice(self):
        # Input decision on game type
        while True:
            try:
                self.game_type = int(input("""\

What type of bet would you like to make?

Outside bets:
-------------
(1): low or high
(2): red or black
(3): even or odd
(4): dozen
(5): column
(6): snake

Inside bets:
------------
(7): single
(8): split
(9): street
(10): corner
(11): double street
(12): trio
(13): first four

"""))
                if self.game_type not in range(1, 14):
                    raise ValueError
            except ValueError:
                print("Invalid answer. Please enter a whole number within the interval 1-13.")
                continue
            break

        # Instantiate "game" object of appropriate class and with appropriate argument according to chosen game type
        # "options" dictionary always contains name and range of every option, written as comprehension where suitable

        if self.game_type == 1:
        # Low or high
            self.options = {"low numbers": range(1, 19), "high numbers": range(19, 37)}
            self.game = Game_Standard_Outside(self.options)
        elif self.game_type == 2:
        # Red or black
            self.options = {"red numbers": [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36], "black numbers": [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]}
            self.game = Game_Standard_Outside(self.options)
        elif self.game_type == 3:
        # Even or odd
            self.options = {"even numbers": range(2, 38, 2), "odd numbers": range(1, 37, 2)}
            self.game = Game_Standard_Outside(self.options)
        elif self.game_type == 4:
        # Dozen
            self.options = {"first dozen": range(1, 13), "second dozen": range(13, 25), "third dozen": range(25, 37)}
            self.game = Game_Standard_Outside(self.options)
        elif self.game_type == 5:
        # Column
            self.options = {"left column": range(1, 37, 3), "middle column": range(2, 38, 3), "right column": range(3, 39, 3)}
            self.game = Game_Standard_Outside(self.options)
        elif self.game_type == 6:
        # Snake
            self.options = {"snake": [1, 5, 9, 12, 14, 16, 19, 23, 27, 30, 32, 34]}
            self.game = Game_Snake(self.options)
        elif self.game_type == 7:
        # Single
            self.options = {f"number {x}": [x] for x in range(37)}
            self.game = Game_Single(self.options)
        elif self.game_type == 8:
        # Split
            self.options = {f"split {x}-{x+1}": [x, x+1] for x in range(1, 36) if x % 3 > 0} | {f"split {x}-{x+3}": [x, x+3] for x in range(1, 34)}
            self.game = Game_Standard_Inside(self.options)
        elif self.game_type == 9:
        # Street
            self.options = {f"street {x}-{x+1}-{x+2}": range(x, x+3) for x in range(1, 37, 3)}
            self.game = Game_Standard_Inside(self.options)
        elif self.game_type == 10:
        # Corner
            self.options = {f"corner {x}-{x+1}-{x+3}-{x+4}": [x, x+1, x+3, x+4] for x in range(1, 33) if x % 3 > 0}
            self.game = Game_Standard_Inside(self.options)
        elif self.game_type == 11:
        # Double street
            self.options = {f"double street {x}-{x+1}-{x+2}-{x+3}-{x+4}-{x+5}": range(x, x+6) for x in range(1, 34, 3)}
            self.game = Game_Standard_Inside(self.options)
        elif self.game_type == 12:
        # Trio
            self.options = {"trio 0-1-2": [0, 1, 2], "trio 0-2-3": [0, 2, 3]}
            self.game = Game(self.options)
        else:
        # First four
            self.options = {"first four": [0, 1, 2, 3]}
            self.game = Game_Snake(self.options)

class Game:
    def __init__(self, options):
        # Create necessary variables based on "options" argument and start game mechanism with "bet_range_choice" function
        self.options = options
        self.options_keys = list(self.options.keys())

        self.bet_range_choice()

    def bet_range_choice(self):
        # Default function - "Single" and "Snake" classes use their own instead

        # Create numbered list of all keys from "options" dictionary
        # Numbers start at # 1 while indexes start at # 0 so adjustment by +1 is necessary
        self.options_list = [f"({self.options_keys.index(option) + 1}): {option}" for option in self.options_keys]

        # Join list into one string with each available option on new line
        self.options_string = "\n".join(self.options_list)

        # Input decision on which option to bet on
        while True:
            try:
                self.bet_option = int(input(f"""\

What range of numbers would you like to bet on?

{self.options_string}

"""))
                if self.bet_option not in range(1, len(self.options_keys) + 1):
                    raise ValueError
            except ValueError:
                print(f"Invalid answer. Please enter a whole number within the interval 1-{len(self.options_keys)}.")
                continue
            break

        # Create "bet_range" variable storing key of option chosen by player
        # Numbers in "options_list" start at # 1 so adjustment by -1 is necessary to get correct index
        self.bet_range = self.options_keys[self.bet_option - 1]

        self.bet_amount_choice()

    def bet_amount_choice(self):
        # Input bet amount
        while True:
            try:
                self.bet_amount = int(input(f"\nHow much money would you like to bet? You have {player.money:,} {player.dollars(player.money)} available.\n"))
                if self.bet_amount not in range(1, player.money + 1):
                    raise ValueError
            except ValueError:
                print(f"Invalid answer. Please enter a whole number within the interval 1-{player.money:,}.")
                continue
            break

        self.draw_number()

    def draw_number(self):
        time.sleep(0.5)

        # Print confirmation of bet details
        print(f"\nYou have bet {self.bet_amount:,} {player.dollars(self.bet_amount)} on the {self.bet_range}.")

        time.sleep(1)

        # Print messages with pauses to increase drama before continuing
        print("\nThe wheel is spinning!")
        time.sleep(1)
        print("\n.")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")

        # Draw random number
        self.drawn_number = random.randint(0, 36)

        self.print_drawn_number()

    def print_drawn_number(self):
        # Default function - "Standard Outside", "Standard Inside" and "Single" classes use their own instead

        time.sleep(1)

        # Print drawn number and info on whether it is within or outside of range of bet
        if self.drawn_number in self.options[self.bet_range]:
            print(f"\nNumber {self.drawn_number} (within the {self.bet_range}) was drawn!")
        else:
            print(f"\nNumber {self.drawn_number} (outside of the {self.bet_range}) was drawn!")

        self.evaluate_bet()

    def evaluate_bet(self):
        time.sleep(1)

        if self.drawn_number in self.options[self.bet_range]:
            # Drawn number is within range of bet - player wins
            # Winnings are calculated based on size of range of bet (how many numbers are winning)
            # Since all ranges for given game type are of same size, length of first one is used
            # Multiplicator value is reduced by 1 in order to get only net winnings (excluding amount of bet itself)
            self.multiplicator = 36 // len(list(self.options.values())[0]) - 1
            self.winnings = self.bet_amount * self.multiplicator
            player.money += self.winnings
            print(f"\nCongratulations, you have won {self.winnings:,} {player.dollars(self.winnings)}! You now have {player.money:,} {player.dollars(player.money)}.")

        elif self.drawn_number == 0 and len(list(self.options.values())[0]) == 18:
            # Number 0 is drawn and game type has 2 options of 18 numbers - player loses only half of bet (rounded up)
            self.loss = math.ceil(self.bet_amount / 2)
            player.money -= self.loss
            print(f"\nYou have lost {self.loss:,} {player.dollars(self.loss)}! You have {player.money:,} {player.dollars(player.money)} left.")

        else:
            # Drawn number is outside range of bet - player loses entire bet
            player.money -= self.bet_amount
            print(f"\nYou have lost {self.bet_amount:,} {player.dollars(self.bet_amount)}! You have {player.money:,} {player.dollars(player.money)} left.")

        self.play_again()

    def play_again(self):
        time.sleep(1)

        # If player has no more money, print goodbye message and end session
        if player.money == 0:
            print("\nYou have lost all your money! You have been kicked out of the casino.\n")

        # Otherwise input decision whether to play another game
        else:
            while True:
                try:
                    self.play_again_decision = int(input("""\

Would you like to play again?

(1): yes
(2): no

"""))
                    if self.play_again_decision not in range(1, 3):
                        raise ValueError
                except ValueError:
                    print("Invalid answer. Please enter a whole number within the interval 1-2.")
                    continue
                break

            if self.play_again_decision == 1:
                # Start new game at "setup"
                setup = Setup()
            else:
                print(f"See you later then! You are leaving the casino with {player.money:,} {player.dollars(player.money)}.\n")

                # If highscore file exists, update highscore and date if current score is equal or higher
                try:
                    with open("highscore.txt") as highscore:
                        if player.money >= int(highscore.readline()):
                            with open("highscore.txt", "w") as highscore:
                                highscore.writelines([f"{player.money}\n", f"{datetime.date.today().strftime('%d %b %Y')}"])
                            time.sleep(1)
                            print("Congratulations, this is your best ever result!\n")

                # If highscore file doesn't exist, create one with current score and date
                except FileNotFoundError:
                    with open("highscore.txt", "w") as highscore:
                        highscore.writelines([f"{player.money}\n", f"{datetime.date.today().strftime('%d %b %Y')}"])                                            

class Game_Standard_Outside(Game):
    # Game types # 1, 2, 3, 4, 5

    def __init__(self, options):
        super().__init__(options)

    def print_drawn_number(self):
        time.sleep(1)

        # Number 0 doesn't belong to any option - print only drawn number
        if self.drawn_number == 0:
            print("\nNumber 0 was drawn!")
        # Any number other than 0 belongs to exactly one option - find that option and print it alongside drawn number
        else:
            for option, option_range in self.options.items():
                if self.drawn_number in option_range:
                    self.drawn_number_range = option
                    break
            print(f"\nNumber {self.drawn_number} ({self.drawn_number_range}) was drawn!")

        self.evaluate_bet()

class Game_Standard_Inside(Game):
    # Game types # 8, 9, 10, 11

    def __init__(self, options):
        super().__init__(options)

    def print_drawn_number(self):
        time.sleep(1)

        # Number 0 doesn't belong to any option - print only drawn number
        if self.drawn_number == 0:
            print("\nNumber 0 was drawn!")
        # Any number other than 0 belongs to at least one option
        # Print drawn number and info on whether it is within or outside of range of bet
        elif self.drawn_number in self.options[self.bet_range]:
            print(f"\nNumber {self.drawn_number} (within the {self.bet_range}) was drawn!")
        else:
            print(f"\nNumber {self.drawn_number} (outside of the {self.bet_range}) was drawn!")

        self.evaluate_bet()

class Game_Single(Game):
    # Game type # 7

    def __init__(self, options):
        super().__init__(options)

    def bet_range_choice(self):
        # Input decision on which single number to bet on (0-36) - printing full list of options is not necessary
        while True:
            try:
                self.bet_option = int(input("\nWhat number would you like to bet on (0-36)?\n"))
                if self.bet_option not in range(37):
                    raise ValueError
            except ValueError:
                print("Invalid answer. Please enter a whole number within the interval 0-36.")
                continue
            break

        # Create "bet_range" variable storing key of option chosen by player
        # List of options starts at # 0 (lowest number to bet on), not # 1
        # Therefore, value of each option corresponds to its own index and no -1 adjustment is necessary to get index
        self.bet_range = self.options_keys[self.bet_option]

        self.bet_amount_choice()

    def print_drawn_number(self):
        time.sleep(1)

        # Print only drawn number, no range info necessary
        print(f"\nNumber {self.drawn_number} was drawn!")

        self.evaluate_bet()

class Game_Snake(Game):
    # Game types # 6, 13

    def __init__(self, options):
        super().__init__(options)

    def bet_range_choice(self):
        # Only one option available, no input needed
        self.bet_range = self.options_keys[0]

        self.bet_amount_choice()

# Run entire session mechanism via instantiating "Welcome" class
welcome = Welcome()