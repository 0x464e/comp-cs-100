"""
COMP.CS.100 molkky.
Tekijä: Otto 
Opiskelijanumero: 
"""


class Player:
    """
    fake docstring
    """
    def __init__(self, name):
        """
        fake docstring
        :param name:
        """
        self.__name = name
        self.__points = 0
        self.__total_points = 0
        self.__throw = 0
        self.__hits = 0

    def get_name(self):
        return self.__name

    def add_points(self, pts):
        self.__total_points += pts
        if self.__points + pts > 50:
            self.__points = 25
            print(self.__name, "gets penalty points!")
        else:
            self.__points += pts
        if 40 <= self.__points <= 49:
            print(f"{self.__name} needs only {50-self.__points} points. It's "
                  f"better to avoid knocking down the pins with higher points.")
        if self.__throw > 0 and pts > self.__total_points/self.__throw:
            print(f"Cheers {self.__name}!")

    def has_won(self):
        return self.__points == 50

    def get_points(self):
        return self.__points

    def add_throw(self, hit):
        self.__throw += 1
        if hit:
            self.__hits += 1

    def hit_percentage(self):
        if self.__throw == 0:
            return 0.0
        return f"{self.__hits/self.__throw*100:.1f}"


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_throw(pts > 0)
        in_turn.add_points(pts)


        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p,", "hit percentage", player1.hit_percentage())
        print(player2.get_name() + ":", player2.get_points(), "p,", "hit percentage", player2.hit_percentage())
        print("")

        throw += 1


if __name__ == "__main__":
    main()
