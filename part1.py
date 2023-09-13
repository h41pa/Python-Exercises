"""
1)
În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.

O variaba este locatie din memorie care tine o valoare si are un nume
"""
"""
2)
Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă:
string
int 
float
bool

"""
# mystring = 'sir de caractere'
# myint = 13
# myfloat = 1.5
# mybool = True

"""
3)
Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.

"""
# print(type(mystring))
# print(type(myint))
# print(type(myfloat))
# print(type(mybool))

"""
4)
Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
Verifică tipul acesteia.

"""
# myfloat = round(myfloat)
# print(type(myfloat))
# print(myfloat)

"""
5)
Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile. 

"""
# varsta = 18          #int
# inaltime = 1.88      #float
# nume = "Ion"         # string
# e_adolescent = True  #boolean
# job = "Chimist"      # string
#
# print(f"Numele meu este {nume}  am {varsta} ani .")
# print(f"Am inaltimea de {inaltime}")
# print(f"Sunt Adolescent = {e_adolescent}")
# print(f"Jobul meu este de {job}")

"""
6)
Citește de la tastatură:
numele;
prenumele.
    Afișează: 'Numele complet are x caractere'.


"""
# nume = input('Introdu numele : ')
# prenume = input('Introd prenumele: ')
# print(f'{nume + prenume} are {len(nume + prenume)} caractere')

"""
7)
Citește de la tastatură:
lungimea;
lățimea.
   Afișează: 'Aria dreptunghiului este x'.


"""
# lungimea = float(input('Lungimea : '))
# latimea = float(input('Latimea : '))
#
# print(f"Aria dreptunghiului este {lungimea * latimea}")

"""
8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
afișează de câte ori apare cuvântul 'the';

"""
# mystring = 'Coral is either the stupidest animal or the smartest rock'
# print(mystring.count('the'))
"""
Același string:
Afișează de câte ori apare cuvântul 'the';
Printează rezultatul

"""
# mystring = 'Coral is either the stupidest animal or the smartest rock'
# print(f'Cuvantul the apare de {mystring.count("the")}')

"""
10. Același string:
Folosește un assert ca să verifici dacă acest string conține doar numere.


"""
# string = 'Coral is either the stupidest animal or  the smartest rock'
# assert string.isdigit() == False
# print("verificarea cu succes")

# if string.isdigit():
#     print('Da')
# else:
#     print('Nu')

"""
11. Exercițiu:
citește de la tastatură un string de dimensiune impară;
afișează caracterul din mijloc.

"""
# inp_string = input("Introdu un string impar :\n")
# if len(inp_string) % 2 == 0:
#     print('Dimensiunea sirului nu este impara')
# else:
#     print(f'Caracterul din mijloc este : {inp_string[len(inp_string) // 2]}')

"""
12. Folosind o singură linie de cod :
citește un string de la tastatură (ex: 'alabala portocala');
salvează fiecare cuvânt într-o variabilă;
printează ambele variabile pentru verificare.

"""
# string_12 = input("Introduceti un string gen alabala portocala:\n").split()
# print(string_12)
# for i in string_12:
#     print(i)

# # Citirea șirului de la tastatură și salvarea cuvintelor în variabile separate
# var1, var2 = input("Introdu un șir de cuvinte separate prin spațiu: ").split()
#
# # Afișarea ambelor variabile
# print("Variabila 1:", var1)
# print("Variabila 2:", var2)

"""
13. Exercițiu:
citește un string de la tastatură (ex: alabala portocala);
salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.


"""

# mystring = input('Scrie un string : ')
# x = mystring[0]
# y = mystring.replace(x, x.upper())
# print(y)
# print(y[0].replace(y[0], y[0].lower()) + y[1:-1] + y[-1].replace(y[-1], y[-1].lower()))

"""
.Exercițiu:
citește un user de la tastatură;
citește o parolă;
afișează: 'Parola pt user x este ***** și are x caractere';
***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.

eg: parola abc => ***
      parola abcd => ****

"""
# user = input('Introdu Username: ')
# parola = input('Introdu parola: ')
# ind = "*"
# print(f'Parola pentru user este {ind * len(parola)} si are {len(parola)} caractere ')
