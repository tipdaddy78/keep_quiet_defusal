from modules.simple_wires import *
from modules.button import *
from modules.symbols import *
from modules.simon import *
from modules.first import *
from modules.memory import *
from modules.morse import *
from modules.comp_wires import *
from modules.wire_sequence import *
from modules.password import *

class Bomb:
    def __init__(self):
        self.parallel = False
        self.last_digit_even = False
        self.serial_has_vowel = False
        self.frk_indicator = False
        self.car_indicator = False
        self.batteries = 0
        self.strikes = 0

    def get_properties(self):
        print("The program will now ask you some details about the bomb.")
        #Get the number of batteries on the bomb.
        while 1:
            i = input("How many batteries does the bomb have?\n")
            if not i.isnumeric():
                print("Please input a numeric value.")
            else:
                self.batteries = int(i)
                break
        #Get if the bomb has a parallel port
        while 1:
            i = input("Is there a Parallel port on the bomb? y/n \n").lower()
            if i != "y" and i != "n":
                print("Invalid entry. Please enter y or n")
                continue
            elif i == "y":
              self.parallel = True
            break
        #Get if the serial number ends in a vowel
        while 1:
            i = input("Does the serial number end in an even number? y/n\n").lower()
            if i != "y" and i != "n":
                print("Invalid entry. Please enter y or n")
                continue
            elif i == "y":
              self.last_digit_even = True
            break
        #Get if the serial number has a vowel
        while 1:
            i = input("Does the serial number contain a vowel? y/n \n")
            if i != "y" and i != "n":
                print("Invalid entry. Please enter y or n")
                continue
            elif i == "y":
              self.serial_has_vowel = True
            break
        # Get if there is a lit FRK indicator
        while 1:
            i = input("Does the bomb have a lit FRK indicator? y/n \n")
            if i != "y" and i != "n":
                print("Invalid entry. Please enter y or n")
                continue
            elif i == "y":
                self.frk_indicator = True
            break
        # Get if there is a lit CAR indicator
        while 1:
            i = input("Does the bomb have a lit CAR indicator? y/n \n")
            if i != "y" and i != "n":
                print("Invalid entry. Please enter y or n")
                continue
            elif i == "y":
                self.car_indicator = True
            break
        print("Thanks for entering those details.")
        return

    def defuse(self):
        print("You can now begin defusing your bomb modules in any order you'd like.")
        m = ""
        found_module = False
        while m != "defused":
            if (self.strikes == 3):
                print("OH NO! YOU BLEW UP\n")
                while 1:
                    i = input("Would you like to restart? y/n\n")
                    if i != "y" and i != "n":
                        print("Invalid entry. Please enter y or n")
                        continue
                    elif i == "y":
                        return 1
                    elif i == "n":
                        return -1

            m = input("\nWhich module? Type 'modules' if you need the options.\n")

            if m == 'modules':
                self.print_modules()
            elif m == "strike":
                self.add_strike()
                if (self.strikes == 3):
                    print("OH NO! YOU BLEW UP\n")
                    while 1:
                        i = input("Would you like to restart? y/n\n")
                        if i != "y" and i != "n":
                            print("Invalid entry. Please enter y or n")
                            continue
                        elif i == "y":
                            return 1
                        elif i == "n":
                            return -1
                print("You now have", self.strikes, "strike(s)")
            if m == "wires":
                found_module = True
                solve_simple_wires(self.last_digit_even)
                print("\n")
            if m == "button":
                found_module = True
                solve_button(self.batteries, self.car_indicator, self.frk_indicator)
            if m == "symbols":
                found_module = True
                solve_symbols()
            if m == "simon":
                found_module = True
                simon_says(self)
            if m == "first":
                found_module = True
                solve_whos_on_first()
            if m == "memory":
                found_module = True
                solve_memory(self)
            if m == "morse":
                found_module = True
                solve_morse_code()
            if m == "complicated":
                found_module = True
                solve_complicated_wires(self)
            if m == "sequence":
                found_module = True
                solve_wire_sequence()
            if m == "password":
                found_module = True
                solve_password()
            if m == "defused":
                found_module = True
                continue
            if not found_module:
                print("I didn't recognize that module")
        print("Congratulations on defusing the bomb!")
        while 1:
            i = input("Would you like to restart? y/n")
            if i != "y" and i != "n":
                print("Invalid entry. Please enter y or n")
                continue
            elif i == "y":
                return 1
            elif i == "n":
                return -1

    def add_strike(self):
        self.strikes += 1
        print("STRIKE ADDED\n")
        print("Now at " + str(self.strikes) + " strikes.")

    def print_modules(self):
        print("Type which module you'd like to defuse from the following options:")
        print("\t \"wires\" for Simple Wires module.")
        print("\t \"button\" for the Button module.")
        print("\t \"symbols\" for the Keypad Symbols module.")
        print("\t \"simon\" for the Simon Says module.")
        print("\t \"first\" for the Who's on First module")
        print("\t \"memory\" for the Memory module")
        print("\t \"morse\" for the Morse Code module")
        print("\t \"complicated\" for the Complicated Wires module")
        print("\t \"sequence\" for the Wire Sequence module")
        print("\t \"strike\" If you caused a strike")
        print("or \t \"defused\" if the bomb is now defused.\n")

def run():
    print("Welcome to the auto-bomb defusal program")
    print("Please note needy modules aside from knobs must be attended to manually.")
    b = Bomb()
    b.get_properties()
    while 1:
        d = b.defuse()
        if (d == 1):
            b = Bomb()
            b.get_properties()
        else:
            print("Thanks for using the program.")
            break

run()
