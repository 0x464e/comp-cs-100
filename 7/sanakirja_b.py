"""
COMP.CS.100 sanakirja_b.
Tekijä: Otto 
Opiskelijanumero: 
"""


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    print("Dictionary contents:")
    print(", ".join(sorted([x for x in english_spanish.keys()])))

    while True:

        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":
            word = input("Enter the word to be translated: ").strip()
            if word in english_spanish:
                print(word, "in Spanish is", english_spanish[word])
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            word_eng = input("Give the word to be added in English: ").strip()
            word_spa = input("Give the word to be added in Spanish: ").strip()
            english_spanish[word_eng] = word_spa
            print("Dictionary contents:")
            print(", ".join(sorted([x for x in english_spanish.keys()])))

        elif command == "R":
            word = input("Give the word to be removed: ").strip()
            if word in english_spanish:
                del english_spanish[word]
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "P":
            print("\nEnglish-Spanish")
            print("\n".join(sorted([x + " " + english_spanish[x] for x in
                                    english_spanish.keys()])))
            print("\nSpanish-English")
            print("\n".join(sorted([english_spanish[x] + " " + x for x in
                                    english_spanish.keys()])))
            print()

        elif command == "T":
            sentence = input("Enter the text to be translated into Spanish: ")\
                .strip().split(" ")
            outp = []
            for word in sentence:
                if word in english_spanish:
                    outp.append(english_spanish[word])
                else:
                    outp.append(word)
            print("The text, translated by the dictionary:")
            print(" ".join(outp))

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


if __name__ == "__main__":
    main()
