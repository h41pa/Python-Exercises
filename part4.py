"""
 Cicluri repetitive

"""

"""
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel'] 

Folosește un for că să iterezi prin toată lista și să afișezi;
‘Mașina mea preferată este x’.
Fă același lucru cu un for each.
Fă același lucru cu un while.

"""

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

#doar for
# for masina in range(len((masini))):
#     print(masini[masina])

#for each
# for masina in masini:
#     print(f'Masina mea preferata este {masina}')

# i = 0
# while i < len(masini):
#     print(f'Masina mea preferata este {masini[i]}')
#     i += 1
"""
2. Aceeași listă:
Folosește un for else
În for
Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul.
În else:
  Printează lista.

"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
#
# for i in range(1,len(masini)-1):
#     masini[i] = masini[i].upper()
# print(masini)

# for i, masina in enumerate(masini):
#     if i == 0 or i == len(masini) - 1:
#         continue  # Sari peste primul și ultimul element
#     masini[i] = masina.upper()  # Converteste masina la majuscule
#
# else:
#     print(masini)

"""
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Iterează prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
   Printează ‘am găsit mașina dorită de dvs’
   Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
   Printează ‘Am găsit mașina X. Mai căutam‘

"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
#
# for car in masini:
#     if car == 'Mercedes':
#         print('AM gasit Masina dumnevoastra')
#         break
#     else:
#         print(f'Am gasit masina {car}. Mai cautam')

"""
Am gasit masina Audi. Mai cautam
Am gasit masina Volvo. Mai cautam
Am gasit masina BMW. Mai cautam
AM gasit Masina dumnevoastra
"""

"""

4. Aceeași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun. 

Dacă mașina e Trabant sau Lăstun:
   Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
Printează S-ar putea să vă placă mașina x.

"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for  masina in masini:
#     if masina in['Trabant','Lăstun']:
#         continue
#     print(f'S-ar putea sa va placa masina {masina}')

"""
5. Modernizează parcul de mașini:

Crează o listă goală, masini_vechi.
Iterează prin mașini.
Când găsesti Lăstun sau Trabant:
Salvează aceste mașini în masini_vechi.
Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
Printează Modele vechi: x.
Modele noi: x.

"""

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# masini_vechi = []

# for i in range(len(masini)):
#     if masini[i] in  ['Lăstun', 'Trabant']:
#         if masini[i] == 'Lăstun' or masini[i] == 'Trabant':
#             masini_vechi.append(masini[i])
#             masini[i] = 'Tesla'
# print(masini_vechi)
# print(masini)

# for i in range(len(masini)):
#     if masini[i] == 'Lăstun' or masini[i] == 'Trabant':
#         masini_vechi.append(masini[i])
#         masini[i] = 'Tesla'
#
#
# print(f'Modele vechi: {masini_vechi}')
# print(f'Modele noi : {masini}')



"""
6. Având dict:
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

Vine un client cu un buget de 15000 euro.

Prezintă doar mașinile care se încadrează în acest buget.
Iterează prin dict.items() și accesează mașina și prețul.
Printează Pentru un buget de sub 15000 euro puteți alege mașină xLastun
Iterează prin listă.

"""
#
# pret_masini = {
#     'Dacia': 6800,
#     'Lăstun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# buget = 15000
#
# for masina, pret in pret_masini.items():
#     if pret <= buget:
#         print(f'Masina {masina} costa {pret} si se incadreaza in buget')

"""
7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterează prin ea.
Afișează de câte ori apare 3 (nu ai voie să folosești count).

"""

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3, 5]
# numara = 0
# for numar in numere:
#     if numar == 3:
#         numara += 1
#
# print(f'3 apare de {numara}')


"""
8. Aceeași listă:
Iterează prin ea
Calculează și afișează suma numerelor (nu ai voie să folosești sum).


"""

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3, 5]
# suma = 0
#
# for nr in numere:
#     suma += nr
# print(f'SUma totala este : {suma}')
# print(sum(numere))

"""
9. Aceeași listă:
Iterează prin ea.
Afișază cel mai mare număr (nu ai voie să folosești max).

"""
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3, 5]
# maxi = numere[0]
#
# for nr in numere:
#     if nr > maxi:
#         maxi = nr
# print(f'Max e {maxi}')

"""
10. Aceeași listă:
Iterează prin ea.
Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
Afișază noua listă.


"""
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3, 5]
# new = []
# for nr in numere:
#     new.append(-abs(nr))
# print(new)
# for i in range(len(numere)):
#     if numere[i] > 0:
#         numere[i] = -numere[i]
# print(numere)

"""
11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere 
Populează corect celelalte liste
Afișează cele 4 liste la final

"""

# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
#
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
#
# for nr in alte_numere:
#     if nr % 2 ==0:
#         numere_pare.append(nr)
#     else:
#         numere_impare.append(nr)
#     if nr > 0:
#         numere_pozitive.append(nr)
#     elif nr < 0:
#         numere_negative.append(nr)
# print(numere_pare)
# print(numere_impare)
# print(numere_pozitive)
# print(numere_negative)

"""

12. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
Te poți inspira vizual de aici.
https://www.youtube.com/watch?v=lyZQPjUT5B4

"""

# numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# for x in range(len(numere)):
#     for y in range(x+1, len(numere)):
#         if numere[y] < numere[x]:
#             numere[x], numere[y] = numere[y], numere[x]
#
# print(numere)
#
# numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere.sort()
# print(numere)


"""

13. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
   User alege un număr
   Programul îi spune:
Nr secret e mai mare
Nr secret e mai mic
Felicitări! Ai ghicit!


"""
# import random
# numar_secret = random.randint(1, 30)
# numar_ghicit = None
# incercari = 0
#
# while numar_ghicit != numar_secret:
#     try:
#         numar_ghicit = int(input('Introdu numarul secret intre 1 si 30: '))
#     except ValueError:
#         print('Nu ai introdus un numar valid')
#         continue
#     incercari += 1
#
#     if numar_ghicit < numar_secret:
#         print('NUmarul secret este mai mare')
#     elif numar_ghicit > numar_secret:
#         print('Numarul secret este nai mic')
#     else:
#         print(f'Felicitari ai ghicit {numar_secret} in {incercari} incercari')


"""

14. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333



"""
# x = int(input('Introdu un numar'))
#
# for i in range(x+1):
#     for j in range(i):
#         print(i, end='')
#     print()
#
# i = 1
# while i <= x:
#     for j in range(i):
#         print(i, end='')
#     print()
#     i += 1
#



""""
15.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)

"""
# tastatura_telefon = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
# for row in tastatura_telefon:
#     for cells in row:
#         print(f' cifra curenta este {cells}')




