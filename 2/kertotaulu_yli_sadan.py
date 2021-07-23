"""
COMP.CS.100 Kertotaulu, kouluversio.
Tekijä: Otto 
Opiskelijanumero: 
"""


def main():
    number = int(input("Choose a number: "))
    index = summation = 0
    while summation < 100:
        index += 1
        summation = index * number
        print(index, "*", number, "=", summation)


if __name__ == "__main__":
    main()
