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

def solve_whos_on_first():
    print("WHO'S ON FIRST MODULE - START")
    while True:
        display_word = input("\nEnter what the display says, or 'done' if this module is complete\n").lower()
        if display_word == "done":
            print("WHO'S ON FIRST MODULE - END ")
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