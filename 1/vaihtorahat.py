"""
COMP.CS.100 Vaihtorahat.
Tekijä: Otto 
Opiskelijanumero: 
"""


def main():
    price = int(input("Purchase price: "))
    paid = int(input("Paid amount of money: "))
    change = paid - price

    if change < 1:
        print("No change")
    else:
        outp = "Offer change:"

        tens = change // 10
        if tens > 0:
            outp += "\n" + str(tens) + " ten-euro notes"
            change -= tens * 10

        fives = change // 5
        if fives > 0:
            outp += "\n" + str(fives) + " five-euro notes"
            change -= fives * 5

        twos = change // 2
        if twos > 0:
            outp += "\n" + str(twos) + " two-euro coins"
            change -= twos * 2

        if change > 0:
            outp += "\n" + str(change) + " one-euro coins"

        print(outp)


if __name__ == "__main__":
    main()
