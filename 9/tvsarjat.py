"""
COMP.CS.100 tvsarjat.
Tekijä: Otto 
Opiskelijanumero: 
"""


def read_file(filename):
    """
    Reads and saves the series and their genres from the file.
    :param filename: name of the file to be read
    :return: a database of tv show genres and tv shows under those genres
    """

    database = {}

    try:
        file = open(filename, mode="r")

        for row in file:
            # If the input row was correct, it contained two parts:
            # · the show name before semicolon (;) and
            # · comma separated list of genres after the semicolon.
            # If we know that a function (method split in this case)
            # returns a list containing two elements, we can assign
            # names for those elements as follows:
            name, genres = row.rstrip().split(";")

            genres = genres.split(",")

            for genre in genres:
                if genre in database:
                    database[genre].append(name)
                else:
                    database[genre] = [name]

        file.close()
        return database

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    
    filename = input("Enter the name of the file: ")

    genre_data = read_file(filename)

    print("Available genres are:", ", ".join(sorted(genre_data.keys())))
    while True:
        genre = input("> ")

        if genre == "exit":
            return

        if genre in genre_data:
            print("\n".join(sorted(genre_data[genre])))


if __name__ == "__main__":
    main()