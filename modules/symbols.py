column1 = ["tennis", "at", "lambda", "lightning", "cat", "h", "back-c"]
column2 = ["back-e", "tennis", "back-c", "squiggle", "white-star", "h", "question"]
column3 = ["copyright", "comma-3", "squiggle", "ix", "r", "lambda", "white-star"]
column4 = ["6", "paragraph", "b", "cat", "ix", "question", "smiley"]
column5 = ["psi", "smiley", "b", "c", "paragraph", "snake", "black-star"]
column6 = ["6", "back-e", "not-equal", "ae", "psi", "back-n", "omega"]
columns = [column1, column2, column3, column4, column5, column6]

def solve_symbols():
    print("SYMBOLS MODULE - START")
    print_symbols()
    symbols_solved = False

    while not symbols_solved:
        print("Please enter the symbols")
        sym1 = ""
        sym2 = ""
        sym3 = ""
        sym4 = ""
        while 1:
            sym1 = input("Symbol 1?\n").lower().strip()
            if sym1 == 'symbols':
                print_symbols()
            else:
                break
        while 1:
            sym2 = input("Symbol 2?\n").lower().strip()
            if sym2 == 'symbols':
                print_symbols()
            else:
                break

        while 1:
            sym3 = input("Symbol 3?\n").lower().strip()
            if sym3 == 'symbols':
                print_symbols()
            else:
                break

        while 1:
            sym4 = input("Symbol 4?\n").lower().strip()
            if sym4 == 'symbols':
                print_symbols()
            else:
                break

        symbols = [sym1, sym2, sym3, sym4]

        correct_column = -1

        for i in range(0, 6):
            if sym1 in columns[i] and sym2 in columns[i] and sym3 in columns[i] and sym4 in columns[i]:
                correct_column = i
                break

        if correct_column == -1:
            print("Looks like you entered a symbol I can't identify. Time to try again.")
            print("Type 'symbols' to list out the accepted symbol names and a description.")
            continue

        #loop through correct column, symbols will be printed from top to bottom.
        print("MATCH FOUND")
        print("The symbols should be pressed in the following order:")
        for i in range(0, 7):
            if columns[correct_column][i] in symbols:
                print(columns[correct_column][i])
                symbols_solved = True
    print("SYMBOLS MODULE - END")

def print_symbols():
    print("Possible symbol names include:")
    print("'tennis' - A circle with a small line, representing a tennis racket.")
    print("'at' - A symbol representing an A and T combined.")
    print("'lambda' - The Greek lambda letter with a slash through it.")
    print("'lightning' - An angular squiggle, also looks like an angled backwards n.")
    print(
        "'cat' - A symbol that looks like a cat.  Vertical line on the left, triangle and upside-down w on the right.")
    print(
        "'h' - A symbol that looks like a capital H drawn without lifting the hand.  Has a tail on the bottom right ")
    print("'back-c' - A backwards capital C with a . in the middle.")
    print("'back-e' - A backwards capital E with an umlaut (..) on-top of it.")
    print("'squiggle' - A curvy symbol with a loop and tails on either end.")
    print("'white-star' - A star that is filled in white.")
    print("'question' - An upside-down question mark.")
    print("'copyright' - The copyright symbol: A C inside a circle.")
    print("'comma-3' - A 3 on its side with a comma and what appears to be an eyebrow above it.")
    print("'ix' - A symbol composed of a curvy capital X with a capital I in the middle.")
    print("'r' - A symbol that looks like a capital R with the lower-left part missing.")
    print("'6' - A Symbol that looks like the number 6.")
    print("'paragraph' - The paragraph symbol: backwards capital P with a filled in hole.")
    print("'b' - A symbol that looks like lowercase b with a capital T.")
    print("'smiley' - A symbol that looks like a smiley face with its tongue out.")
    print("'c' - A capital C with a . in the middle.")
    print("'snake' - A symbol that looks like a 3 with a v on top of it and a tail coming off the bottom.")
    print("'black-star' - A star that is filled in black.")
    print("'not-equal' - A symbol that looks like an equal sigh with a slash through it.  Also looks like two x's")
    print("'ae' - A symbol of the letters a and e combined.")
    print("'psi' - A symbol that looks like Poseidon's trident.  Also a capital I with a U through it.")
    print("'back-n' - A symbol that looks like a backwards capital N with a small curve above it.")
    print("'omega' - The Greek omega letter.")