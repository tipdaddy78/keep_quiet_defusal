def solve_memory(bomb):
    stages = list()
    stages.append([0, 0])
    print("MEMORY MODULE - START")
    print("When the console shows 'Display Says?', enter in the value in the top.")
    print("The program will then tell you a position to press, or a specific number.")
    print("Positions are from left to right so 'Third Position' is the third from the left button.")
    print("Lastly, it will ask what number or position was pressed.")
    print("If at any time a mistake is made causing a strike, enter 'strike' to reset the module.")

    #STAGE 1
    stage = 1
    while stage <= 5:
        print("\nSTAGE " + str(stage))
        disp = input("Display says?\n")
        if disp.lower().strip() == 'strike':
            bomb.add_strike()
            if bomb.strikes == 3:
                return
            stage = 1
            stages.clear()
            stages.append([0, 0])
            continue
        display = int(disp)
        if stage == 1:
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
        elif stage == 2:
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
        elif stage == 3:
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
        elif stage == 4:
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
        elif stage == 5:
            if display == 1:
                print("Press ", stages[1][1])
            if display == 2:
                print("Press ", stages[2][1])
            if display == 3:
                print("Press ", stages[4][1])
            if display == 4:
                print("Press ", stages[3][1])
        stage += 1
    print("MEMORY MODULE - END")
    return