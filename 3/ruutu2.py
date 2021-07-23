"""
COMP.CS.100 Ruutu 2.
Tekijä: Otto 
Opiskelijanumero: 
"""


def read_input(msg):
    inp = int(input(msg))
    while inp < 1:
        inp = int(input(msg))
    return inp


def print_box(w, h, c):
    for _ in range(h):
        print(c*w)


def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print_box(width, height, mark)


if __name__ == "__main__":
    main()

