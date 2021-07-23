"""
COMP.CS.100 rubikinkuutio.
Tekijä: Otto 
Opiskelijanumero: 
"""


def convert_grades(arr):
    """
    converts each elem in the array to 6 if it's non zero
    :param arr:
    :return:
    """
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i] = 6


def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()
