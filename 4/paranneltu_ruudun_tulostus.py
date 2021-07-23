"""
COMP.CS.100 paranneltu_ruudun_tulostus.
Tekijä: Otto 
Opiskelijanumero: 
"""


def print_box(width, height, border_mark="#", inner_mark=" "):
    """
    prints a box with the desired settings
    :param height:
    :param width:
    :param inner_mark:
    :param border_mark:
    """
    print(border_mark * width)
    for _ in range(height-2):
        print(f"{border_mark}{inner_mark*(width-2)}{border_mark}")
    print(border_mark * width)
    print()


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


if __name__ == "__main__":
    main()
