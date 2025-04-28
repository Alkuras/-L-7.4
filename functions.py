#
def Loe_failist(fail:str)->list:
    f=open(fail,'r',encoding="utf8")

    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())

    f.close()
    print(type(jarjend[0]))
    return jarjend

def Kirjuta_failisse(fail:str,jarjend1:list,jarjend2:list,jarjend3:list):
    
    f=open(fail,'w',encoding="utf8")
    sõnastik=[]
    for e, r, g in zip(jarjend1,jarjend2, jarjend3):
        sõnastik.append({'nimi': e, 'email': r, 'number': g})

    for line in sõnastik:
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