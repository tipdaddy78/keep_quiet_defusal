def solve_complicated_wires(bomb):
    print("COMPLICATED WIRES MODULE - START")
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
            if "." in wire:
                if "*" in wire:
                    if bomb.batteries >= 2:
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
                        if bomb.last_digit_even:
                            wire_actions.append(1)
                        else:
                            wire_actions.append(0)
                elif "*" in wire:
                    if bomb.parallel:
                        wire_actions.append(1)
                    else:
                        wire_actions.append(0)
                else:
                    if bomb.last_digit_even:
                        wire_actions.append(1)
                    else:
                        wire_actions.append(0)
            else:
                if "." in wire:
                    if bomb.parallel:
                        wire_actions.append(1)
                    else:
                        wire_actions.append(0)

                elif "*" in wire:
                    wire_actions.append(0)
                else:
                    if bomb.last_digit_even:
                        wire_actions.append(1)
                    else:
                        wire_actions.append(0)
        elif "r" in wire:
            if "." in wire:
                if bomb.batteries >= 2:
                    wire_actions.append(1)
                else:
                    wire_actions.append(0)
            elif "*" in wire:
                wire_actions.append(1)
            else:
                if bomb.last_digit_even:
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

    print("\nCut wires: ", cut_wires)
    print("Do not cut wires: ", uncut_wires)

    print("COMPLICATED WIRES MODULE - START")
    return