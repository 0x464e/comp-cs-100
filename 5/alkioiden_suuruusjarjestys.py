"""
COMP.CS.100 alkioiden_suuruusjarjestys.
Tekijä: Otto 
Opiskelijanumero: 
"""


def is_the_list_in_order(arr):
    """
    checks if each elem on the list is the same
    :param arr:
    :return:
    """
    return arr == sorted(arr)
