def simon_says(bomb):
    print("SIMON MODULE - START")
    while True:
        sequence = input("\nPlease enter the sequence by first letter of the color, or 'done' if you are done.\n")
        if sequence == "done":
            print("SIMON MODULE - END")
            return
        if sequence == "strike":
            bomb.add_strike()
            if bomb.strikes == 3:
                print("SIMON MODULE - END DUE TO STRIKES")
                return
            else:
                continue
        invalid = "acdefhijklmnopqstuvwxz0123456789"
        if any((i in invalid) for i in sequence):
            print("You included invalid characters.")
            continue
        for i in sequence:
            if bomb.serial_has_vowel:
                if bomb.strikes == 0:
                    if i == 'r':
                        print("Blue")
                    elif i == 'b':
                        print("Red")
                    elif i == 'g':
                        print("Yellow")
                    else:
                        print("Green")
                elif bomb.strikes == 1:
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
                if bomb.strikes == 0:
                    if i == 'r':
                        print("Blue")
                    elif i == 'b':
                        print("Yellow")
                    elif i == 'g':
                        print("Green")
                    else:
                        print("Red")
                elif bomb.strikes == 1:
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