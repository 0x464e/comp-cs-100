"""
COMP.CS.100 montako_loytyy.
Tekijä: Otto 
Opiskelijanumero: 
"""


def input_to_list(count):
    """
    Generates a list of x numbers from user input
    :param count: amount of numbers
    :return:
    """
    arr = []
    print(f"Enter {count} numbers:")
    for _ in range(count):
        arr.append(int(input()))
    return arr


def main():
    numbers = input_to_list(int(input("How many numbers do you want to process: ")))
    search = int(input("Enter the number to be searched: "))
    matches = numbers.count(search)
    if matches != 0:
        print(f"{search} shows up {numbers.count(search)} times among the "
              f"numbers you have entered.")
    else:
        print(f"{search} is not among the numbers you have entered.")


if __name__ == "__main__":
    main()
