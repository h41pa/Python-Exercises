"""
Decorators
Implementați următorii decoratori:
-	timeit – decorator care măsoară timpul de execuție al unei funcții
-	logger – decorator care printeaza argumentele de intrare, și rezultatul unei funcții

"""

# import time
#
# def timeit(func):
#     def inner_func(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f'Functia {func.__name__} a rulata in {execution_time:.4f} secunde') # :4f numarul de zecimale.
#
#         return result
#
#     return inner_func
# @timeit
# def exemplu():
#      time.sleep(2)
#      print('Hello there, count this function speed!')
#
# exemplu()

# def logger(func):
#     def inner_func(*args, **kwargs):
#         print(f' Functia {func.__name__} are:\nParametri pozitionali {args}\nParametri keyword :{kwargs}')
#         result = func(*args, **kwargs)
#         print(f'Rezultatul este {result}')
#         return result
#     return inner_func
#
# @logger
# def suma(a, b, c=5):
#     return a + b + c
#
# suma(3, 4, c=7)

"""
6.	Decorators extra
Implementați o clasă User, cu următoarele cerințe:
– constructorul va primi nume, email, parola, și data nașterii 
– o metoda login, care va primi email și parola ca parametrii; dacă acestea sunt corecte, userul va fi marcat ca logat
– o metoda get_info, care va returna toate informațiile despre user DOAR DACĂ acesta este logat, folosind un decorator `@require_login` 
– o metoda logout, fara params, care delogheaza userul.

Se va testa apelarea metodei get_info inainte de logare, dupa logare, dupa delogare, și după încă o logare.
"""

# class User:
#     user = False
#     def __init__(self, nume, email, parola, data_nasterii):
#         self.nume = nume
#         self.email = email
#         self.parola = parola
#         self.data_nasterii = data_nasterii
#
#     def login(self, email, parola):
#         if email == self.email and parola == self.parola:
#             print(f'USerul {self.nume} este logat!')
#             User.user = True
#             # return print(User.user)
#         else:
#             print(f'Email-ul sau parola sunt gresite mai incearca')
#
#     def logout(self):
#         User.user = False
#         print(f'Userul {self.nume} s-a delogat')
#
#
#     def require_login(self):
#         def inner_func(*args, **kwargs):
#             if User.user == True:
#                 result = self(*args, **kwargs)
#                 return result
#             else:
#                 print(f'Te rog logheazate!')
#         return inner_func
#     @require_login
#     def get_info(self):
#         print(f'NUme : {self.nume}')
#         print(f'Ziua de nastere : {self.data_nasterii}')
#         print(f'Email : {self.email}')
#
#
# user1 = User('Madalin Chelu', 'madalin@ceva.ro','1234','13.11.92')
# user1.login('madalin@ceva.ro','1234')
# # user1.logout()
# user1.get_info()
