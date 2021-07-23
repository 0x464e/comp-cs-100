"""
COMP.CS.100 Parasetamolin annostelusta.
Tekijä: Otto 
Opiskelijanumero: 
"""

EPSILON = 0.000000001


def compare_floats(a, b, tol):
    """
    checks if two floats are within a desired tolerance value
    :param a: float1
    :param b: float2
    :param tol: tolerance for the comparison
    :return: boolean
    """
    return abs(a-b) < tol
