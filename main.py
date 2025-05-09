from functions import *
from tkinter import *
from tkinter import messagebox

def lisa_kontakt():
    nimi=e1.get()
    email=e2.get()
    number=e3.get()
    
    book.append({'nimi': nimi, 'email': email, 'number': number})
    f=open("kontakt.txt",'w',encoding="utf8")
    for line in book:
        f.write(str(line)+"\n")
    f.close()
    print(book)
def kuva_kontakt():
    tekstikast.get(book)
book=[]
book=ast_read()


aken=Tk()
aken.title("Kontaktid")
aken.geometry("600x400")
aken.configure(bg="white")
aken.resizable(width=True, height=True)
aken.iconbitmap("catdog.ico")
display=Label(aken,text="Tere tulemast kontakt raamatusse!",bg="white",fg="black",font=("Arial",15))
# pealkiri=Label(aken,text="Tere tulemast kontakt raamatusse!",bg="orange",fg="brown",font=("Arial",20))
# nupp1=Button(aken,text="Kontakte laadimine",bg="red",fg="white",font=("Arial",15),command=lambda: book=ast_read())
# nupp2=Button(aken,text="Kontakte salvestamine",bg="red",fg="white",font=("Arial",15),command=lambda: Kirjuta_failisse("kontakt.txt",book))
# nupp3=Button(aken,text="Uue kontakti lisamine.",bg="red",fg="white",font=("Arial",15),command=lambda: uus_kontakt(book))
# nupp4=Button(aken,text="Kõigi kontaktide kuvamine.",bg="red",fg="white",font=("Arial",15),command=lambda: show_contacts(book))
# nupp5=Button(aken,text="Kontakti otsimine nime järgi.",bg="red",fg="white",font=("Arial",15),command=lambda: find_contact(book))
# nupp6=Button(aken,text="Kontakti kustutamine.",bg="red",fg="white",font=("Arial",15),command=lambda: kustuta_kontakt(book))
# nupp7=Button(aken,text="Kontakti muutmine (kõik väljad: nimi, telefon, e-mail).",bg="red",fg="white",font=("Arial",15),command=lambda: muuda_kontakti(book))
rida=Frame(aken)

accept=Button(aken,text="Lisa kontakt",bg="red",fg="black",font=("Arial",15),command=lambda: lisa_kontakt())
accept2=Button(aken,text="Kuva kontaktid",bg="red",fg="black",font=("Arial",15),command=lambda: kuva_kontakt())
tekstikast =Text(aken, height=10, width=50)
l1 = Label(aken, text = "Nimi:")
l2 = Label(aken, text = "Email:")
l3 = Label(aken, text= "Number: ")
e1 = Entry(aken)
e2 = Entry(aken)
e3 = Entry(aken)


# pealkiri.grid(row = 0, column = 0, sticky = W, pady = 2)
# nupp2.grid(row = 1, column = 0, sticky = W, pady = 2)
# nupp3.grid(row = 2, column = 0, sticky = W, pady = 2)
# nupp4.grid(row = 3, column = 0, sticky = W, pady = 2)
# nupp5.grid(row = 4, column = 0, sticky = W, pady = 2)
# nupp6.grid(row = 5, column = 0, sticky = W, pady = 2)
# nupp7.grid(row = 6, column = 0, sticky = W, pady = 2)
l1.grid(row = 1, column = 0, sticky = W, pady = 2)
l2.grid(row = 2, column = 0, sticky = W, pady = 2)
l3.grid(row = 3, column = 0, sticky = W, pady = 2)
e1.grid(row = 1, column = 1, pady = 2)
e2.grid(row = 2, column = 1, pady = 2)
e3.grid(row = 3, column = 1, pady = 2)
accept.grid(row = 4,column = 2, pady=2)
accept2.grid(row = 5,column = 2, pady=2)

tekstikast.grid(row=5,pady =5, columnspan=2 )





aken.mainloop()



























# while True:
#     print("Tere tulemas menüüsse")
#     v=int(input("""
    

#     1- Failist andmete lugemine ja faili kirjutamine.

#     2- Uue kontakti lisamine.

#     3- Kõigi kontaktide kuvamine.

#     4- Kontakti otsimine nime järgi.

#     5- Kontakti kustutamine.

#     6- Kontakti muutmine (kõik väljad: nimi, telefon, e-mail).

#     7- Kontaktide sorteerimine (valiku järgi: nimi, telefon või e-mail).
    
#     8- Saada e-kiri

#     9- Välja 
#     """))

#     if v==1:
#         p=int(input("Kontakte laadimine - 1.\nKontakte salvestamine - 2."))
#         if p==1:
#             #book=Loe_failist("kontakt.txt")
#             book=ast_read()
#             print(book)
#         elif p==2:
#             Kirjuta_failisse("kontakt.txt",book)
#     elif v==2:
#       uus_kontakt(book)
#     elif v==3:
#         show_contacts(book)
#     elif v==4:
#         find_contact(book)
#     elif v==5:
#         kustuta_kontakt(book)
#     elif v==6:
#         muuda_kontakti(book)