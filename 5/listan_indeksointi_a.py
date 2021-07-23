"""
COMP.CS.100 listan indeksointi A.
Tekijä: Otto 
Opiskelijanumero: 
"""


def main():
    arr = []
    print("Give 5 numbers:")
    for _ in range(5):
        arr.append(int(input("Next number: ")))
    print("The numbers you entered that were greater than zero were:")
    for num in arr:
        if num > 0:
            print(num)


if __name__ == "__main__":
    main()
