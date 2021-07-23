"""
COMP.CS.100 Old MacDonald Had a Farm -laulu.
Tekijä: Otto 
Opiskelijanumero: 
"""

# en usko et tätä joku manuaalisesti kattoo, mut
# jos kattoo, nii meni moti variablejen nimeämisen
# kaa, ne nyt on mitä sattuu :'_D


def repeat_name(name, count):
    for _ in range(1, count+1):
        print(f"{name}, {name} Bear")


def verse(words, name):
    print(words)
    print(f"{name}, {name}")
    print(words)
    repeat_name(name, 3)
    print(words)
    repeat_name(name, 1)
    print()


def main():
    verse("I know someone you don't know", "Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()
