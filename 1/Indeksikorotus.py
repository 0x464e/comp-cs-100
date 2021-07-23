"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Otto 
Opiskelijanumero: 
"""


benefits = input("Enter the amount of the study benefits: ")
raise1 = float(benefits)*1.0117
print("""If the index raise is 1.17 percent, the study benefit,
after a raise, would be""", raise1, """euros
and if there was another index raise, the study
benefits would be as much as""", raise1*1.0117, "euros")
