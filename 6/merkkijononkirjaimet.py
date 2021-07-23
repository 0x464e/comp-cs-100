"""
COMP.CS.100 merkkijononkirjaimet.
Tekijä: Otto 
Opiskelijanumero: 
"""


def main():
    vowels = list("aeiouyäö")
    consonants = "b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,z".split(",")
    word = list(input("Enter a word: "))
    print(f"The word {''.join(word)} contains {len([x for x in word if x in vowels])}"
          f" vowels and {len([x for x in word if x in consonants])} consonants")


if __name__ == "__main__":
    main()
