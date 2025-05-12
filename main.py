

from functions import *
from tkinter import *
from tkinter import messagebox

def lisa_kontakt():
    nimi=e1.get()
    email=e2.get()
    number=e3.get()
    if nimi.isalpha() and number.isnumeric():
        if nimi and number and email:
            lisa_kontaktt(book,nimi,email,number)
            json_save(book)
            messagebox.showinfo("Edu","Kontakt lisatud.")
            e1.delete(0,"end")
            e2.delete(0,"end")
            e3.delete(0,"end")
            kuva_kontakt()
            book.append({'nimi': nimi, 'email': email, 'number': number})
        else:
            messagebox.showwarning("Tühjad väljad", "Täida kõik väljad.")

    
    
    
def kuva_kontakt():
    tekstikast.delete("1.0","end")
    for kontakt in book:
        nimi=kontakt["nimi"]
        meil=kontakt["email"]
        number=kontakt["number"]
        tekstikast.insert("end", f"{nimi} | {meil} | {number}\n")

def otsi_kontakt_gui():
    nimi=e1.get()
    tulemused=otsi_kontakt(book,nimi)
    if tulemused:
        kontakt=tulemused[0]
        otsingu_viide.set(kontakt["nimi"])
        e1.delete(0,"end")
        e1.insert(0,kontakt["nimi"])
        e2.delete(0,"end")
        e2.insert(0,kontakt["email"])   
        e3.delete(0,"end")
        e3.insert(0,kontakt["number"])
        tekstikast.delete("1.0","end")
        nimi=kontakt["nimi"]
        meil=kontakt["email"]
        number=kontakt["number"]
        tekstikast.insert("end",f"Leitud: {nimi} | {meil} | {number}\n")
    else:
        messagebox.showinfo("Tulemus puudub", "Kontakt ei leitud.")

def kustuta_kontakt_gui():
    nimi = e1.get()
    if kustuta_kontakt(book,nimi):
        json_save(book)
        messagebox.showinfo("Kustutatud", f"´{nimi}´ kusutati.")
        kuva_kontakt()
    else:
        messagebox.showwarning("Ei leitud", "Kontakti ei leitud.")

def sorteeri_gui():
    kontaktid_sorted= sorteeri_kontaktid(book,"nimi")
    tekstikast.delete("1.0","end")
    for kontakt in kontaktid_sorted:
        nimi=kontakt["nimi"]
        meil=kontakt["email"]
        number=kontakt["number"]
        tekstikast.insert("end",f"Leitud: {nimi} | {meil} | {number}\n")

def muuda_kontakti_gui():
    vana_nimi=otsingu_viide.get()

    uus_nimi=e1.get()
    uus_email=e2.get()
    uus_number=e3.get()

    if vana_nimi and uus_nimi and uus_number and uus_email:
        õnnestus=muuda_kontakt(book,vana_nimi,uus_nimi,uus_email,uus_number,)
        if õnnestus:
            json_save(book)
            messagebox.showinfo("Muudetud", f"´{vana_nimi}´ andmed on muudetud.")
            kuva_kontakt()
        else:
            messagebox.showwarning("Tõrge", "Kontakti ei leitud muudatuseks.")
    else:
        messagebox.showwarning("Puuduvad andmed", "Palun täida kõik väljad.")
book=json_read()




aken=Tk()
aken.title("Kontaktid")
aken.geometry("700x400")
aken.configure(bg="orange")
aken.resizable(width=False, height=False)
otsingu_viide=StringVar()
otsingu_viide.set("")
aken.iconbitmap("catdog.ico")

nupp3=Button(aken,text="Sorteerimine nimi järgi.",bg="purple",fg="white",width=25,font=("Algerian",12),command=lambda: sorteeri_gui())
nupp5=Button(aken,text="Kontakti otsimine nime järgi.",bg="purple",fg="white",width=25,font=("Algerian",12),command=lambda: otsi_kontakt_gui())
nupp6=Button(aken,text="Kontakti kustutamine.",bg="brown",fg="white",width=25,font=("Algerian",12),command=lambda: kustuta_kontakt_gui())
nupp7=Button(aken,text="Kontakti muutmine.",bg="brown",fg="white",width=25,font=("Algerian",12),command=lambda: muuda_kontakti_gui())
accept=Button(aken,text="Lisa kontakt",bg="purple",fg="white",width=25,font=("Algerian",12),command=lambda: lisa_kontakt())
accept2=Button(aken,text="Kuva kontaktid",bg="brown",fg="white",width=25,font=("Algerian",12),command=lambda: kuva_kontakt())
tekstikast =Text(aken, height=15, width=40,bg="dark orange")
l1 = Label(aken, text = "Nimi:",bg="orange")
l2 = Label(aken, text = "Email:",bg="orange")
l3 = Label(aken, text= "Number: ",bg="orange")
e1 = Entry(aken,bg="dark orange")
e2 = Entry(aken,bg="dark orange")
e3 = Entry(aken,bg="dark orange")
pilt=PhotoImage(file="catdoggg.png")
pilt_label=Label(aken,image=pilt,bg="orange")

nupp3.grid(row = 6, column = 2, pady = 2)
nupp6.grid(row = 5, column = 2, pady = 2)
nupp5.grid(row = 4, column = 2, pady = 2)
nupp7.grid(row = 7, column = 2, pady = 2)
accept.grid(row = 2,column = 2, pady=2)
accept2.grid(row = 3,column = 2, pady=2)
pilt_label.grid(row= 8, column = 2, pady=3)
l1.grid(row = 2, column = 0, sticky = W, pady = 2)
l2.grid(row = 3, column = 0, sticky = W, pady = 2)
l3.grid(row = 4, column = 0, sticky = W, pady = 2)
e1.grid(row = 2, column = 1, pady = 2)
e2.grid(row = 3, column = 1, pady = 2)
e3.grid(row = 4, column = 1, pady = 2)
tekstikast.grid(row=6,pady =5, columnspan=2,rowspan=10 )

aken.mainloop()


























# book=[]
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
#             book=json_read()
#             print(book)
#         elif p==2:
#             json_save(book)
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