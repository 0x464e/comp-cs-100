"""
COMP.CS.100 bussi.
Tekijä: Otto 
Opiskelijanumero: 
"""


def main():
    times = [630, 1015, 1415, 1620, 1720, 2000, 630, 1015, 1415]
    time = int(input("Enter the time (as an integer): "))
    if time > 2000:
        time = 0
    i = 0
    for t in times:
        if t >= time:
            print("The next buses leave:\n" + "\n".join(str(n) for n in times[i:i+3]))
            return
        i += 1


if __name__ == "__main__":
    main()
