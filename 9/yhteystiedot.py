"""
COMP.CS.100 yhteystiedot.
Tekijä: Otto 
Opiskelijanumero: 
"""


def read_file(filename):
    """
    parses a csv file
    :param filename: name of the file containing the csv
    :return: parsed csv
    """
    database = {}
    keys = []

    for i, row in enumerate(open(filename, mode="r")):
        if i == 0:
            keys = row.rstrip().split(";")
            continue
        values = [x for x in row.rstrip().split(";") if x]
        database[values[0]] = {}
        for j, value in enumerate(values):
            database[values[0]][keys[j]] = value

    return database

