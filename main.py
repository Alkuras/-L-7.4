from functions import *
book=[]
names=[]
emails=[]
numbers=[]
while True:
    print("Tere tulemas menüüsse")
    v=int(input("""
    

    1- Failist andmete lugemine ja faili kirjutamine.

    2- Uue kontakti lisamine.

    3- Kõigi kontaktide kuvamine.

    4- Kontakti otsimine nime järgi.

    5- Kontakti kustutamine.

    6- Kontakti muutmine (kõik väljad: nimi, telefon, e-mail).

    7- Kontaktide sorteerimine (valiku järgi: nimi, telefon või e-mail).
    
    8- Saada e-kiri

    9- Välja 
    """))

    if v==1:
        p=int(input("Kontakte laadimine - 1.\nKontakte salvestamine - 2."))
        if p==1:
            book=Loe_failist("kontakt.txt")
            print(book)
        elif p==2:
            Kirjuta_failisse("kontakt.txt",names,emails,numbers)
    elif v==2:
        uus_kontakt(book)
    elif v==3:
        show_contacts(book)
    elif v==4:
        find_contact(book)