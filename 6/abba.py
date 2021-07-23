"""
COMP.CS.100 str_dokumentaatio.
Tekijä: Otto 
Opiskelijanumero: 
"""


def count_abbas(inp):
    """
    counts occurrences of the string "abba"
    :param inp: string,
        input
    :return: int,
        count
    """

    if len(inp) < 4:
        return 0

    ret = 0
    for i in range(len(inp)-3):
        if inp[i:i+4] == "abba":
            ret += 1

    return ret
