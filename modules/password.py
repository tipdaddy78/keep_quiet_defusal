passwords = ['about', 'after', 'again', 'below', 'could',
           'every', 'first', 'found', 'great', 'house',
           'large', 'learn', 'never', 'other', 'place',
           'plant', 'point', 'right', 'small', 'sound',
           'spell', 'still', 'study', 'their', 'there',
           'these', 'thing', 'think', 'three', 'water',
           'where', 'which', 'world', 'would', 'write']

def solve_password():
    print("PASSWORD MODULE - START")
    options = set()
    first_letters = input("Please input letter options of first space\n")
    second_letters = input("Please input letter options of second space\n")
    for f in first_letters:
        if f == '' or f == ' ':
            continue
        for s in second_letters:
            if s == '' or s == ' ':
                continue
            for p in passwords:
                if p.startswith(f + s):
                    options.add(p)
    if len(options) == 1:
        print("Password is: " + str(options))
        print("PASSWORD MODULE - END")
        return
    else:
        third_letters = input("Please input letter options of third space\n")
        new_ops = options.copy()
        for op in options:
            found = False
            for t in third_letters:
                if found:
                    break
                for p in passwords:
                    if found:
                        break
                    if p.startswith(op[0:2] + t):
                        found = True
            if not found:
                new_ops.remove(op)

        options = new_ops
        if len(options) == 1:
            print("Password is: " + str(options))
            print("PASSWORD MODULE - END")
            return
        else:
            fourth_letters = input("Please input letter options of fourth space\n")
            new_ops2 = options.copy()
            for op in options:
                found = False
                for fo in fourth_letters:
                    if found:
                        break
                    for p in passwords:
                        if found:
                            break
                        if p.startswith(op[0:3] + fo):
                            found = True
                if not found:
                    new_ops2.remove(op)
            options = new_ops2
            if len(options) == 1:
                print("Password is: " + str(options))
                print("PASSWORD MODULE - END")
                return
            else:
                fifth_letters = input("Please input letter options of fifth space\n")
                new_ops3 = options.copy()
                for op in options:
                    found = False
                    for fi in fifth_letters:
                        if found:
                            break
                        for p in passwords:
                            if found:
                                break
                            if p.startswith(op[0:4] + fi):
                                found = True
                    if not found:
                        new_ops3.remove(op)
                options = new_ops3
                if len(options) == 1:
                    print("Password is: " + str(options))
                    print("PASSWORD MODULE - END")
                    return
                else:
                    print("Unable to locate password... Restarting.")
                    print("PASSWORD MODULE - END")
                    solve_password()