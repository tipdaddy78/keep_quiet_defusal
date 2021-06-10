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

def solve_morse_code():
    print("MORSE CODE MODULE - START")
    print("Enter the letters one at a time using . and -, or 'done' when all are entered.")
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
        print("\nTune to ", solutions[letters])
        print("MORSE CODE MODULE - END")
    else:

        print("No word found. Please start over, ensure you're starting from the beginning for best results.")
        solve_morse_code()