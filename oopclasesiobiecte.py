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

"""
3. Clasa Angajat
     Atribute: nume, prenume, salariu
     Constructor pentru toate atributele
     Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)


"""
# class Angajat:
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#     def descrie(self):
#         return f'Angajatul {self.nume} {self.prenume} are salariul {self.salariu}'
#
#     def nume_complet(self):
#         return f' Numele complet este : {self.nume}{self.prenume}'
#
#     def salariu_lunar(self):
#         return f'Salariul lunar al angajatului {self.nume} este de {self.salariu}'
#     def salariu_anual(self):
#         return f'Angajatul {self.nume} {self.prenume} are salariul anual de {self.salariu * 12}'
#
#     def marire_salariu(self, procent):
#         if procent < 0:
#            return f' Salariul tau s-a miscorat , noul salariu este {self.salariu * (1 + procent/100)} '
#
#         elif procent == 0:
#             return 'Salariul a ramas acelasi'
#
#         else:
#             return f'Dupa marirea de {procent}% noul tau salariu este {self.salariu *(1 + procent/100)}'
#
# angajat1 = Angajat('Madalin', 'Chelu', 4000)
# print(angajat1.descrie())
# print(angajat1.nume_complet())
# print(angajat1.salariu_lunar())
# print(angajat1.salariu_anual())
# print(angajat1.marire_salariu(-20))
# print(angajat1.marire_salariu(0))
# print(angajat1.marire_salariu(20))
#
#
"""
4. Clasa Cont
   Atribute: iban, titular_cont, sold
   Constructor pentru toate atributele
   Metode:
afisare_sold() - Titularul x are în contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)

"""
#
# class Cont:
#     def __init__(self, iban, titular_cont, sold):
#         self.iban = iban
#         self.titular_cont = titular_cont
#         self.sold =sold
#
#     def afisare_sold(self):
#         print(f'Titularul {self.titular_cont} are în contul {self.iban} suma de {self.sold} lei')
#
#     def debitare_cont(self, *suma):
#         print("Tranzactia va fi comisionata")
#         suma = int(input('Introdu suma pe care vrei o retragi'))
#         if suma > self.sold:
#             print('Fonduri insuficiente')
#         else:
#             self.sold = self.sold - suma
#             print(f'Ai retras {suma} lei')
#             return self.sold
#
#     def creditare_cont(self, suma):
#         self.sold = self.sold + suma
#         print(f'Ati adaugat {suma} in contul curent')
#         return self.sold
#
# cont1 = Cont('1234', 'Madalin Chelu', 15000)
# cont1.afisare_sold()
# cont1.debitare_cont()
# cont1.creditare_cont(400)
# cont1.afisare_sold()

"""
5. Clasa Factură
     Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor avea aceeași serie), număr, nume_produs, cantitate, pret_buc
     Constructor: toate atributele, fără serie
     Metode:
schimbă_cantitatea(cantitate)
schimbă_prețul(pret)
schimbă_nume_produs(nume)
generează_factura() - va printa tabelar dacă reușiți

"""
#
# from datetime import date
#
# class Factura:
#     # Atribut constant pentru serie
#     serie = "x"
#
#     # Constructor
#     def __init__(self, numar, nume_produs, cantitate, pret_buc):
#         self.numar = numar
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_buc = pret_buc
#         self.data = date.today()
#
#     # Metoda pentru a schimba cantitatea
#     def schimba_cantitatea(self, cantitate):
#         self.cantitate = cantitate
#
#     # Metoda pentru a schimba prețul
#     def schimba_pretul(self, pret):
#         self.pret_buc = pret
#
#     # Metoda pentru a schimba numele produsului
#     def schimba_nume_produs(self, nume):
#         self.nume_produs = nume
#
#     # Metoda pentru a genera factura
#     def genereaza_factura(self):
#         total = self.cantitate * self.pret_buc
#         print(f"Factura seria {self.serie} număr {self.numar}")
#         print(f"Data: {self.data.strftime('%d/%m/%Y')}")
#         print("Produs | Cantitate | Preț bucată | Total")
#         print(f"{self.nume_produs} | {self.cantitate} | {self.pret_buc} | {total}")
#
# # Exemplu de utilizare
# factura1 = Factura(1, "Telefon", 7, 700)
# factura1.genereaza_factura()
# factura1.schimba_cantitatea(10)
# factura1.schimba_pretul(750)
# factura1.schimba_nume_produs("Telefon Samsung")
# factura1.genereaza_factura()
#
#


