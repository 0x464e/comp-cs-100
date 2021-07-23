"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tekijä: Otto 
Opiskelijanumero: 

Project: accesscontrol

A program which controls access to doors via door codes and area access codes.
Door codes and are codes are defined in DOORCODES and unique access cards,
identified by an id, are read from a text file 'accessinfo.txt'.

The program can print info about specific access cards and add access codes
to them.
"""

# Global variable containing all access codes and areas
DOORCODES = {'TC114': ['TIE'],
             'TC203': ['TIE'],
             'TC210': ['TIE', 'TST'],
             'TD201': ['TST'],
             'TE111': [],
             'TE113': [],
             'TE115': [],
             'TE117': [],
             'TE102': ['TIE'],
             'TD203': ['TST'],
             'TA666': ['X'],
             'TC103': ['TIE', 'OPET', 'SGN'],
             'TC205': ['TIE', 'OPET', 'ELT'],
             'TB109': ['OPET', 'TST'],
             'TB111': ['OPET', 'TST'],
             'TB103': ['OPET'],
             'TB104': ['OPET'],
             'TB205': ['G'],
             'SM111': [],
             'SM112': [],
             'SM113': [],
             'SM114': [],
             'S1': ['OPET'],
             'S2': ['OPET'],
             'S3': ['OPET'],
             'S4': ['OPET'],
             'K1705': ['OPET'],
             'SB100': ['G'],
             'SB202': ['G'],
             'SM220': ['ELT'],
             'SM221': ['ELT'],
             'SM222': ['ELT'],
             'secret_corridor_from_building_T_to_building_F': ['X', 'Y', 'Z'],
             'TA': ['G'],
             'TB': ['G'],
             'SA': ['G'],
             'KA': ['G']}

# since the DOORCODES object is constant, we can define a global constant list
# of access area codes, which we can efficiently refer to during runtime
# without having to traverse through the DOORCODES object every time
ACCESSAREACODES = []

for area_list in DOORCODES.values():
    # for each value
    for area_code in area_list:
        # for each area code in list of area codes
        if area_code not in ACCESSAREACODES:
            # append if not already in the list
            ACCESSAREACODES.append(area_code)

# Global object, which contains all the Accesscard objects
# Key: Accesscard id
# Value: Accesscard object
ACCESSCARDS = {}


class Accesscard:
    """
    This class models an access card which can be used to check
    whether a card should open a particular door or not.
    """

    def __init__(self, id, name):
        """
        Constructor, creates a new object that has no access rights.

        :param id: str, card holders personal id
        :param name: str, card holders name

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME OR THE
        PARAMETERS!
        """

        self.__id = id
        self.__name = name
        self.__access_codes = []

    def info(self):
        """
        The method has no return value. It prints the information related to
        the access card in the format:
        id, name, access: a1,a2,...,aN
        for example:
        777, Thelma Teacher, access: OPET, TE113, TIE
        Note that the space characters after the commas and semicolon need to
        be as specified in the task description or the test fails.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE PRINTOUT FORMAT!
        """

        print(f"{self.__id}, {self.__name}, access: "
              f"{', '.join(sorted(self.__access_codes))}")

    def get_name(self):
        """
        :return: Returns the name of the accesscard holder.
        """
        return self.__name

    def add_access(self, new_access_code):
        """
        The method adds a new accesscode into the accesscard according to the
        rules defined in the task description.

        :param new_access_code: str, the accesscode to be added in the card.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """
        if is_valid_access(new_access_code) \
                and new_access_code not in self.__access_codes:
            # if access code is valid and not already found in the card
            self.__access_codes.append(new_access_code)
            self.clean_access_codes()

    def clean_access_codes(self):
        """
        Removes redundant access codes, i.e door codes which are
        covered by an area code.
        """

        if len(self.__access_codes) < 2:
            # if there are 0-1 access codes, there can't possibly be
            # any redundant ones
            return

        # extract all area codes from the card's access codes
        card_area_codes = [code for code in self.__access_codes
                           if code in ACCESSAREACODES]

        for area_code in card_area_codes:
            # for each area code in the access card
            for door_code in DOORCODES:
                # for each door
                if area_code in DOORCODES[door_code] \
                        and door_code in self.__access_codes:
                    # if the door can be accessed with the area access, and the
                    # door's code is included in the access card, remove it
                    self.__access_codes.remove(door_code)

    def check_access(self, door):
        """
        Checks if the accesscard allows access to a certain door.

        :param door: str, the doorcode of the door that is being accessed.
        :return: True: The door opens for this accesscard.
                 False: The door does not open for this accesscard.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """

        # if the door code is in the card, or if any of the area codes, which
        # unlock the door, are in the card by using a generator expression
        return door in self.__access_codes \
               or any(area_code in self.__access_codes
                      for area_code in DOORCODES[door])

    def merge(self, card):
        """
        Merges the accesscodes from another accesscard to this accesscard.

        :param card: Accesscard, the accesscard whose access rights are added
            to this card.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """

        # merge access codes
        self.__access_codes.extend(card.__access_codes)

        # convert to a set to remove duplicates and then convert back to a list
        self.__access_codes = list(set(self.__access_codes))
        self.clean_access_codes()


def is_valid_access(access_codes):
    """
    Checks if the given list of access codes is valid.
    Can also be a single access code
    :param access_codes: str, csv of accesses, can be empty
    :return: bool
    """
    # an empty list is valid
    if not access_codes:
        return True

    for code in access_codes.split(","):
        # if code is empty
        # or code is neither a room code or an area code
        if (not code) or ((code not in DOORCODES) and
                          (code not in ACCESSAREACODES)):
            return False

    # all codes are fine if we got this far
    return True


def read_input_file():
    """
    Parses a csv input file of acesscards and pushes the results to a global
    variable 'ACCESSCARDS' defined above.
    :return: bool, successful or unsuccessful parsing of the csv
    """

    try:
        input_file = open("accessinfo.txt", "r")
    except OSError:
        # file couldn't be read
        return False

    # store the input csv ids so we can conveniently check for duplicates
    ids = []

    for line in input_file:
        # id;name;access\n
        values = line.rstrip().split(";")
        if len(values) != 3:
            return False

        id = values[0]
        name = values[1]
        access = values[2]

        # if id or name empty
        # or duplicate id
        # or invalid access code(s)
        if (not id) or (not name) or (id in ids) \
                or (not is_valid_access(access)):
            return False

        # note id as used
        ids.append(id)

        # create new accesscard object
        access_card = Accesscard(id, name)

        # if there are access codes, add each access code to the card
        # individually since the constructor doesn't allow passing
        # a list straight in (..??)
        if access:
            for access_code in access.split(","):
                access_card.add_access(access_code)

        # add the access card to the database
        # key: id
        # value: accesscard object
        ACCESSCARDS[id] = access_card

    # the whole csv was parsed successfully if we got this far
    return True


def main():
    if not read_input_file():
        # error and exit the program if input csv is invalid
        print("Error: file cannot be read.")
        return

    while True:
        line = input("command> ")

        if line == "":
            break

        strings = line.split()
        command = strings[0]

        # print info all access cards found in the database
        if command == "list" and len(strings) == 1:
            for card in sorted(ACCESSCARDS):
                ACCESSCARDS[card].info()

        # print info of a specific access card
        elif command == "info" and len(strings) == 2:
            card_id = strings[1]
            if card_id not in ACCESSCARDS:
                print("Error: unknown id.")
            else:
                ACCESSCARDS[card_id].info()

        # check if an access card has access to a specific door
        elif command == "access" and len(strings) == 3:
            card_id = strings[1]
            door_id = strings[2]
            if card_id not in ACCESSCARDS:
                print("Error: unknown id.")
            elif door_id not in DOORCODES:
                print("Error: unknown doorcode.")
            else:
                card = ACCESSCARDS[card_id]
                print(f"Card {card_id} ( {card.get_name()} ) has "
                      # add word "no" if there was no access
                      f"{'no ' if not card.check_access(door_id) else ''}"
                      f"access to door {door_id}")

        # add an access code to an access card
        elif command == "add" and len(strings) == 3:
            card_id = strings[1]
            access_code = strings[2]
            if card_id not in ACCESSCARDS:
                print("Error: unknown id.")
            elif not is_valid_access(access_code):
                print("Error: unknown accesscode.")
            else:
                ACCESSCARDS[card_id].add_access(access_code)

        # copy access codes from one card to an other
        elif command == "merge" and len(strings) == 3:
            card_id_to = strings[1]
            card_id_from = strings[2]
            if card_id_to not in ACCESSCARDS \
                    or card_id_from not in ACCESSCARDS:
                print("Error: unknown id.")
            else:
                ACCESSCARDS[card_id_to].merge(ACCESSCARDS[card_id_from])

        elif command == "quit":
            print("Bye!")
            return
        else:
            print("Error: unknown command.")


if __name__ == "__main__":
    main()
