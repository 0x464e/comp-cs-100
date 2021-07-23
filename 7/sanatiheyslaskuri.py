"""
COMP.CS.100 sanatiheyslaskuri.
Tekijä: Otto 
Opiskelijanumero: 
"""


def main():
    print("Enter rows of text for word counting. Empty row to quit.")
    words = [x for x in read_message().lower().split() if x]
    print("\n".join(sorted([" : ".join([str(y) for y in x]) + " times" for x in dict(zip(words, [words.count(x) for x in words])).items()])))

    # print("\n".join(sorted([f"{x} : {words.count(x)} times" for x in sorted(set(words))])))


def read_message():
    """
    vastaanottaa syötettä kunnes tyhjä rivi
    :return: string,
        syöte
    """
    ret = ""
    inp = input()

    # ei kine jos käyttäjä pistää rivin vaihtoi
    # kaikki teksti vaa pötköön ja välilöynti väliin
    while inp != "":
        ret += " " + inp
        inp = input()

    # poistetaa se extra välilöynti tost alust
    return ret[1:]


if __name__ == "__main__":
    main()
