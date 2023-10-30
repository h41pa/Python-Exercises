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