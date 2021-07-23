"""
COMP.CS.100 Pelihahmo A.
Tekijä: Otto 
Opiskelijanumero: 
"""


class Character:
    """
    fake docstring
    """

    def __init__(self, name):
        self.__name = name
        self.__items = {}

    def give_item(self, item):
        if item in self.__items:
            self.__items[item] += 1
        else:
            self.__items[item] = 1

    def remove_item(self, item):
        if item in self.__items:
            self.__items[item] -= 1

    def printout(self):
        print(f"Name: {self.__name}")
        if sum(self.__items.values()) > 0:
            print("\n".join([f"  {value} {key}" for key, value in
                            sorted(self.__items.items()) if value != 0]))
        else:
            print("  --nothing--")

    def get_name(self):
        return self.__name

    def has_item(self, item):
        return item in self.__items and self.__items[item] > 0

    def how_many(self, item):
        return self.__items[item] if item in self.__items else 0


def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
