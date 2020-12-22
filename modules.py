def simple_wires(even):
    wires_solved = False
    while not wires_solved:
        print("Please input the first letter of the color of the wires from top to bottom\n", "Use b for black and u for blue\n")
        wire_string = input("Wirestring?\n")
        wire_string = str(wire_string).lower()
        invalid = "acdefghijklmnopqstvxz0123456789"
        if any((i in invalid) for i in wire_string):
            print("You included invalid characters. \n")
            continue
        if len(wire_string) == 3:
            if wire_string.find('r') == -1:
                print("Cut the second wire")
            elif wire_string[2] == 'w':
                print("Cut the last wire")
            elif wire_string.count('u') > 1:
                print("Cut the last blue wire")
            else:
                print("Cut the last wire")
            wires_solved = True

        elif len(wire_string) == 4:
            if wire_string.count('r') > 1 and not even:
                print("Cut the last wire")
            elif 'r' not in wire_string and wire_string[3] == 'y':
                print("Cut the first wire")
            elif wire_string.count('u') == 1:
                print("Cut the first wire")
            elif wire_string.count('y') > 1:
                print("Cut the last wire")
            else:
                print("Cut the second wire")
            wires_solved = True

        elif len(wire_string) == 5:
            if wire_string[4] == 'b' and not even:
                print("Cut the fourth wire")
            elif wire_string.count('r') == 1 and wire_string.count('y') > 1:
                print("Cut the first wire")
            elif 'b' not in wire_string:
                print("Cut the second wire")
            else:
                print("Cut the first wire")
            wires_solved = True

        elif len(wire_string) == 6:
            if 'y' not in wire_string and not even:
                print("Cut the third wire")
            elif wire_string.count('y') == 1 and wire_string.count('w') > 1:
                print("Cut the fourth wire")
            elif 'r' not in wire_string:
                print("Cut the last wire")
            else:
                print("Cut the fourth wire")
            wires_solved = True

        else:
            print("That is not an acceptable length, please re-enter wirestring \n")
            continue

    return


def button(batteries, car, frk):
    button_color = input("What color is the button?\n").lower()
    button_text = input("What does the button say?\n").lower()

    if button_color == "blue" and button_text == "abort":
        return True
    elif batteries > 1 and button_text == "detonate":
        return False
    elif button_color == "white" and car:
        return True
    elif batteries > 2 and frk:
        return False
    elif button_color == "yellow":
        return True
    elif button_color == "red" and button_text == "hold":
        return False
    else:
        return True


def symbols():
    symbols_solved = False
    column1 = ["tennis", "at", "lambda", "lightning", "cat", "h", "back-c"]
    column2 = ["back-e", "tennis", "back-c", "squiggle", "white-star", "h", "question"]
    column3 = ["copyright", "nutsack", "squiggle", "ix", "r", "lambda", "white-star"]
    column4 = ["6", "paragraph", "b", "cat", "ix", "question", "smiley"]
    column5 = ["psi", "smiley", "b", "c", "paragraph", "snake", "black-star"]
    column6 = ["6", "back-e", "not-equal", "ae", "psi", "back-n", "omega"]
    columns = [column1, column2, column3, column4, column5, column6]

    while not symbols_solved:
        print("Please enter the symbols")
        symbol1 = input("Symbol 1?\n").lower()
        symbol2 = input("Symbol 2?\n").lower()
        symbol3 = input("Symbol 3?\n").lower()
        symbol4 = input("Symbol 4?\n").lower()
        symbols = [symbol1, symbol2, symbol3, symbol4]

        correct_column = -1

        for i in range(0, 6):
            if symbol1 in columns[i] and symbol2 in columns[i] and symbol3 in columns[i] and symbol4 in columns[i]:
                correct_column = i
                break

        if correct_column == -1:
            print("Looks like you entered a symbol I can't identify. Time to try again.\n")
            continue

        for i in range(0, 7):
            if columns[correct_column][i] in symbols:
                print(columns[correct_column][i])
                symbols_solved = True


def simon_says(strikes, vowel):
    while True:
        sequence = input("Please enter the sequence by first letter of the color, or 'done' if you are done.\n")
        if sequence == "done":
            return
        if sequence == "strike":
            strikes += 1
            continue
        invalid = "acdefhijklmnopqstuvwxz0123456789"
        if any((i in invalid) for i in sequence):
            print("You included invalid characters. \n")
            continue
        for i in sequence:
            if vowel:
                if strikes == 0:
                    if i == 'r':
                        print("Blue")
                    elif i == 'b':
                        print("Red")
                    elif i == 'g':
                        print("Yellow")
                    else:
                        print("Green")
                elif strikes == 1:
                    if i == 'r':
                        print("Yellow")
                    elif i == 'b':
                        print("Green")
                    elif i == 'g':
                        print("Blue")
                    else:
                        print("Red")
                else:
                    if i == 'r':
                        print("Green")
                    elif i == 'b':
                        print("Red")
                    elif i == 'g':
                        print("Yellow")
                    else:
                        print("Blue")
            else:
                if strikes == 0:
                    if i == 'r':
                        print("Blue")
                    elif i == 'b':
                        print("Yellow")
                    elif i == 'g':
                        print("Green")
                    else:
                        print("Red")
                elif strikes == 1:
                    if i == 'r':
                        print("Red")
                    elif i == 'b':
                        print("Blue")
                    elif i == 'g':
                        print("Yellow")
                    else:
                        print("Green")
                else:
                    if i == 'r':
                        print("Yellow")
                    elif i == 'b':
                        print("Green")
                    elif i == 'g':
                        print("Blue")
                    else:
                        print("Red")


def whos_on_first():
    display = dict()
    solutions = dict()

    display["yes"] = "mid-left"
    display["first"] = "top-right"
    display["display"] = "bot-right"
    display["okay"] = "top-right"
    display["says"] = "bot-right"
    display["nothing"] = "mid-left"
    display[""] = "bot-left"
    display["blank"] = "mid-right"
    display["no"] = "bot-right"
    display["led"] = "mid-left"
    display["lead"] = "bot-right"
    display["read"] = "mid-right"
    display["red"] = "mid-right"
    display["reed"] = "bot-left"
    display["leed"] = "bot-left"
    display["hold on"] = "bot-right"
    display["you"] = "mid-right"
    display["you are"] = "bot-right"
    display["your"] = "mid-right"
    display["you're"] = "mid-right"
    display["ur"] = "top-left"
    display["there"] = "bot-right"
    display["they're"] = "bot-left"
    display["their"] = "mid-right"
    display["they are"] = "mid-left"
    display["see"] = "bot-right"
    display["c"] = "top-right"
    display["cee"] = "bot-right"

    solutions["ready"] = "YES, OKAY, WHAT, MIDDLE, LEFT, PRESS, RIGHT, BLANK, READY"
    solutions["first"] = "LEFT, OKAY, YES, MIDDLE, NO, RIGHT, NOTHING, UHHH, WAIT, READY, BLANK, WHAT, PRESS, FIRST"
    solutions["no"] = "BLANK, UHHH, WAIT, FIRST, WHAT, READY, RIGHT, YES, NOTHING, LEFT, PRESS, OKAY, NO"
    solutions["blank"] = "WAIT, RIGHT, OKAY, MIDDLE, BLANK"
    solutions["nothing"] = "UHHH, RIGHT, OKAY, MIDDLE, YES, BLANK, NO, PRESS, LEFT, WHAT, WAIT, FIRST, NOTHING"
    solutions["yes"] = "OKAY, RIGHT, UHHH, MIDDLE, FIRST, WHAT, PRESS, READY, NOTHING, YES"
    solutions["what"] = "UHHH, WHAT"
    solutions["uhhh"] = "READY, NOTHING, LEFT, WHAT, OKAY, YES, RIGHT, NO, PRESS, BLANK, UHHH"
    solutions["left"] = "RIGHT, LEFT"
    solutions["right"] = "YES, NOTHING, READY, PRESS, NO, WAIT, WHAT, RIGHT"
    solutions["middle"] = "BLANK, READY, OKAY, WHAT, NOTHING, PRESS, NO, WAIT, LEFT, MIDDLE"
    solutions["okay"] = "MIDDLE, NO, FIRST, YES, UHHH, NOTHING, WAIT, OKAY"
    solutions["wait"] = "UHHH, NO, BLANK, OKAY, YES, LEFT, FIRST, PRESS, WHAT, WAIT"
    solutions["press"] = "RIGHT, MIDDLE, YES, READY, PRESS"
    solutions["you"] = "SURE, YOU ARE, YOUR, YOU'RE, NEXT, UH HUH, UR, HOLD, WHAT?, YOU"
    solutions["you are"] = "YOUR, NEXT, LIKE, UH HUH, WHAT?, DONE, UH UH, HOLD, YOU, U, YOU'RE, SURE, UR, YOU ARE"
    solutions["your"] = "UH UH, YOU ARE, UH HUH, YOUR"
    solutions["you're"] = "YOU, YOU'RE"
    solutions["ur"] = "DONE, U, UR"
    solutions["u"] = "UH HUH, SURE, NEXT, WHAT?, YOU'RE, UR, UH UH, DONE, U"
    solutions["uh huh"] = "UH HUH"
    solutions["uh uh"] = "UR, U, YOU ARE, YOU'RE, NEXT, UH UH"
    solutions["what?"] = "YOU, HOLD, YOU'RE, YOUR, U, DONE, UH UH, LIKE, YOU ARE, UH HUH, UR, NEXT, WHAT?"
    solutions["done"] = "SURE, UH HUH, NEXT, WHAT?, YOUR, UR, YOU'RE, HOLD, LIKE, YOU, U, YOU ARE, UH UH, DONE"
    solutions["next"] = "WHAT?, UH HUH, UH UH, YOUR, HOLD, SURE, NEXT"
    solutions["hold"] = "YOU ARE, U, DONE, UH UH, YOU, UR, SURE, WHAT?, YOU'RE, NEXT, HOLD"
    solutions["sure"] = "YOU ARE, DONE, LIKE, YOU'RE, YOU, HOLD, UH HUH, UR, SURE"
    solutions["like"] = "YOU'RE, NEXT, U, UR, HOLD, DONE, UH UH, WHAT?, UH HUH, YOU, LIKE"

    while True:
        display_word = input("Enter what the display says, or 'done' if this module is complete\n").lower()
        if display_word == "done":
            return
        if display_word in display:
            print(display[display_word])
        else:
            print("Not a valid entry, please try again.")
            continue

        solution = input("Word in that location?\n").lower()
        if solution in solutions:
            print(solutions[solution])
        else:
            print("Not a valid entry, please try again.")


def memory():
    stages = list()
    stages.append([0, 0])

    #STAGE 1
    display = int(input("Display says?\n"))
    if display == 1:
        print("Second position")
        pressed = int(input("What number was pressed?\n"))
        stages.append([2, pressed])
    if display == 2:
        print("Second position")
        pressed = int(input("What number was pressed?\n"))
        stages.append([2, pressed])
    if display == 3:
        print("Third position")
        pressed = int(input("What number was pressed?\n"))
        stages.append([3, pressed])
    if display == 4:
        print("Fourth position")
        pressed = int(input("What number was pressed?\n"))
        stages.append([4, pressed])

    #STAGE 2
    display = int(input("Display says?\n"))
    if display == 1:
        print("Press 4")
        position = int(input("What position was that?\n"))
        stages.append([position, 4])
    if display == 2:
        print("Position ", stages[1][0])
        pressed = int(input("What number was pressed?\n"))
        stages.append([stages[1][0], pressed])
    if display == 3:
        print("First position")
        pressed = int(input("What number was pressed?\n"))
        stages.append([1, pressed])
    if display == 4:
        print("Position ", stages[1][0])
        pressed = int(input("What number was pressed?\n"))
        stages.append([stages[1][0], pressed])

    #STAGE 3
    display = int(input("Display says?\n"))
    if display == 1:
        print("Press ", stages[2][1])
        position = int(input("What position was that?\n"))
        stages.append([position, stages[2][1]])
    if display == 2:
        print("Press ", stages[1][1])
        position = int(input("What position was that?\n"))
        stages.append([position, stages[1][1]])
    if display == 3:
        print("Third position")
        pressed = int(input("What number was pressed?\n"))
        stages.append([3, pressed])
    if display == 4:
        print("Press 4")
        position = int(input("What position was that?\n"))
        stages.append([position, 4])

    #STAGE 4
    display = int(input("Display says?\n"))
    if display == 1:
        print("Position ", stages[1][0])
        pressed = int(input("What number was pressed?\n"))
        stages.append([stages[1][0], pressed])
    if display == 2:
        print("First position")
        pressed = int(input("What number was pressed?\n"))
        stages.append([1, pressed])
    if display == 3:
        print("Position ", stages[2][0])
        pressed = int(input("What number was pressed?\n"))
        stages.append([stages[2][0], pressed])
    if display == 4:
        print("Position ", stages[2][0])
        pressed = int(input("What number was pressed?\n"))
        stages.append([stages[2][0], pressed])

    # STAGE 5
    display = int(input("Display says?\n"))
    if display == 1:
        print("Press ", stages[1][1])
    if display == 2:
        print("Press ", stages[2][1])
    if display == 3:
        print("Press ", stages[4][1])
    if display == 4:
        print("Press ", stages[3][1])

    return


def morse_code():
    print("Enter the letters one at a time using . and -, or 'done' when all are entered.")
    morse = dict()
    solutions = dict()

    morse[".-"] = "a"
    morse["-..."] = "b"
    morse["-.-."] = "c"
    morse["."] = "e"
    morse["..-."] = "f"
    morse["--."] = "g"
    morse["...."] = "h"
    morse[".."] = "i"
    morse["-.-"] = "k"
    morse[".-.."] = "l"
    morse["--"] = "m"
    morse["-."] = "n"
    morse["---"] = "o"
    morse[".-."] = "r"
    morse["..."] = "s"
    morse["-"] = "t"
    morse["...-"] = "v"
    morse["-..-"] = "x"

    solutions["shell"] = "3.505"
    solutions["halls"] = "3.515"
    solutions["slick"] = "3.522"
    solutions["trick"] = "3.532"
    solutions["boxes"] = "3.535"
    solutions["leaks"] = "3.542"
    solutions["strobe"] = "3.545"
    solutions["bistro"] = "3.552"
    solutions["flick"] = "3.555"
    solutions["bombs"] = "3.565"
    solutions["break"] = "3.572"
    solutions["brick"] = "3.575"
    solutions["steak"] = "3.582"
    solutions["sting"] = "3.592"
    solutions["vector"] = "3.595"
    solutions["beats"] = "3.600"
    letters = ""

    while True:
        code = input("Next Letter?\n")
        if code == "done":
            break
        if code in morse:
            letters += morse[code]
        else:
            print("Letter not found, try again.")

    if letters in solutions:
        print("Tune to ", solutions[letters])
    else:
        print("No word found. Please start over.")
        morse_code()


def complicated_wires(pport, even, batteries):
    wires = list()
    wire_actions = list()
    print("Please enter the wirestring in the following format:")
    print(".       \tIf the LED is on")
    print("w, b, r \tThe colors of the wires")
    print("*       \tIf there is a star")
    print(":       \tBetween each entry.")
    print("Examples: .w:rb*:.wb*:.rw:br*")

    wirestring = input("\n Wirestring?\n")
    wires = wirestring.split(":")
    for wire in wires:
        if "w" in wire and "b" not in wire and "r" not in wire:
            if "." == wire:
                if "*" == wire:
                    if batteries >= 2:
                        wire_actions.append(1)
                    else:
                        wire_actions.append(0)
                else:
                    wire_actions.append(0)
            else:
                wire_actions.append(1)
        elif "b" in wire:
            if "r" in wire:
                if "." in wire:
                    if "*" in wire:
                        wire_actions.append(0)
                    else:
                        if even:
                            wire_actions.append(1)
                        else:
                            wire_actions.append(0)
                elif "*" in wire:
                    if pport:
                        wire_actions.append(1)
                    else:
                        wire_actions.append(0)
                else:
                    if even:
                        wire_actions.append(1)
                    else:
                        wire_actions.append(0)
            else:
                if "." in wire:
                    if pport:
                        wire_actions.append(1)
                    else:
                        wire_actions.append(0)

                elif "*" in wire:
                    wire_actions.append(0)
                else:
                    if even:
                        wire_actions.append(1)
                    else:
                        wire_actions.append(0)
        elif "r" in wire:
            if "." in wire:
                if batteries >= 2:
                    wire_actions.append(1)
                else:
                    wire_actions.append(0)
            elif "*" in wire:
                wire_actions.append(1)
            else:
                if even:
                    wire_actions.append(1)
                else:
                    wire_actions.append(0)

    wire_number = 1
    cut_wires = list()
    uncut_wires = list()
    for i in range(0, len(wire_actions)):
        if wire_actions[i] == 1:
            cut_wires.append(wire_number)
        else:
            uncut_wires.append(wire_number)
        wire_number += 1

    print("Cut wires: ", cut_wires)
    print("Do not cut wires: ", uncut_wires)

    return



def wire_sequence():
    red = [" ", "c", "b", "a", "ac", "b", "ac", "abc", "ab", "b"]
    blue = [" ", "b", "ac", "b", "a", "b", "bc", "c", "ac", "a"]
    black = [" ", "abc", "ac", "b", "ac", "b", "bc", "ab", "c", "c"]

    red_count = 0
    blue_count = 0
    black_count = 0

    while True:
        wire_color = input("Enter the next wire color; b for black, u for blue; or 'done'\n")

        if wire_color == "done":
            return

        if wire_color == "red" or wire_color == "r":
            red_count += 1
            connection = input("What letter is it connected to?\n")
            if connection in red[red_count]:
                print("cut")
            else:
                print("leave")

        if wire_color == "blue" or wire_color == "u":
            blue_count += 1
            connection = input("What letter is it connected to?\n")
            if connection in blue[blue_count]:
                print("cut")
            else:
                print("leave")

        if wire_color == "black" or wire_color == "b":
            black_count += 1
            connection = input("What letter is it connected to?\n")
            if connection in black[black_count]:
                print("cut")
            else:
                print("leave")

    return


def password():
    first_letters = input("Please input letter options of first space\n")
    second_letters = input("Please input letter options of second space\n")

    possible
