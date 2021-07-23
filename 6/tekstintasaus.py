"""
COMP.CS.100 tekstintasaus.
Tekijä: Otto 
Opiskelijanumero: 
"""


def main():
    print("Enter text rows. Quit by entering an empty row.")
    inp = read_message()    # "moro mitä kuuluu :D:D :'_D :-D"
    max_length = int(input("Enter the number of characters per line: "))  # 12

    # "list comprehension"
    # luo listan kaikist sanoist poistaen tyhjät.
    # tyhjii tulee string.split(" ") kans jos on monta
    # välilöyntii peräkkäi
    words = [x for x in inp.split(" ") if x]

    words = []
    for word in inp.split(" "):
        if word:    # jos epätyhjä
            words.append(word)

    # words = ["moro", "mitä", "kuuluu" ":D:D" ":'_D", ":-D"]

    rows = []
    current_row = []
    current_row_len = 0

    # ensi tehää alalistoi, "rivei" sillee et
    # nii monta sanaa per rivi ku mahtuu siihe
    # maksimi pituutee
    for word in words:
        # jos atm rivii mahtuu viel lisää yhen sanan
        if current_row_len + len(word) <= max_length:
            current_row.append(word)
            current_row_len += len(word) + 1
        else:
            # jos atm rivi tyhjä (voi vaa tapahtuu ekan rivin ekal sanal jos
            # se sana on liia pitkä), nii ei lisää sitä tyhjää rivii tonne
            if current_row:
                rows.append(current_row)
            current_row = [word]
            current_row_len = len(word) + 1

    # sit viel lopuks se keskenjääny rivi perään mukaan
    rows.append(current_row)

    # rows = [['moro', 'mitä'], ['kuuluu', ':D:D'], [":'_D", ':-D']]

    # tallennan tän ettei tarvii turhaan laskee tota joka loopin kierros
    last_row_index = len(rows) - 1

    # enumeraten kaa saa molemmat sekä loopin indexin ja ite elementin
    for i, row in enumerate(rows):
        # jos ollaa vikas rivis nii printtaa sen vaa ja lähtee loopist vittuu
        # vikaan rivii ei pitäny pistää extra välilyöntei
        if i == last_row_index:
            print(" ".join(row))
            break

        # tallennan taas tän pituuden koska sitä tullaa käyttää kaks kertaa
        row_len = len(row)
        if row_len == 1:
            print(*row)     # jos rivis on vaa yks sana nii sit vaa printtaa
            continue        # sen ja rupee työstää seuraavaa rivii

        # kui paljo välilyöntei pitää täyttää siihe rivii et täynnä
        to_fill = max_length - len("".join(row)) - row_len + 1

        # poistan vikan sanan siit listast, koska vikan sanan perää
        # ei mitää välilöyntei lisätä
        last_word = row.pop()

        # taas tallennan sen pituuden ettei tarvii turhaa laskee
        # sitä joka loopin kierroksel
        row_len = len(row)
        for j in range(to_fill):
            # täs on ehkä vähän taikaa, mut siis kätevästi ku ottaa indexist
            # modulon elementtien määräl, nii se vastaus menee hienosti läpi
            # jokasen arrayn elementin ja sen jälkee alottaa taas alust jos
            # looppaamist riittää niinki pitkäl
            # ja sit täs vaa lisää aina yhe välilöynni kerral sen elementi perää
            row[j % row_len] += " "

        # sit onki valmis printtaamaa ekan rivin ja muistan lisätä sen
        # aijjemin poistetun vikan sanan siihe perään
        # ja sit seuraavan rivin kimppuu vaa
        print(" ".join(row), last_word)


def read_message():
    """
    vastaanottaa syötettä kunnes tyhjä rivi
    :return: string,
        syöte
    """
    ret = ""
    inp = input()

    # ei kine jos käyttäjä pistää rivin vaihtoi
    # kaikki teksti vaa pötköön ja välilöynti väliin
    while inp != "":
        ret += " " + inp
        inp = input()

    # poistetaa se extra välilöynti tost alust
    return ret[1:]


if __name__ == "__main__":
    main()
