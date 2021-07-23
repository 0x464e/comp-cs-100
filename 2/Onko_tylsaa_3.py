"""
COMP.CS.100 Onko tylsää 3.
Tekijä: Otto 
Opiskelijanumero: 
"""

validInputs = ["Y", "y", "N", "n"]


def main():
    inp = input("Bored? (y/n) ")

    while inp not in validInputs[0:2]:
        if inp not in validInputs[2:]:
            inp = input("Incorrect entry.\nPlease retry: ")
        else:
            inp = input("Bored? (y/n) ")

    print("Well, let's stop this, then.")


if __name__ == "__main__":
    main()
