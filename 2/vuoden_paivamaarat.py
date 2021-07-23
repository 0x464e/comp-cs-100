"""
COMP.CS.100 Vuoden päivämäärät.
Tekijä: Otto 
Opiskelijanumero: 
"""

Days_In_Months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def main():
    for m in range(1, 13):
        for d in range(1, Days_In_Months[m-1]+1):
            print(f"{d}.{m}.")


if __name__ == "__main__":
    main()