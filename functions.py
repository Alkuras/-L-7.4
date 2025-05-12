#

import json
import os

faili_nimi="kontaktid.json"


def json_read():
    if not os.path.exists(faili_nimi):
        return []
    with open(faili_nimi, "r", encoding="utf-8") as f:
        return json.load(f)

def json_save(kontaktid):
    with open(faili_nimi, "w", encoding="utf-8") as f:
        json.dump(kontaktid,f,ensure_ascii=False, indent=4)

def lisa_kontaktt(kontaktid,nimi,email,number):

    kontaktid.append({'nimi': nimi, 'email': email, 'number': number})

def otsi_kontakt(kontaktid, nimi):
    return[k for k in kontaktid if nimi.lower() in k["nimi"].lower()]

def kustuta_kontakt(kontaktid, nimi):
    leitud = [k for k in kontaktid if k["nimi"].lower() == nimi.lower()]
    if leitud:
        kontaktid.remove(leitud[0])
        return True
    return False

def sorteeri_kontaktid(kontaktid, vaike):
    return sorted(kontaktid, key=lambda x: x[vaike].lower())

def muuda_kontakt(book,vana_nimi,uus_nimi,uus_email,uus_number):
    for k in book:
        if k["nimi"].lower()==vana_nimi.lower():
            k["nimi"]=uus_nimi
            k["email"]=uus_email
            k["number"]=uus_number
            return True
        else:
            return False
    


def Loe_failist(fail:str)->list:
    f=open(fail,'r',encoding="utf8")

    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())

    f.close()
    print(jarjend)
    return jarjend

def Kirjuta_failisse(fail:str,jarjend:list):
    f=open(fail,'w',encoding="utf8")
    for line in jarjend:
        f.write(str(line)+"\n")
    f.close()

def uus_kontakt(book:list)->list:
    nimi=input("Sisesta kontanti nimi: ")
    
    mail=input("Sisesta kontakti email: ")
    
    number=input("Sisesta kontakti numbri: ")
    book.append({'nimi': nimi, 'email': mail, 'number': number})
    return book

def show_contacts(book:list):
    print(book)
   
def find_contact(book:list):
    k=0
    name=input("Otsitav nimi: ")
    try:
        for e in book:

                  if name.lower() in e["nimi"]:
                    k+=1
                    print(e)
                    break  
    except Exception as e:
        print("Viga", e)

def kustuta_kontaktt(book:list):
  o=0
  for e in book:
        o=str(o)
        print(o+"."+" ",end=" ")
        print(e)
        o=int(o)
        o+=1
  print()
  v=int(input("Kirjuta number mida tahad kustutada"))
  book.pop(v)

def muuda_kont(book:list):
    o=0
    for e in book:
        o=str(o)
        print(o+"."+" ",end=" ")
        print(e)
        o=int(o)
        o+=1
    print()
    v=int(input("Kirjuta number mida tahad muuta "))
    while True:
        try:
            uus_est = input("Kirjuta nimi: ").strip().lower()
            if uus_est.isalpha():
                break
            else:
                print("Write a word")
        except:
            print("ERROR")
    
    while True:
        try:
            uus_rus = input("Kirjuta emaili: ").strip().lower()
            if uus_est.isalpha():
                break
            else:
                print("Write a word")
        except:
            print("ERROR")
    
    while True:
        try:
            uus_eng = input("Kirjuta numbri: ").strip().lower()
            if uus_est.isalpha():
                break
            else:
                print("Write a word")
        except:
            print("ERROR")
    book.insert(v,{'nimi': uus_est, 'email': uus_rus, 'number': uus_eng})
