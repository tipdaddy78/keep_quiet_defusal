def solve_button(batteries, car, frk):
    button_color = ""
    while 1:
        button_color = input("What color is the button?\n").lower()
        if button_color != "blue" and button_color != "white" and button_color != "yellow" and button_color != "red":
            print("That is not a valid button color.  Valid colors are blue, red, white, and yellow.")
        else:
            break
    button_text = input("What does the button say?\n").lower()
    hold = False

    if button_color == "blue" and button_text == "abort":
        hold = True
    elif batteries > 1 and button_text == "detonate":
        hold = False
    elif button_color == "white" and car:
        hold = True
    elif batteries > 2 and frk:
        hold = False
    elif button_color == "yellow":
        hold = True
    elif button_color == "red" and button_text == "hold":
        hold = False
    else:
        hold = True

    if hold:
        print("HOLD the button")
        print("If the strip is blue, release it when the timer has a 4 in any position.")
        print("If the strip is yellow, release it when the timer has a 5 in any position.")
        print("Otherwise, release it when the timer has a 1 in any position.")
    else:
        print("Press and release")
    return