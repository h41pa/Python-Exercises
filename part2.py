"""
Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.


"""
"""
1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.

if - daca ne ajuta sa  sa aratam daca o conditie este adevarata
else - functioneaza doar cu if  si este blocul care se executa cand conditia este falsa
"""

"""
2. Verifică și afișează dacă x este număr natural sau nu.
"""

# x = float(input('Introdu Numarul :'))
# if x < 0:
#     print('Numar Negativ')
# else:
#     print('Numar Natural')

"""
3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
"""
# x = float(input('Introdu numar'))
#
# if x > 0:
#     print(f'{x} este numar pozitiv')
#
# if x < 0:
#     print(f'{x} este numar -')
# if x == 0:
#     print(f'{x} este numar 0')

"""
4. Verifică și afișează dacă x este între -2 și 13.
"""
# x = int(input('Introdu x : '))

# if x in range(-2, 13):
#     print(f'{x} se afla intre -2 si 13')
# else:
#     print(f'{x} nu se afla in intervalul -2 si 13')

# if x >= 2 and x <= 13 :
#     print(f'{x} se afla intre -2 si 13')
# else:
#     print(f'{x} nu se afla in intervalul -2 si 13')

"""
Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
"""

# x = float(input('Introdu valoarea pentru x :'))
# y = float(input('Introdu valoarea pentru y :'))
#
# if x - y < 5:
#     print(f'Diferenta dintre {x} si {y} este mai mica de 5.')
# else:
#     print(f'Diferenta dintre {x} si {y} NU este mai mica de 5.')

"""
6. Verifică dacă x NU este între 5 și 27  - a se folosi ‘not’.
"""

# x = int(input('Introdu x'))
#
# if not  5 < x < 25:
#     print(f'{x}  nu se afla intre 5-27')
# else:
#     print(f'{x} se  afla intre 5 si 27')

"""
7.
x și y (int)
Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.

"""
# x = int(input('Introdu valoarea pentru x :'))
# y = int(input('Introdu valoarea pentru y :'))

# if x == y:
#     print(f'{x} si {y} sun egale')
# elif x > y:
#     print(f'{x} este mai mare')
# else:
#     print(f'{y} este mai mare')

# if x > y:
#     print(f'{x} este mai mare')
# elif y > x:
#     print(f'{y} este mai mare')
# else:
#     print(f'{x} si {y} sun egale')

"""
X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.


"""
#
# x = int(input('Introdu valoarea pentru x :'))
# y = int(input('Introdu valoarea pentru y :'))
# z = int(input('Introdu valoarea pentru z :'))
#
# if x == y == z:
#     print('Triughiul este echilater')
# elif x == y or x == z or y == z:
#     print('Triughiul este isoscel')
# else:
#     print('Triunghiul este oarecare')

"""
Citește o literă de la tastatură.
    Verifică și afișează dacă este vocală sau nu.

"""
#
# litera = input("Introdu o literă: ")
#
# if litera in ['a', 'e', 'i', 'o', 'u']:
#     print(f"{litera} este o vocală.")
# else:
#     print(f"{litera} nu este o vocală.")

"""
10.Transformă și printează notele din sistem românesc în  >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F


"""

# grade = float(input("Introdu nota:\n"))
# american_grade = ""
#
# if grade > 10 or grade <= 0:
#     print("Ai introdus o valoare gresita!")
# else:
#     if grade <= 4:
#         american_grade = "F"
#     elif grade < 6:
#         american_grade = "E"
#     elif grade < 7:
#         american_grade = "D"
#     elif grade < 8:
#         american_grade = "C"
#     elif grade < 9:
#         american_grade = "B"
#     else:
#         american_grade = "A"
#     # afisam mesajul doar daca nota introdusa a fost corecta!
#     print(f"Felicitari, ai luat nota {american_grade}")

"""
Un mic exercitiu folosind enumarate
"""

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
#
# for index, cars in enumerate(masini, start=1):
#     print(f'{index} : {cars}')

"""
11.Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

"""

# x = input("Introdu x :")
# y = int(len(x))
# print(y)

# if int(len(x)) < 4:
#     print(f'{x} nu are minim 4 cifre')
# else:
#     print(f'{x} are 4 cifre !')
#
# if x >= 1000 or x <= -1000:
#     print(f"{x} are cel puțin 4 cifre.")
# else:
#     print(f"{x} nu are cel puțin 4 cifre.")

"""
12.Verifică dacă x are exact 6 cifre.

"""
# x = input("Introdu x :")
# if int(len(x)) == 4:
#     print(f'{x} are 4 cifre !')
# elif int(len(x)) == 6:
#     print(f'{x} are 6 cifre !')
# else:
#     print(f'{x} u are nici 4 si nici 6 cifre')

"""
13.Verifică dacă x este număr par sau impar (x e int).
"""
# x = int(input("Introdu x :"))
# if x % 2 == 0:
#     print(f'{x} este numar par')
# else:
#     print(f'{x} este numar impar')

# x = (input("Introdu x :"))
# if not x.isdigit():
#     print('Introdu doar cifre, ai introduse alte caractere')
# else:
#     if int(x) % 2 == 0:
#         print(f'{x} este numar par')
#     else:
#         print(f'{x} este numar impar')


"""
14.      x, y, z (int)
Afișează care este cel mai mare dintre ele?

"""
# x = int(input('Introdu valoarea pentru x :'))
# y = int(input('Introdu valoarea pentru y :'))
# z = int(input('Introdu valoarea pentru z :'))



# if x > y:
#     print(f'x {x} este mai mare')
# elif x > z:
#     print(f'X {x} este mai mare')
# elif  y > z:
#     print(f'Y {y} este mai mare')
# else:
#     print(f'Z {z} este mai mare')

# if x >= y and x >= z:
#     print(f'X: {x} este mai mare')
# elif y >= x and y >= z:
#     print(f'Y: {y} este mai mare')
# else:
#     print(f'Z: {z} este mai mare')

# if x >= y:
#     if x >= z:
#         print(f'X: {x} este mai mare')
#     else:
#         print(f'Z: {z} este mai mare')
# else:
#     if y >= z:
#         print(f'Y: {y} este mai mare')
#     else:
#         print(f'Z: {z} este mai mare')


"""
15. 
X, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu.

"""

# x = float(input('Introdu valoarea pentru x :'))
# y = float(input('Introdu valoarea pentru y :'))
# z = float(input('Introdu valoarea pentru z :'))
#
# if x + y + z == 180:
#     print('Triunghiul este valid')
# else:
#     print('Triunghul este invalid')

"""
16. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
Citește de la tastatură un int x
Afișează stringul fără ultimele x caractere
Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'

"""

# mystring = 'Coral is either the stupidest animal or the smartest rock'
#
# x = int(input('Introdu x :'))
# print(mystring[:-(x)])

"""
17. Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5.
"""

# mystring = 'Coral is either the stupidest animal or the smartest rock'
# mynewstring = mystring[0:5] + mystring[-5:]
# print(mynewstring)

"""
18. Același string. 
Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
output: 'Coral is either the stupidest animal or the smartest' 


"""
# mystring = 'Coral is either the stupidest animal or the smartest rock'
# start_index = mystring.find('rock')
# print(mystring[:start_index])

"""
20.  Citește de la tastatură un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat
"""
# x = input('Introdu text :').lower()
# assert x[0] == x[-1], "Primul si ultimul nu sunt la fel"
# print('Primul si ultimul sunt la fel')

"""
21. Având stringul '0123456789'
Afișează doar numerele pare 
Afișează doar numerele impare
(hint: folosește slicing, controlează din pas)

"""

# mystring = '0123456789'
# print(f'Numere Pare : {mystring[::2]}')
# print(f'Numere impare : {mystring[1::2]}')