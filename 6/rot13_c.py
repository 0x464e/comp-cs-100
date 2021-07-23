"""
COMP.CS.100 rot13_c.
Tekijä: Otto 
Opiskelijanumero: 
"""


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("ROT13:")
    print("\n".join([row_encryption(x) for x in msg]))


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


def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                     "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                     "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    if text.lower() not in regular_chars:
        return text

    upper = text.isupper()
    c = encrypted_chars[regular_chars.index(text.lower())]
    if upper:
        c = c.upper()

    return c


def row_encryption(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    ret = ""
    for c in text:
        ret += encrypt(c)

    return ret


if __name__ == "__main__":
    main()
