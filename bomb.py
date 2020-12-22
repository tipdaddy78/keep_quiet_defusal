import sys
from modules import *


def defuse():
    parallel = False
    even = False
    vowel = False
    frk = False
    car = False
    strikes = 0
    module = ""

    batteries = int(input("How many batteries? \n"))

    if input("Is there a Parallel port?\n") == "y":
        parallel = True

    #Serial Port info
    if input("Even serial?\n") == "y":
        even = True
    if input("Vowel in serial?\n") == "y":
        vowel = True

    #Indicator Info
    if input("Lit FRK indicator?\n") == "y":
        frk = True
    if input("Lit CAR indicator?\n") == "y":
        car = True

    found_module = False
    while module != "defused":
        module = input("Which module? \n")

        if module == "strike":
            strikes += 1
            print("You now have", strikes, "strike(s)")
        if module == "wires" or module == "simple wires":
            found_module = True
            print(simple_wires(even), "\n")
        if module == "button" or module == "hold button":
            found_module = True
            if button(batteries, car, frk):
                print("HOLD")
                print("Blue, 4")
                print("Yellow, 5")
                print("Other, 1\n")
            else:
                print("Press and release\n")
        if module == "symbols":
            found_module = True
            symbols()
        if module == "simon" or module == "simonsays":
            found_module = True
            simon_says(strikes, vowel)
        if module == "first":
            found_module = True
            whos_on_first()
        if module == "memory":
            found_module = True
            memory()
        if module == "morse":
            found_module = True
            morse_code()
        if module == "complicated_wires":
            found_module = True
            complicated_wires(parallel, even, batteries)
        if module == "wire_sequence":
            found_module = True
            wire_sequence()
        if module == "defused":
            found_module = True
            continue
        if not found_module:
            print("I didn't recognize that module")


    print("Wow wow wow")


defuse()




