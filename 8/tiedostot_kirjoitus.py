"""
COMP.CS.100 tiedostot_kirjoitus.
Tekijä: Otto 
Opiskelijanumero: 
"""


def main():
    try:
        name = input("Enter the name of the file: ")
        file = open(name, "w")
        inp = input("Enter rows of text. Quit by entering an empty row.\n")
        i = 1
        txt = ""
        while inp != "":
            txt += f"{i} {inp}\n"
            i += 1
            inp = input()
        print(txt.rstrip(), file=file)
        print(f"File {name} has been written.")
    except:
        print(f"Writing the file {name} was not successful.")


if __name__ == "__main__":
    main()
