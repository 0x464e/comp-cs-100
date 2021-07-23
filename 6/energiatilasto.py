"""
COMP.CS.100 energiatilasto.
Tekijä: Otto 
Opiskelijanumero: 
"""


def main():
    print("Enter energy consumption data.")
    print("End by entering an empty line.")
    print()

    input_data = get_user_input()
    if not input_data:
        print("Nothing to print. Done.")
    else:
        print_histogram(input_data)


def get_user_input():
    """
    Pyytää käyttäjää syöttämään energia-arvoja kunnes syöttää tyhjää

    :return: array,
        lista energia-arvoista
    """
    ret = []

    inp = input("Enter energy consumption (kWh): ")

    while inp != "":
        # vissii oli ok olettaa et sielt syötetää vaa kokonaislukui
        if int(inp) > -1:
            ret.append(int(inp))
        else:
            print(f"You entered: {inp}. Enter non-negative numbers only!")
        inp = input("Enter energy consumption (kWh): ")

    return ret


def print_histogram(input_data):
    """
    tulostaa itse histogrammin annetun datan perusteella

    :param input_data: array,
        lista energia-arvoista
    """

    input_data.sort()
    largest_class_number = len(str(input_data[-1]))
    current_index = 1   # missä luokassa ollaan menossa
    count = 0           # kuinka monta alkiota tässä luokassa

    for number in input_data:
        if len(str(number)) > current_index:    # jos luokka vaihtuu

            # jos vaihtu enemmän ku yks luokka kerralla
            # nii loopataan sen verran "tyhjii" rivei histrogrammiin
            for _ in range(len(str(number)) - current_index):
                print_single_histogram_line(current_index, count,
                                            largest_class_number)
                current_index += 1
                count = 0

            count = 1
        else:
            count += 1

    # lopuks viel viimenenki rivi sinne mukaan
    print_single_histogram_line(current_index, count, largest_class_number)


def print_single_histogram_line(class_number, count, largest_class_number):
    """
    Funktio tulostaa oikean muotoisen histogrammin rivin,
    kuhan kutsut sitä oikeilla parametrien arvoilla.

    :param class_number: int,
        Mitä kulutuskatergoriaa tulostettava rivi kuvaa (1, 2, 3, ...)
        Parametria <class_number> käytetään päättämään, mikä arvoväli
        (0-9, 10-99, 100-999, ...) riville tulostuu ennen diagrammin
        "*"-merkkejä.

    :param count: int,
        Kuinka monta "*"-merkkiä riville on tarpeen tulostaa, eli
        kuinka monta käyttäjän syöttämää arvoa kuuluu <class_number>-
        parametrin kuvaamalle välillä.

    :param largest_class_number: int,
        Mikä on kaikkein suurin kategorian numero.  Riippuu
        suurimmasta käyttäjän syöttämästä kulutusarvosta.
        Esimerkiksi jos suurin käyttäjän syöttämä luku
        oli 91827364 (8 numeromerkkiä) <largest_class_number>-parametrin
        arvon tulisi myös olla 8.  Parametrin arvoa käytetään
        määriteltäessä, kuinka monta välilyöntiä muiden kuin viimeisen
        histogrammin rivin eteen pitäisi tulostaa.
    """

    min_value = class_minimum_value(class_number)
    max_value = class_maximum_value(class_number)
    range_string = f"{min_value}-{max_value}"

    largest_width = 2 * largest_class_number + 1

    print(f"{range_string:>{largest_width}}: {'*' * count}")


def class_minimum_value(class_number):
    """
    Tuottaa kategorian alarajan katagorian indeksistä

    :param class_number:
        kategorian indeksi

    :return: int,
        kategorian alaraja
    """
    if class_number == 1:
        return 0
    return 10**(class_number-1)


def class_maximum_value(class_number):
    """
    Tuottaa kategorian ylärajan katagorian indeksistä

    :param class_number:
        kategorian indeksi

    :return: int,
        kategorian yläraja
    """
    return 10**class_number-1


if __name__ == "__main__":
    main()
