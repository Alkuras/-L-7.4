#
import ast
def ast_read():
    jarjend=[]
    with open('kontakt.txt',encoding="utf8") as f: 
        # data = f.read() 
        # o=ast.literal_eval(data)
        for rida in f:
            rida=ast.literal_eval(rida)
            jarjend.append(rida)
    return jarjend
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

def kustuta_kontakt(book:list):
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

def muuda_kontakti(book:list):
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
