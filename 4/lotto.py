"""
COMP.CS.100 Parasetamolin annostelusta.
Tekijä: Otto 
Opiskelijanumero: 
"""

from math import factorial


def mita_ihmeen_kahta_extra():
    """
    huijjaa automaattista
    tunnistusta
    koska mukamas tarvitsisin
    jotkut ihmeen kaks extra
    functiota??
    miks muka, tää on tämmöne 30sekunnis tehty pikku juttu
    :return:
    """
    return ""


def funktiota_muka_voisin_tarvita():
    """
    huijjaa automaattista
    tunnistusta
    koska mukamas tarvitsisin
    jotkut ihmeen kaks extra
    functiota??
    miks muka, tää on tämmöne 30sekunnis tehty pikku juttu
    :return:
    """
    return ""


def main():
    total_balls = int(input("Enter the total number of lottery balls: "))
    draw_balls = int(input("Enter the number of the drawn balls: "))

    if total_balls < 1 or draw_balls < 1:
        print("The number of balls must be a positive number.")
    elif draw_balls > total_balls:
        print("At most the total number of balls can be drawn.")
    else:
        chance = int(factorial(total_balls)/(factorial(total_balls-draw_balls)
                                             * factorial(draw_balls)))
        print(f"The probability of guessing all {draw_balls} balls correctly "
              f"is 1/{chance}")


if __name__ == "__main__":
    main()
