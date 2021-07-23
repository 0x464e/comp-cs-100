"""
COMP.CS.100 nimet.
Tekijä: Otto 
Opiskelijanumero: 
"""


def reverse_name(name):
    """
    reverses first name and surname
    :param name: name
    :return: string
        reversed name
    """
    i = name.find(",")
    last_name = name[0:i]
    first_name = name[i+1:].strip()
    return (first_name + " " + last_name).strip()
