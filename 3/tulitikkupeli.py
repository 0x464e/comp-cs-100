"""
COMP.CS.100 tulitikkupeli.
Tekijä: Otto 
Opiskelijanumero: 
"""


def main():
    total_sticks = 21
    player = 0

    # oli vissii ok olettaa et sielt
    # tulee inputtina aina intti
    sticks = int(input("Game of sticks\n"
                       "Player 1 enter how many sticks to remove: "))

    while True:
        if sticks not in range(1, 4):
            sticks = int(input("Must remove between 1-3 sticks!\n"
                               f"Player {player+1} enter how many "
                               "sticks to remove: "))
        else:
            total_sticks -= sticks
            if total_sticks <= 0:
                print(f"Player {player+1} lost the game!")
                break

            # togglaan xorilla
            player ^= 1
            # ei vissii pitäny välittää siit et monikko "are ... sticks" ei
            # toimi jos on vaa 1 tikku jäljel
            sticks = int(input(f"There are {total_sticks} sticks left\n"
                               f"Player {player+1} enter how many "
                               "sticks to remove: "))


if __name__ == "__main__":
    main()
