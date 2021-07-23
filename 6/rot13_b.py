"""
COMP.CS.100 rot13_b.
Tekijä: Otto 
Opiskelijanumero: 
"""


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("The same, shouting:")
    print("\n".join([x.upper() for x in msg]))


def read_message():
    """
    ottaa vastaan syötettä kunnes tyhjä rivi

    :return: array,
        syöte
    """
    ret = []
    inp = input()

    while inp != "":
        ret.append(inp)
        inp = input()

    return ret


if __name__ == "__main__":
    main()
