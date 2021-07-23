"""
COMP.CS.100 Fibonacci lukusarja.
Tekijä: Otto 
Opiskelijanumero: 
"""


def main():
    inp = int(input("How many Fibonacci numbers do you want? "))
    prev2 = 0
    prev1 = 1
    print("1. 1")
    for i in range(inp-1):
        summation = prev2 + prev1
        print(f"{i+2}. {summation}")
        prev2 = prev1
        prev1 = summation


if __name__ == "__main__":
    main()
