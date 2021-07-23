"""
COMP.CS.100 Old MacDonald Had a Farm -laulu.
Tekijä: Otto 
Opiskelijanumero: 
"""


def print_verse(animal, sound):
    print("Old MACDONALD had a farm\n"
          "E-I-E-I-O\n"
          f"And on his farm he had a {animal}\n"
          "E-I-E-I-O\n"
          f"With a {sound} {sound} here\n"
          f"And a {sound} {sound} there\n"
          f"Here a {sound}, there a {sound}\n"
          f"Everywhere a {sound} {sound}\n"
          "Old MacDonald had a farm\n"
          "E-I-E-I-O\n")


def main():
    print_verse("cow", "moo")
    print_verse("pig", "oink")
    print_verse("duck", "quack")
    print_verse("horse", "neigh")
    print_verse("lamb", "baa")


if __name__ == "__main__":
    main()
