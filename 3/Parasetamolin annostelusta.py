"""
COMP.CS.100 Parasetamolin annostelusta.
Tekijä: Otto 
Opiskelijanumero: 
"""


def calculate_dose(weight, time, total_doze_24):
    if total_doze_24 >= 4000 or time < 6:
        return 0

    allowed_dose = weight * 15

    if total_doze_24 + allowed_dose >= 4000:
        return 4000-total_doze_24
    else:
        return allowed_dose


def main():
    weight = int(input("Patient's weight (kg): "))
    time = int(input("How much time has passed from the "
                     "previous dose (full hours): "))
    total_doze_24 = int(input("The total dose for the last 24 hours (mg): "))

    print("The amount of Parasetamol to give to the patient:",
          calculate_dose(weight, time, total_doze_24))


if __name__ == "__main__":
    main()
