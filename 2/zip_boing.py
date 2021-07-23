"""
COMP.CS.100 Zip Boing.
Tekijä: Otto 
Opiskelijanumero: 
"""


def main():
    number = int(input("How many numbers would you like to have? "))
    for i in range(1, number+1):
        cond1 = i % 3 == 0
        cond2 = i % 7 == 0
        if cond1 and cond2:
            print("zip boing")
        elif cond1:
            print("zip")
        elif cond2:
            print("boing")
        else:
            print(i)


if __name__ == "__main__":
    main()
