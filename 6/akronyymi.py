"""
COMP.CS.100 akronyymi.
Tekijä: Otto 
Opiskelijanumero: 
"""


def create_an_acronym(inp):
    """
    creates an acronym
    :param inp: string, 
        input
    :return: string,
        output acronym
    """

    return "".join([x[0].upper() for x in inp.split(" ")])
