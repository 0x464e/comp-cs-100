"""
COMP.CS.100 listan indeksointi B.
Tekijä: Otto 
Opiskelijanumero: 
"""


def main():
    arr = []
    print("Give 5 numbers:")
    for _ in range(5):
        arr.append(int(input("Next number: ")))
    print("The numbers you entered, in reverse order:")
    for num in reversed(arr):
        print(num)


if __name__ == "__main__":
    main()
