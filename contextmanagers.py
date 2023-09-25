"""
Context Managers
Se da un fisier text hello.txt, care contine un text scurt. Deschideți fișierul și citiți conținutul, folosind urmatoarele 2 metode:
-	try - finally
-	Fișierul se deschide înainte de try, folosind functia open
-	În interiorul try citim conținutul folosind functia read
-	În finally se închide fișierul
-	with (context manager)
-	Se va observa ca pentru with nu mai este nevoie sa inchidem noi manual fișierul, pentru ca context managerul face asta pentru noi.
"""

# metoda with
# with open('files/hello.txt', 'r') as my_file:
#     for line in my_file:
#         print(line)
    # print(my_file.readlines())
    #  print(my_file.read())

# # -	try - finally
# file = open('files/hello.txt')
# try:
#     lines = file.read()
#     print(lines)
# finally:
#     file.close()

