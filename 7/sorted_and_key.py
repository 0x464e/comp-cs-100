"""
COMP.CS.100 sorted_ja_key.
Tekijä: Otto 
Opiskelijanumero: 
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    print("\n".join([f"{x} {y:.2f}" for x, y in sorted(PRICES.items(), key=lambda x: x[1])]))


if __name__ == "__main__":
    main()

