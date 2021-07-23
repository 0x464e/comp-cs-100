"""
COMP.CS.100 pistekirjanpito_a.
Tekijä: Otto 
Opiskelijanumero: 
"""


def main():

    counted_scores = {}
    try:
        file = open(input("Enter the name of the score file: "), "r")
    except OSError:
        print("There was an error in reading the file.")
        return

    scores = []
    for line in file:
        parts = line.split()
        if len(parts) != 2:
            print("There was an erroneous line in the file:\n" + line)
            return
        scores.append(parts)

    for score in scores:
        try:
            if score[0] in counted_scores:
                counted_scores[score[0]] += int(score[1])
            else:
                counted_scores[score[0]] = int(score[1])
        except ValueError:
            print("There was an erroneous score in the file:\n" + score[1])
            return

    print("Contestant score:")
    print("\n".join([f"{x} {y}" for x, y in sorted(counted_scores.items())]))





if __name__ == "__main__":
    main()
