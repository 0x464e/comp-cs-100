"""
COMP.CS.100 poikkeukset.
Tekijä: Otto 
Opiskelijanumero: 
"""


def read_input(msg):
    """
    tries to parse a positive integer
    :param msg:
    :return: int
    """
    err = True
    while err:
        try:
            inp = int(input(msg))
            while inp < 1:
                inp = int(input(msg))
            err = False
        except ValueError:
            continue
    return inp


def print_box(w, h, c):
    """
    prints a box based off the desired values
    :param w: width
    :param h: heigth
    :param c: character
    :return:
    """
    for _ in range(h):
        print(c*w)


def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print_box(width, height, mark)


if __name__ == "__main__":
    main()