"""
COMP.CS.100 Kertotaulu, kouluversio.
Tekijä: Otto 
Opiskelijanumero: 
"""


def main():
    number = int(input("Choose a number: "))
    for i in range(1, 11):
        print(i, "*", number, "=", i*number)


if __name__ == "__main__":
    main()