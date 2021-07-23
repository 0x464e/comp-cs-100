"""
COMP.CS.100 Lukusarjoja.
Tekijä: Otto 
Opiskelijanumero: 
"""


def main():
    for number in range(101):
        if number % 2 == 0:
            print(number)
    for number in reversed(range(101)):
        if number % 2 == 0:
            print(number)


if __name__ == "__main__":
    main()
