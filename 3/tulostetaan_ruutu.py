"""
COMP.CS.100 tulostetaan ruutu.
Tekijä: Otto 
Opiskelijanumero: 
"""


def print_box(w, h, c):
    for _ in range(h):
        print(c*w)


def main():
    width = int(input("Enter the width of a frame: "))
    height = int(input("Enter the height of a frame: "))
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
