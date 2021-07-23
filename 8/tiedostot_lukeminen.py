"""
COMP.CS.100 tiedostot_lukeminen.
Tekijä: Otto 
Opiskelijanumero: 
"""


def main():
    try:
        file = open(input("Enter the name of the file: "), "r")
    except OSError:
        print("There was an error in reading the file.")
        return
    print("".join([f"{x+1} {y}" for x, y in enumerate(file)]))


if __name__ == "__main__":
    main()
