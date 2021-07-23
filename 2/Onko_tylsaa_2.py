"""
COMP.CS.100 Onko tylsää 2.
Tekijä: Otto 
Opiskelijanumero: 
"""

validInputs = ["Y", "y", "N", "n"]


def main():
    inp = input("Answer Y or N: ")

    while inp not in validInputs:
        inp = input("Incorrect entry.\nPlease retry: ")

    print("You answered", inp)


if __name__ == "__main__":
    main()
