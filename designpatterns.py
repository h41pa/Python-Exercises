"""
####### Singleton
Se da următoarea clasa:
class PresedinteRomania:

    def __str__(self):
        return "Eu sunt presedintele Romaniei"

    def say_hello(self):
        return f'Salut! {self}'

In momentul de fata, dacă încercăm să creăm mai multe obiecte din clasa aceasta, vom putea:

a = PresedinteRomania()
b = PresedinteRomania()

print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Acelasi obiect? {a is b}')

Scopul acestui exercițiu este sa modificăm clasa de mai sus folosind DP Singleton pentru a obține mereu același obiect:
Vom folosi functia `__new__` (adevăratul constructor din Python)
Vom tine singurul obiect pe clasa (cls), și îl vom crea doar la prima apelare a lui __new__
La orice alta apelare, vom returna obiectul deja existent
"""

# class PresedinteRomania:
#     __instance = None
#
#     def __init__(self, name):
#         self.name = name
#
#     def __new__(cls, *args):
#         if cls.__instance is None:
#             cls.__instance = object.__new__(cls)
#         return cls.__instance
#
#
#     def __str__(self):
#         return "Eu sunt presedintele Romaniei"
#
#     def say_hello(self):
#         return f'Salut! {self}'
#
# a = PresedinteRomania('Gicu')
# b = PresedinteRomania('Andrei')
# print(f'ID(a) = {id(a)}')
# print(f'ID(b) = {id(b)}')
# print(f'Acelasi obiect? {a is b}')
# b.new = "Dumitru"
# print(b.new)

"""
### Factory Pattern
Acest pattern ne permite sa creăm un obiect dintr-o clasa folosind o alta clasa (fabrica).
Fabrica are posibilitatea de a crea obiecte din mai multe clase (de obicei aceste clase sunt siblings,
adica mostenesc de la acelasi parinte).
	
Vom implementa următoarele clase:
English/French/Spanish Translator – clase care știu sa traduca cuvinte din română în limba specificata
translations va fi un dicționar cu acele cuvinte, exemplu `{ “masina”: “car” }` – se poate hardcoda în clasa
localize va fi o funcție care pentru un parametru de intrare,
ne va da traducerea lui în acea limba (exemplu `input(“masina”)` returneaza “car”)

TranslatorFactory – clasa care are o singura metoda (preferabil statica sau de clasa)
numita get_translator(language) – in functie de parametrul language, returnează un translator object.

factory = TranslatorFactory()

english_trans = factory.get_translator('en')
spanish_trans = factory.get_translator('es')

print(f'In engleza zicem {english_trans.localize("masina")}')
print(f'In spaniola zicem {spanish_trans.localize("masina")}')

"""
# class EnglishTranslator:
#     translations = {"masina": "car", "culoare": "color", "apa": "water"}
#
#     def localize(self, word):
#         if word in self.translations:
#             print(f"Traducerea pentru {word} in engleza este {self.translations[word]}")
#         else:
#             print(f"Traducerea lipseste din dictionar")
#
# class FrenchTranslator:
#     translations = {"masina": "voiture", "culoare": "couleur", "apa": "eau"}
#
#     def localize(self, word):
#         if word in self.translations:
#             print(f"Traducerea pentru {word} in franceza este {self.translations[word]}")
#         else:
#             print(f"Traducerea lipseste din dictionar")
#
#
# class SpanishTranslator:
#     translations = {"masina": "coche", "culoare": "color", "apa": "agua"}
#
#     def localize(self, word):
#         if word in self.translations:
#             print(f"Traducerea pentru {word} in spaniola este {self.translations[word]}")
#         else:
#             print(f"Traducerea lipseste din dictionar")
#
#
# class TranslatorFactory:
#     def get_language(self, language):
#         if language == 'en':
#             return EnglishTranslator()
#
#         elif language == 'fr':
#             return FrenchTranslator()
#         elif language == 'es':
#             return SpanishTranslator
#         else:
#             return  ValueError(f'limba nu exista {language}')
#
# factory = TranslatorFactory()
# # english_trans = factory.get_language('en')
# # english_trans.localize('masina')
# # french_trans = factory.get_language('fr')
# # french_trans.localize('masina')

#    ``` alta modalitate cu clasa abstracta

# from abc import ABC
#
# class AbstractTranslator(ABC):
#
#     def localize(self, text):
#         return NotImplementedError
#
#
# class EnglishTranslator(AbstractTranslator):
#
#     def __init__(self):
#         self.translations = {
#             'masina': 'car',
#             'om': 'human',
#             'curs': 'course',
#             'salut!': 'hello!'
#         }
#
#     def localize(self, text):
#         if text in self.translations:
#             return self.translations[text]
#         print('Traducerea nu exista')
#
# class SpanishTranslator(AbstractTranslator):
#
#     def __init__(self):
#         self.translations = {
#             'masina': 'coche',
#             'om': 'hombre',
#             'curs': 'clase',
#             'salut!': 'hola!'
#         }
#
#
#     def localize(self, text):
#         if text in self.translations:
#             return self.translations[text]
#         print('Traducerea nu exista...')
#
# class FrenchTranslator(AbstractTranslator):
#     def __init__(self):
#         self.translations = {
#             'masina': 'voiture',
#             'om': 'homme',
#             'curs': 'course',
#             'salut!': 'bonjour!'
#         }
#     def localize(self, text):
#         if text in self.translations:
#             return self.translations[text]
#
#         print('Traducerea nu exista...')
#
#
# class TranslatorFactory:
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def get_translator(language):
#         if language == 'en':
#             return EnglishTranslator()
#         elif language == 'fr':
#             return FrenchTranslator()
#         elif language == 'es':
#             return SpanishTranslator()
#         else:
#             return ValueError(f'limba nu exista {language}')
#
#
# translators = []
# translators.append((TranslatorFactory.get_translator('en')))
# translators.append((TranslatorFactory.get_translator('fr')))
# translators.append((TranslatorFactory.get_translator('es')))
#
# for t in translators:
#     print(t.localize('masina'))