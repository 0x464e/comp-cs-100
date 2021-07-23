"""
COMP.CS.100 murtolukulaskin.
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


def main():
    memory = {}
    while True:
        command = input("> ")

        if command == "quit":
            print("Bye bye!")
            break

        elif command == "add":
            inp = input("Enter a fraction in the form integer/integer: ")
            numbers = [int(x) for x in inp.split("/")]
            name = input("Enter a name: ")
            memory[name] = Fraction(numbers[0], numbers[1])

        elif command == "print":
            name = input("Enter a name: ")
            if name not in memory:
                print(f"Name {name} was not found")
                continue
            print(f"{name} = {memory[name]}")

        elif command == "list":
            if not memory:
                continue
            print("\n".join([f"{key} = {memory[key]}" for key in sorted(memory.keys())]))

        elif command == "*":
            first = input("1st operand: ")
            if first not in memory:
                print(f"Name {first} was not found")
                continue

            second = input("2nd operand: ")
            if second not in memory:
                print(f"Name {second} was not found")
                continue

            mult = memory[first].multiply(memory[second])
            print(f"{memory[first]} * {memory[second]} = {mult}")
            mult.simplify()
            print("simplified", mult)

        elif command == "file":
            try:
                file = open(input("Enter the name of the file: "), "r")
            except OSError:
                print("Error: the file cannot be read.")
                continue

            for line in file:
                try:
                    name, numerator, denominator = line.replace("=", "/").split("/")
                    memory[name] = Fraction(int(numerator), int(denominator))
                except ValueError:
                    print("Error: the file cannot be read.")

        else:
            print("Unknown command!")


if __name__ == "__main__":
    main()