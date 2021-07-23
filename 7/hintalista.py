"""
COMP.CS.100 hintalista.
Tekijä: Otto 
Opiskelijanumero: 
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15
}


def main():
    inp = input("Enter product name: ").strip()

    while inp != "":
        if inp in PRICES:
            print(f"The price of {inp} is {PRICES[inp]:.2f} e")
        else:
            print(f"Error: {inp} is unknown.")
        inp = input("Enter product name: ").strip()

    print("Bye!")


if __name__ == "__main__":
    main()
