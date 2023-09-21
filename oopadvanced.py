"""
OOP - advance
"""
"""
ABSTRACTION 
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’

"""

# from abc import ABC, abstractmethod
#
#
# class FormaGeometrica(ABC):
#     PI = 3.14
#
#     @abstractmethod
#     def aria(self):
#        return NotImplementedError

    # @abstractmethod    # obligatoriu de implementant
    # def descrie(self):
    #     print("Cel mai probabil am colțuri")

    # @classmethod  # se poate apela din subclase cls face referire la clasa.
    # def describe(cls):
    #     print("Cel mai probabil am colțuri")

"""
INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură

"""


# class Patrat(FormaGeometrica):
#     def __init__(self, latura):
#         self.latura = latura

"""
ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)


"""
# from abc import ABC, abstractmethod
#
#
# class FormaGeometrica(ABC):
#     PI = 3.14
#
#     @abstractmethod
#     def aria(self):
#        return NotImplementedError
#
#
#     @classmethod  # se poate apela din subclase cls face referire la clasa.
#     def describe(cls):
#         print("Cel mai probabil am colțuri")
#
#
# class Patrat(FormaGeometrica):
#     def __init__(self, latura):
#         self.__latura = latura
#
#
#     @property
#     def latura(self):
#         return self.__latura
#
#     @latura.setter
#     def latura(self, noua_latura):
#         self.__latura = noua_latura
#
#     @latura.deleter
#     def latura(self):
#         print("Ștergerea laturii nu este permisă.")
#
#     def aria(self):
#         return self.__latura * 2
#
# patrat = Patrat(5)
# print(patrat.latura)
# print(patrat.aria())

"""
Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI mostenit din clasa părinte (opțional,
doar dacă ai ales să implementezi metoda abstractă aria)


"""
#
# from abc import ABC, abstractmethod
#
#
# class FormaGeometrica(ABC):
#     PI = 3.14
#
#     @abstractmethod
#     def aria(self):
#        return NotImplementedError
#
#
#     @classmethod
#     def describe(cls):
#         print("Cel mai probabil am colțuri")
#
#
#
# class Cerc(FormaGeometrica):
#     def __init__(self, raza):
#         self.__raza = raza
#
#     @property
#     def raza(self):
#         return self.__raza
#     @raza.setter
#     def raza(self, noua_raza):
#         self.__raza =  noua_raza
#     @raza.deleter
#     def raza(self):
#         print('Nu poti sterge raza')
#
#     def aria(self):
#         return self.PI * (self.raza ** 2)
#
# cerc1 = Cerc(4)
# print(f'Raza cercului este de {cerc1.raza}')
# print(f'Aria Cercului este {cerc1.aria()}')
# cerc1.raza = 7
# print(f'Noua raza cercului este de {cerc1.raza}')
# print(f'Noua arie a cercului este {cerc1.aria()}')

"""
POLYMORPHISM 
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’

Creează un obiect de tip Pătrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui


"""

# from abc import ABC, abstractmethod
#
#
# class FormaGeometrica(ABC):
#     PI = 3.14
#
#     @abstractmethod
#     def aria(self):
#        return NotImplementedError
#
#
#     @classmethod
#     def describe(cls):
#         print("Cel mai probabil am colțuri")
#
#
# class Cerc(FormaGeometrica):
#     def __init__(self, raza):
#         self.raza = raza
#
#
#
#     def aria(self):
#         return self.PI * (self.raza ** 2)
#
#     def describe(cls):
#         print('Eu nu am colturi')
#
# class Patrat(FormaGeometrica):
#     def __init__(self, latura):
#         self.atura = latura
#
#
#
#     def aria(self):
#         return self.__latura * 2

# metoda describe are acelasi nume dar comportament diferit