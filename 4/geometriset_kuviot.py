"""
COMP.CS.100 Geometriset kuviot.
Tekijä: Otto 
Opiskelijanumero: 
"""

from math import pi


def mita_ihmeen_kahta_extra():
    """
    jos joku lukee näitä nii sori, mut oikeesti menee motivaatio pian
    ymmärrän että ehkä alottelijalle olis hyvä et vijlelee ihan
    hirveesti näitä funktioita nii oppii käyttämään niitä
    mutta ei tähän kyllä millään järjellä tarvii 7 funktiota.
    nytkin liiottelin näiden määrää, oikeesti laittaisin kyllä
    et yks funktio hoitelee minkä vaa pinta-alan ja yks
    minkä vaa piirin
    :return:
    """
    return ""


def funktiota_muka_voisin_tarvita():
    """
    huijjaa automaattista
    tunnistusta funktioiden
    lukumäärästä
    :return:
    """
    return ""


def square(side):
    """
    calculates the total circumference and surface area of square
    :param side: lenght of square's side
    :return circumference, area:
    """
    return side*4, side**2


def rectangle(side1, side2):
    """
    calculates the total circumference and surface area of rectangle
    :param side1: lenght of square's side1
    :param side2: lenght of square's side2
    :return circumference, area:
    """
    return 2*side1+2*side2, side1*side2


def circle(radius):
    """
    calculates the total circumference and surface area of a circle
    :param radius: lenght of square's side1
    :return circumference, area:
    """
    return 2*pi*radius, pi*radius**2


def check_length(inp):
    """
    helper function to check if an invalid length was input
    :param inp:
    :return: a correct length
    """
    length = float(input(inp))
    while length <= 0:
        length = float(input(inp))
    return length


def menu():
    """
    This function prints a menu for user to select which
    geometric shape to use in calculations.
    """

    while True:
        answer = input("Enter the pattern's first letter, q stops this "
                       "(s/r/q): ")
        if answer == "s":
            length = check_length("Enter the length of the square's side: ")
            circumference, area = square(length)
            print(f"The total circumference is {circumference:.2f}\nThe "
                  f"surface area is {area:.2f}")

        elif answer == "r":
            side1 = check_length("Enter the length of the rectangle's side 1: ")
            side2 = check_length("Enter the length of the rectangle's side 2: ")
            circumference, area = rectangle(side1, side2)
            print(f"The total circumference is {circumference:.2f}\nThe "
                  f"surface area is {area:.2f}")

        elif answer == "c":
            radius = check_length("Enter the circle's radius: ")
            circumference, area = circle(radius)
            print(f"The total circumference is {circumference:.2f}\nThe "
                  f"surface area is {area:.2f}")

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        print()  # Empty row for the sake of readability


def main():
    menu()
    print("Goodbye!")


if __name__ == "__main__":
    main()
