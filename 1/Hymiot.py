"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Otto 
Opiskelijanumero: 
"""


def main():
    i = int(input("How do you feel? (1-10) "))
    if i < 1 or i > 10:
        print("Bad input!")
    elif i == 1:
        print("A suitable smiley would be :'(")
    elif i == 10:
        print("A suitable smiley would be :-D")
    elif i < 4:
        print("A suitable smiley would be :-(")
    elif i < 8:
        print("A suitable smiley would be :-|")
    else:
        print("A suitable smiley would be :-)")


if __name__ == "__main__":
    main()
