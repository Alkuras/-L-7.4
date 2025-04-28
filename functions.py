# import ast
# def ast_read():
#     jarjend=[]
#     with open('kontakt.txt',encoding="utf8") as f: 
#         data = f.read() 
#         o=ast.literal_eval(data)
#         for rida in f:
#             rida=ast.literal_eval(rida)
#             jarjend.append((rida.strip()))
#     return jarjend

def Loe_failist(fail:str)->list:
    f=open(fail,'r',encoding="utf8")
    s=0
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
        dict(jarjend[s])
        s+=1
    f.close()
    print(type(jarjend[0]))
    return jarjend

def Kirjuta_failisse(fail:str,jarjend1:list,jarjend2:list,jarjend3:list):
    
    f=open(fail,'w',encoding="utf8")
    sõnastik=[]
    for e, r, g in zip(jarjend1,jarjend2, jarjend3):
        sõnastik.append({'nimi': e, 'email': r, 'number': g})
    # for line in jarjend1:
    #     f.write(str(line)+":")
    # for line in jarjend2:
    #     f.write(str(line)+":")
    # for line in jarjend3:
    #     f.write(str(line)+":")
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