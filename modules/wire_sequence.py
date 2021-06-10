red = [" ", "c", "b", "a", "ac", "b", "ac", "abc", "ab", "b"]
blue = [" ", "b", "ac", "b", "a", "b", "bc", "c", "ac", "a"]
black = [" ", "abc", "ac", "b", "ac", "b", "bc", "ab", "c", "c"]

def solve_wire_sequence():
    print("WIRE SEQUENCE MODULE - START")
    red_count = 0
    blue_count = 0
    black_count = 0

    while True:
        wire_color = input("\nEnter the next wire color; b for black, u for blue; or 'done'\n")

        if wire_color == "done":
            break

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
    print("WIRE SEQUENCE MODULE - END")
    return