"""
COMP.CS.100 rubikinkuutio.
Tekijä: Otto 
Opiskelijanumero: 
"""


def main():
    arr = []
    for i in range(5):
        arr.append(float(input(f"Enter the time for performance {i+1}: ")))
    print(f"The official competition score is {sum(sorted(arr)[1:4])/3:.2f} seconds.")


if __name__ == "__main__":
    main()
