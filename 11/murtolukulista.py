"""
COMP.CS.100 murtolukulista.
Tekijä: Otto 
Opiskelijanumero: 
"""


class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def __lt__(self, other):
        return self.__numerator/self.__denominator < \
               other.__numerator / other.__denominator

    def __gt__(self, other):
        return self.__numerator/self.__denominator > \
               other.__numerator / other.__denominator

    def __str__(self):
        return self.return_string()

    def simplify(self):
        """
        fake docstrging
        :return:
        """
        gcd = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator //= gcd
        self.__denominator //= gcd

    def complement(self):
        """
        fake docstring
        :return:
        """
        return Fraction(-1*self.__numerator, self.__denominator)

    def reciprocal(self):
        """
        fake docstring
        :return:
        """
        return Fraction(self.__denominator, self.__numerator)

    def multiply(self, frac_obj):
        """
        fake docstring
        :return:
        """
        return Fraction(self.__numerator * frac_obj.__numerator,
                        self.__denominator * frac_obj.__denominator)

    def divide(self, frac_obj):
        """
        fake docstring
        :return:
        """
        return Fraction(self.__numerator * frac_obj.__denominator,
                        self.__denominator * frac_obj.__numerator)

    def add(self, frac_obj):
        """
        fake docstring
        :return:
        """
        return Fraction(frac_obj.__denominator * self.__numerator
                        + self.__denominator * frac_obj.__numerator,
                        self.__denominator * frac_obj.__denominator)

    def deduct(self, frac_obj):
        """
        fake docstring
        :return:
        """
        return Fraction(frac_obj.__denominator * self.__numerator
                        - self.__denominator * frac_obj.__numerator,
                        self.__denominator * frac_obj.__denominator)

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a


def read_message():
    """
    vastaanottaa syötettä kunnes tyhjä rivi
    :return: array,
        syötteet
    """
    ret = []
    inp = input()

    while inp != "":
        ret.append(inp)
        inp = input()

    return ret


def main():
    print("Enter fractions in the format integer/integer.\n"
          "One fraction per line. Stop by entering an empty line.")
    print_out = "The given fractions in their simplified form:\n"

    while True:
        inp = input()
        if inp == "":
            break
        split = [int(x) for x in inp.split("/")]
        frac = Fraction(split[0], split[1])
        og = frac.return_string()
        frac.simplify()
        print_out += f"{og} = {frac.return_string()}\n"

    print(print_out.rstrip())


if __name__ == "__main__":
    main()