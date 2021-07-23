"""
COMP.CS.100 kolmion_kulmat.
Tekijä: Otto 
Opiskelijanumero: 
"""


def calculate_angle(angle1, angle2=90):
    """
    calculates the 3rd angle of a triange
    :param angle1: angle
    :param angle2: defaults to 90
    :return: 3rd angle
    """
    return 180-angle1-angle2
