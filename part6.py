"""
Se citesc trei valori reale a, b, c. Să se precizeze dacă ele pot fi laturile unui triunghi.

"""
# a = int(input("Introdu a: "))
# b = int(input("Introdu b: "))
# c = int(input("Introdu c: "))
#
# if a + b > c and a + c > b and b + c > a:
#     print("aceste valori pot fi laturile unui triunghi")
# else:
#     print("Aceste valori nu pot forma un triunghi")

"""
4. Maria citește, în medie, Y cărți a câte Z pagini în X zile. 
Știind că o pagină are în medie 300 de cuvinte și că Maria are ca termen limită citirea a B cărți într-o perioadă 
de C zile (fiecare carte având Z+36 pagini), afișați de câte ori mai multe/mai puține cuvinte trebuie să citească 
pe zi pentru a termina cărțile la timp. (Toate variabilele sunt introduse de la tastatură).

Exemplu: Y=5, Z=200, X=10, B=10, C=5. Se afișează: ”Trebuie să citească de 4.72 ori mai multe cuvinte pe zi 
pentru finalizarea la timp a cărților”.

"""
#
# Y = int(input('Cate carti citite?\n'))
# Z = int(input('Cate pagini?\n'))
# X = int(input('Cate zile?\n'))
# B = int(input('Cate carti trebuie citite?\n'))
# C = int(input('Cate zile disponibile?'))
#
# cuvinte_necesare = B * (Z + 36) * 300
# cuvinte_pe_zi = cuvinte_necesare / C
# cuvinte_pe_zi_obisnuite = (Y * Z * X * 300)
# ratio = cuvinte_pe_zi / cuvinte_pe_zi_obisnuite
#
# if cuvinte_pe_zi_obisnuite < cuvinte_pe_zi:
#     print(f"Maria citeste {ratio:.2f} ori mai multe cuvinte pe zi pentru a finaliza la timp cartile.")
# else:
#     print(f'Maria citeste de {1 / ratio:.2f} ori mai putine cuvinte pe zi pentru a finaliza la timp cartile')

"""
Ascude vocalele!. Să se scrie un "translator" care să modifice vocalele în "*" utilizând ciclul while și if.
"""
#
# text = str(input("Introduceti textul pentru a ascunde vocalele: "))
# text_nou = ""
# i = 0
#
# while i < len(text):
#     if text[i] in "aeiouAEIOU":
#         text_nou += "*"
#     else:
#         text_nou += text[i]
#     i += 1
# print(text_nou)

notite = []


def adauga_nota():
    nota = input("Introduceti o nota : ")
    notite.append(nota)
    print("Nota a fost adaugata")

def afiseaza_notite():
    for i, nota in enumerate(notite, start=1):
        print(f'{1}. {nota}')

def sterge_nota():
    afiseaza_notite()
    index = int(input("Selectati nota de sters (introduceti numarul): "))
    if 0 <= index < len(notite):
        nota_stearsa = notite.pop(index)
        print(f"Nota '{nota_stearsa}' a fost stearsa")
    else:
        print("Selectare invalida!")

while True:
    print("\nOpțiuni:")
    print("1. Adaugă notă")
    print("2. Afisează notițele")
    print("3. Șterge notă")
    print("4. Ieșire")

    optiune = input("Introduceți numărul opțiunii: ")

    if optiune == "1":
        adauga_nota()
    elif optiune == "2":
        afiseaza_notite()
    elif optiune == "3":
        sterge_nota()
    elif optiune == "4":
        print("La revedere")
        break
    else:
        print("optiune invalida")