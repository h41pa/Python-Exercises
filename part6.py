"""
OOP _ Clase & Obiecte
"""

"""
1.Clasa Cerc
    Atribute: rază, culoare
    Constructor pentru ambele atribute
    Metode:
descrie_cerc() - va PRINTA culoarea și raza
aria() - va RETURNA aria 
diametru() 
circumferinta()

"""
# from math import pi
#
# class Cerc:
#     PI = pi
#     def __init__(self, raza, culoare):
#         self.raza = raza
#         self.culoare = culoare
#
#     def descrie_cerc(self):
#         print(f'Cercul meu are raza de {self.raza} si este culoarea {self.culoare}')
#
#     def aria(self):
#         return pi * (self.raza **2)
#     def diametru(self):
#         return 2 * self.raza
#     def circumferinta(self):
#         return 2 * pi * self.raza
#
#
#
# c = Cerc(4,'rosu')
# c.descrie_cerc()
# print(c.aria())
# print(c.diametru())
# print(c.circumferinta())

"""
2. Clasa Dreptunghi
     Atribute: lungime, lățime, culoare
     Constructor pentru toate atributele
     Metode:
descrie()
aria()
perimetrul()
schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic. Ea va lua ca și parametru o nouă culoare
și va suprascrie atributul self.culoare. Poți verifica schimbarea culorii prin apelarea metodei descrie().

"""

# class Dreptunghi:
#     def __init__(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#     def descrie(self):
#         print(f' SUnt un dreptunghi am lungime = {self.lungime} , latimea = {self.latime} si culoarea {self.culoare}')
#
#     def aria(self):
#         return self.lungime * self.latime
#
#     def perimetrul(self):
#         return 2 * (self.lungime + self.latime)
#
#     def schimbă_culoarea(self, noua_culoare):
#         self.culoare = noua_culoare
#         # return self.culoare


#
# d1 = Dreptunghi(4, 6, 'Rosu')
# d1.descrie()
# print(d1.aria())
# print(d1.perimetrul())
# d1.schimbă_culoarea('ALbastru')
# d1.descrie()

