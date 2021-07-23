"""
COMP.CS.100 str_dokumentaatio.
Tekijä: Otto 
Opiskelijanumero: 
"""


def longest_substring_in_order(inp):
    """
    finds the longest alphabetically ordered substring
    :param inp: string,
        input
    :return: string,
        substr
    """

    if len(inp) < 2:
        return inp

    best_one = ""
    prev_char = ""
    current_str = ""

    for c in inp:
        if prev_char < c:
            current_str += c
            prev_char = c
        else:
            if len(current_str) > len(best_one):
                best_one = current_str
            current_str = prev_char = c

    # lopuks sit viel viimenen vertailu täs et onks se
    # "kesken jäänyt" jono pidempi ku tallennettu
    if len(current_str) > len(best_one):
        best_one = current_str

    return best_one
