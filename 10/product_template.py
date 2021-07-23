"""
COMP.CS.100 ystavaverkko.
Tekijä: Otto 
Opiskelijanumero: 
"""


class Product:
    """
    This class defines a simplified product for sale in a store.
    """
    def __init__(self, product, price):
        """
        fake docstring
        :param product:
        :param price:
        """
        self.__product = product
        self.__price = price
        self.__sale_percentage = 0.0

    def printout(self):
        """
        fake docstring
        :return:
        """
        print(f"{self.__product}\n"
              f"  price: {self.__price}\n"
              f"  sale%: {self.__sale_percentage}")

    def get_price(self):
        """
        fake docstring
        :return:
        """
        return self.__price if self.__sale_percentage == 0.00 else self.__price*(1-self.__sale_percentage/100)

    def set_sale_percentage(self, sale_percentage):
        """
        fake docstring
        :return:
        """
        self.__sale_percentage = sale_percentage



def main():
    ################################################################
    #                                                              #
    #  You can use the main-function to test your Product class.   #
    #  The automatic tests will not use the main you submitted.    #
    #                                                              #
    #  Voit käyttää main-funktiota Product-luokkasi testaamiseen.  #
    #  Automaattiset testit eivät käytä palauttamaasi mainia.      #
    #                                                              #
    ################################################################

    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
