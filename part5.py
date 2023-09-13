"""
Partea 1- Funcții

Pentru toate exercițiile. Apelați funcția de cel puțin 2 ori cu valori diferite pentru a testa.
Dacă funcția are return, printează răspunsul.
"""

"""
1.Funcție care să calculeze și să returneze suma a două numere
"""

# def suma(a, b):
#     return a + b
#
# a = 4
# b = 8
# print(suma(a, b))
# print(suma(2, 4))

"""
2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar

"""
# def is_even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
#
# print(is_even(88)

"""
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu) 

"""

# def nr_char(nume, prenume, nume_mijlociu):
#     return len(nume + prenume + nume_mijlociu)
#
# print(nr_char('Chelu','Ion','Madalin'))

"""
4. Funcție care returnează aria dreptunghiului

"""
# def get_aria(lungime, latime):
#     return f'Aria Dreptiunghiului cu lungimea = {lungime} si latime = {latime} este = {lungime * latime}'
#
# print(get_aria(6, 8))

"""
5. Funcție care returnează aria cercului
"""

# def get_circle_area(r):
#     PI = 3.14159
#     return f'Aria cercului cu raza {r} este : {PI* (r**2)}'
#
# print(get_circle_area(12))

"""
6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.
"""

# def get_char(caracter, text):
#     if caracter in text:
#         return True
#     return False
# print(get_char('s', 'Am sapte copi'))
# def get_char(caracter, text):
#     return caracter in text
# print(get_char('s', 'Am sapte copi'))

"""
7. Funcție fără return, primește un string și printează pe ecran:
Numărul de caractere lower case este x
Numărul de caractere upper case exte y 

"""
# def print_strings(text):
#     numar_lower = 0
#     numar_upper = 0
#     for caracter in text:
#         if caracter.islower():
#             numar_lower += 1
#         elif caracter.isupper():
#             numar_upper += 1
#     print(f"Numărul de caractere lower case este {numar_lower}")
#     print(f"Numărul de caractere upper case este {numar_upper}")
#
# print_strings('Ana Are Mere')

"""

8. Funcție care primește o LISTĂ de numere și returnează o LISTĂ doar cu numerele pozitive.

"""

# def return_positive(lista):
#     new_list = []
#     for x in lista:
#         if x > 0:
#             new_list.append(x)
#
#     return (new_list)
#
#
# return_positive([2, 4, 6, -5, -3, -2, 8])
#
# print(return_positive([2, 4, 6, -5, -3, -2, 8]))

"""
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ
Primul număr x este mai mare decat al doilea număr y
Al doilea număr y este mai mare decat primul număr x
Numerele sunt egale. 

"""
# def compare(x, y):
#     if x > y:
#         print(f'Primul număr {x} este mai mare decat al doilea număr {y}')
#     elif y > x:
#         print(f'Al doilea număr {y} este mai mare decat primul număr {x}')
#     else:
#         print('Sunt egale')
#
# compare(4, 5)

"""
10. Funcție care primește un număr și un set de numere.
Printează ‘am adaugat numărul nou în set’ + returnează True
Printează ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False


"""

# def compare2(nr, setnr):
#     if nr not  in setnr:
#         setnr.add(nr)
#         print(f'am adaugat numărul {nr} în set')
#         return True
#     else:
#         print(f'nu am adaugat {nr} în set. Acesta există deja')
#         return False
#
# setrandom = {0, 1, 3, 2, 5, 4}
# print(setrandom)
# compare2(3, setrandom)
# compare2(6, setrandom)
# print(setrandom)
#
# print(type(setrandom))

"""
11. Funcție care primește o lună din an și returnează câte zile are acea lună.

"""
# def get_days_of_month(year, month):
#     if month == 2 and year % 4 == 0:
#         print('Number of days is 29')
#     elif month == 2:
#         print('Number of days is 28')
#     elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
#         print('Number of days is 31')
#     else:
#         print('Number of day 30')
#
# get_days_of_month(2023, 9)

# def zile_in_luna(luna):
#     luni = {
#         "ianuarie": 31,
#         "februarie": 28,  # 29 în an bisect
#         "martie": 31,
#         "aprilie": 30,
#         "mai": 31,
#         "iunie": 30,
#         "iulie": 31,
#         "august": 31,
#         "septembrie": 30,
#         "octombrie": 31,
#         "noiembrie": 30,
#         "decembrie": 31
#     }
#     luna = luna.lower()
#
#     if luna in luni:
#         print(f'{luna} are {luni[luna]} zile')
#     else:
#         return None
#
#
# zile_in_luna('ApriLie')

"""
12. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.

În final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)


"""

# def returns(x, y):
#     suma = x + y
#     diferenta = x - y
#     inmultire = x * y
#     impartire = x /y
#     return suma, diferenta, inmultire, impartire
#
# a, b, c, d = returns(10, 2)
# print('Suma', a)
# print('Diferenta', b)
# print('Inmultire', c)
# print('Impartire', d)

"""
13. Funcție care primește o listă de cifre (adică doar 0-9) 
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3:  1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}

"""


# def return_dict(*args):
#     d = {}
#     for i in args:
#         d[i] = args.count(i)
#     return d
#
# print(return_dict(1, 3, 1, 5, 9, 7, 7, 5, 5))

# def return_dict2(*args):
#     d = {
#         0: 0,
#         1: 0,
#         2: 0,
#         3: 0,
#         4: 0,
#         5: 0,
#         6: 0,
#         7: 0,
#         8: 0,
#         9: 0
#     }
#     for i in args:
#         if i in d:
#             d[i] += 1
#         return d
#
# print(return_dict2(1, 3, 1, 5, 9, 7, 7, 5, 5))
#
# def numara_cifre(lista_cifre):
#     rezultat = {}
#     for cifra in lista_cifre:
#         if cifra in rezultat:
#             rezultat[cifra] += 1
#         else:
#             rezultat[cifra] = 1
#     for cifra in range(10):
#         if cifra not in rezultat:
#             rezultat[cifra] = 0
#     return rezultat
# lista_cifre = [1, 3, 1, 5, 9, 7, 7, 5, 5]
# rezultat = numara_cifre(lista_cifre)
# print(rezultat)

"""

14. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele.

"""

# def maxim(x, y ,z):
#     return max(x, y, z)
#
# print(max(3, 5, 8))

"""
15. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr.
Exemplu: dacă dăm numărul 3, suma va fi 6 (0+1+2+3)

"""

# def suma_pana_la_nr(numar):
#     suma = 0
#     for i in range(numar + 1):
#         suma += i
#     return suma
#
# print(suma_pana_la_nr(3))

"""
16.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.



"""
# def numere_comune(list1, list2):
#     set1 = set(list1)
#     set2 = set(list2)
#     return set1.intersection(set2)
#
#
#
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# print(numere_comune(list1, list2))
# print(numere_comune([1, 1, 2, 3], [2, 2, 3, 4]))

"""

17. Funcție care să aplice o reducere de preț.
Dacă produsul costă 100 lei și aplicăm reducere de 10%. Pretul va fi 90 de lei.
Tratează cazurile în care reducerea e invalidă. De exemplu o reducere de 110% e invalidă.

"""

# def discount(pret_initial, pret_redus):
#     if pret_initial < 0 or pret_redus > 100:
#         raise ValueError ("Reducere invalida! Pretul initial trebuie sa fie > 0 si procentul reducerii < 100!")
#     return pret_initial - pret_redus/100 * pret_initial
# print(discount(100 , 110))

"""

 18.Funcție care să afișeze data și ora curentă din România.
(bonus: afișazăi și data și ora curentă din China)

"""

from datetime import datetime
import pytz
# def ora_curenta_in_romania():
#     tz_bucharest = pytz.timezone('Europe/Bucharest') # Această linie creează un obiect timezone reprezentând fusul orar al Bucureștiului (care este fusul orar al întregii Românii)
#     datetime_bucharest = datetime.now(tz_bucharest) # Această linie obține data și ora curentă, conform fusului orar pe care tocmai l-am definit
#     return datetime_bucharest # Aici, funcția returnează data și ora curentă din București
#
# print(ora_curenta_in_romania()) #Această linie apelează funcția ora_curenta_inromania și afișează rezultatul său.

# def ora_curenta():
#     # tz_bucharest = pytz.timezone('Europe/Bucharest')
#     datetime_bucharest = datetime.now(pytz.timezone('Europe/Bucharest'))
#     return datetime_bucharest
#
# print(ora_curenta())

# def ora_curenta():
#     # tz_bucharest = pytz.timezone('Europe/Bucharest')
#     datetime_bucharest = datetime.now(pytz.timezone('Europe/Bucharest'))
#     print(f'Ora in Bucuresti : {datetime_bucharest}')
#     datetime_china = datetime.now(pytz.timezone('Asia/Shanghai'))
#     print(f'Ora in China : {datetime_china}')
#
# ora_curenta()

""""
19. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la Crăciun dacă nu vrei să ne zici cand e ziua ta :)


"""
