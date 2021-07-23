"""
COMP.CS.100 alkioiden_yhtasuuruus.
Tekijä: Otto 
Opiskelijanumero: 
"""


def are_all_members_same(arr):
    """
    checks if each elem on the list is the same
    :param arr:
    :return:
    """
    return arr[1:] == arr[:-1]
