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
# import datetime
# class Factura:
#     SERIE = 'A0001'
#
#     def __init__(self, numar: object, nume_produs: object, cantitate: object, pret_buc: object) -> object:
#         self.numar = numar
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_buc = pret_buc
#
#     def schimba_cantitate(self, cantitate):
#         self.cantitate = cantitate
#     def schimba_pretul(self, pret):
#         self.pret_buc = pret
#     def schimba_nume_produs(self, nume):
#         self.nume_produs = nume
#
#     def genereaza_factura(self):
#         total =  self.cantitate * self.pret_buc
#         date_now = datetime.date.today()
#         print(f'Factura seria {self.SERIE} numar {self.numar}\n Data: {date_now}')
#         print(f'Produs\t|Cantitate\t|Pret Bucata\t|Total')
#         print(f'{self.nume_produs}\t|{self.cantitate}\t|{self.pret_buc}\t|{total}')
#
# telefon = Factura('12','Telefon', 2, 500)
# telefon.schimba_cantitate(4)
# telefon.schimba_pretul(800)
# telefon.genereaza_factura()
from datetime import datetime

# print(datetime.today())


class Factura:
    serie = 'A0001'

    def __init__(self, numar):
        self.numar = numar
        self.date = None
        self.total_produs = None
        self.pret_buc = None
        self.cantitate = None
        self.lista_produse = {}
        self.nume_produs = None
        self.total_plata = None

    def adauga_produs(self, nume_produs, cantitate, pret_buc):
        self.lista_produse[nume_produs] = list()
        self.lista_produse[nume_produs].append(cantitate)
        self.lista_produse[nume_produs].append(pret_buc)
        self.lista_produse[nume_produs].append(self.get_total_produs(nume_produs))

    def get_total_produs(self, nume_produs):
        return self.lista_produse[nume_produs][0] * self.lista_produse[nume_produs][1]

    def schimba_cantitatea(self, nume_produs, cantitate):
        self.lista_produse[nume_produs][0] = cantitate
        self.lista_produse[nume_produs][2] = self.get_total_produs(nume_produs)

    def schimba_pretul(self, nume_produs, pret):
        self.lista_produse[nume_produs][1] = pret
        self.lista_produse[nume_produs][2] = self.get_total_produs(nume_produs)

    def sterge_produsul(self, nume_produs):
        del self.lista_produse[nume_produs]

    def schimba_numele_produsului(self, nume_produs, nume_nou):
        self.lista_produse[nume_nou] = self.lista_produse[nume_produs]
        self.sterge_produsul(nume_produs)

    def get_date(self):
        self.date = datetime.today()
        return self.date

    def genereaza_factura(self):
        self.total_plata = 0
        print(f"Factura seria {self.serie} numar {self.numar}")
        print(f"Data: {self.get_date()}")
        col1, col2, col3, col4 = "Produs", 'Cantitate', 'Pret bucata', 'Total produs'
        col_size = 20

        print(f"{col1:^{col_size}}|{col2:^{col_size}}|{col3:^{col_size}}|{col4:^{col_size}}|")
        for produs in self.lista_produse.keys():
            print(f"{str(produs):^{col_size}}", end="|")
            for coloana in self.lista_produse[produs]:
                print(f"{str(coloana):^{col_size}}", end="|")
            print()
        for produs in self.lista_produse.keys():
            self.total_plata += self.lista_produse[produs][2]
        print('-' * 4 * col_size)
        print(f"Total de plata: {self.total_plata}")
        print('-' * 4 * col_size)


f1 = Factura(1)
f1.adauga_produs('Telefon', 7, 700)
f1.adauga_produs('TV', 1, 2000)
f1.adauga_produs('Frigider', 2, 1500)
f1.genereaza_factura()
f1.schimba_cantitatea('TV', 5)
f1.genereaza_factura()
f1.schimba_pretul('Telefon', 1000)
f1.genereaza_factura()
f1.schimba_numele_produsului('Telefon', 'Congelator')
f1.genereaza_factura()
f1.sterge_produsul('TV')
f1.genereaza_factura()