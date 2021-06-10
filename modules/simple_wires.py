def solve_simple_wires(even=False):
    solved = False
    while not solved:
        print("Please enter the wires from top to bottom using the first letter. \n")
        print("Use b for black, r for red, u for blue, w for white, and y for yellow.\n")
        wire_string = input("Wirestring? \n")
        wire_string = str(wire_string).lower().strip()
        invalid = "acdefghijklmnopqstvxz0123456789"
        if any((i in invalid) for i in wire_string):
            print("You included invalid characters. Try again. \n")
            continue
        #If there are no red wires, cut the second wire.
        #Otherwise, if the last wire is white, cut the last wire.
        #Otherwise, if there is more than one blue wire, cut the last blue wire.
        #Otherwise, cut the last wire.
        if len(wire_string) == 3:
            if wire_string.find('r') == -1:
                print("Cut the second wire")
            elif wire_string[2] == 'w':
                print("Cut the last wire")
            elif wire_string.count('u') > 1:
                print("Cut the last blue wire")
            else:
                print("Cut the last wire")
            solved = True

        #If there is more than one red wire and the last digit of the serial number is odd, cut the last red wire.
        #Otherwise, if the last wire is yellow and there are no red wires, cut the first wire.
        #Otherwise, if there is exactly one blue wire, cut the first wire.
        #Otherwise, if there is more than one yellow wire, cut the last wire.
        #Otherwise, cut the second wire.
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
            solved = True

        elif len(wire_string) == 5:
            if wire_string[4] == 'b' and not even:
                print("Cut the fourth wire")
            elif wire_string.count('r') == 1 and wire_string.count('y') > 1:
                print("Cut the first wire")
            elif 'b' not in wire_string:
                print("Cut the second wire")
            else:
                print("Cut the first wire")
            solved = True

        elif len(wire_string) == 6:
            if 'y' not in wire_string and not even:
                print("Cut the third wire")
            elif wire_string.count('y') == 1 and wire_string.count('w') > 1:
                print("Cut the fourth wire")
            elif 'r' not in wire_string:
                print("Cut the last wire")
            else:
                print("Cut the fourth wire")
            solved = True

        else:
            print("That is not an acceptable length, please re-enter wirestring \n")
            continue

    return
