"""
COMP.CS.100 TGIF.
Tekijä: Otto 
Opiskelijanumero: 
"""

Days_In_Months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def main():
    day = -3
    for m in range(1, 13):
        for d in range(1, Days_In_Months[m-1]+1):
            day += 1
            if day % 7 == 0:
                print(f"{d}.{m}.")


if __name__ == "__main__":
    main()
