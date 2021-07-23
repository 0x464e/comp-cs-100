"""
COMP.CS.100 Kivi-paperi-sakset.
Tekijä: Otto 
Opiskelijanumero: 
"""


def main():
    p1 = input("Player 1, enter your choice (R/P/S): ")
    p2 = input("Player 2, enter your choice (R/P/S): ")
    if p1 == p2:
        print("It's a tie!")
    elif p1 == "R":
        if p2 == "P":
            print("Player 2 won!")
        else:
            print("Player 1 won!")
    elif p1 == "P":
        if p2 == "S":
            print("Player 2 won!")
        else:
            print("Player 1 won!")
    else:
        if p2 == "R":
            print("Player 2 won!")
        else:
            print("Player 1 won!")


if __name__ == "__main__":
    main()
