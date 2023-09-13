"""   Structuri de date
Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.


"""

"""

1. Declară o listă note_muzicale în care să pui do re mi etc până la do
Afișeaz-o.
Inversează ordinea folosind slicing și suprascrie această listă.
Printează varianta actuală (inversată).
Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea.
Nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat.
Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.

Concluzii: slicing e temporar, dacă vrei să păstrezi nouă variantă va trebui să suprascrii lista 
sau să o salvezi într-o listă nouă.
 Metoda găsită de tine face suprascrierea automat și permanentizează aceste modificări. 
Ambele variante își găsesc utilitatea în funcție de ce ne dorim în acel moment. 
"""
# note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# print(note_muzicale)
# note_muzicale = note_muzicale[::-1]
# print(note_muzicale)
# note_muzicale.reverse()
# print(note_muzicale)

"""
2. De câte ori apare ‘do’?
"""
# note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# print(note_muzicale.count('do'))

"""
3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
   Găsește 2 variante să le unești într-o singură listă. 

"""
# a = [3, 1, 0, 2]
# b = [6, 5, 4]
# c = a +b # [3, 1, 0, 2, 6, 5, 4]
# print(c)
# a.extend(b)
# print(a)

"""
4.
Sortează și afișează lista generată la exercițiul anterior.
Șterge numărul 0 folosind o funcție.
Afișaza iar lista.

"""
# c = [3, 1, 0, 2, 6, 5, 4]
# c.sort()
# print(c) # [0, 1, 2, 3, 4, 5, 6]
# c.remove(0)
# print(c) # [1, 2, 3, 4, 5, 6]

"""
5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
Lista este goală.
Lista nu este goală.

"""
# c = [3, 1, 0, 2, 6, 5, 4]
# if len(c) == 0:
#     print('Lista este goala !')
# else:
#     print('Lista nu este goala')

"""
6. Folosește o funcție care să șteargă lista de la exercițiul 3.

"""

# c = [3, 1, 0, 2, 6, 5, 4]
# c.clear()
# # del c
# print(c)

"""
7. Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.

"""
# c = [3, 1, 0, 2, 6, 5, 4]
# c.clear()
#
# if len(c) == 0:
#     print('Lista este goala')
# else:
#     print('lista nu este goala')

"""
8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)


"""
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}

# for key in dict1.keys():
#     print(key)
# def afisare(dict):
#     for key in dict.keys():
#         print(key)
#
# afisare(dict1)

"""
9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie

"""
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}

# for  nume, nota in dict1.items():
#     print(f'{nume} a luat nota {nota}')
# for elev in dict1.keys():
#     print(f'{elev} a luat nota {dict1[elev]}')

"""
10. Dorel a făcut contestație și a primit 6
Modifică nota lui Dorel în 6
Printează nota după modificare

"""
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# dict1['Dorel'] = 6
# print(dict1)

"""
11. Gigel se transferă din clasă
Căuta o funcție care să îl șteargă
Vine un coleg nou. Adaugă Ionică, cu nota 9
Printează noii elevi

"""
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# # del dict1['Gigel']
# dict1.pop('Gigel')
# print(dict1) # {'Ana': 8, 'Dorel': 5}
# dict1['Ionica'] = 9
# print(dict1) # dict1 = {'Ana': 8, 'Dorel': 5, 'Ionica': 9}

"""
12. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:

Declară o Listă cu 5 jucători
Schimbari_efectuate = te joci tu cu valori diferite
Schimbari_max = 3

Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
Efectuează schimbarea 
Șterge jucătorul scos din listă
Adaugă jucătorul intrat
Afișază a intrat x, a ieșit y, mai ai z schimbări

Dacă jucătorul nu e în teren:
Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
Afișază ‘mai ai z schimbări’

Testează codul cu diferite valori

Google search hint
“how to check if item is în list python”


"""
# jucatori = ['Madalin', 'Andrei', 'Alex', 'Gigel', 'Ion']
# SCHIMBARI_MAX = 3
# schimbari_efectuate = 0
#
#
# print('Pe teren se afla urmatorii jucatori :')
# for i in jucatori:
#     print(i, end=' ')
# while True:
#     schimbare = input('Ce jucator vrei sa schimbi :')
#     if schimbare in jucatori:
#         print(schimbare)
#         index_schimbare = jucatori.index(schimbare)
#         if schimbari_efectuate < SCHIMBARI_MAX:
#             print(schimbari_efectuate)
#             print(SCHIMBARI_MAX)
#             jucatori.pop(index_schimbare)
#             inlocuitor = input('Cu ce jucator vrei sa il inlocuiesti')
#             print(inlocuitor)
#             jucatori.append(inlocuitor)
#             schimbari_efectuate += 1
#         else:
#             print(f'Ai depasit numarul maxim de schimari {SCHIMBARI_MAX}')
#             break
#     else:
#         print('Jucatorul nu este in teren')

"""
13.
Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
Adaugă în zilele_sapt ‘luni’
Afișează zile_sapt

"""


# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# zile_sapt.add('luni')
# # Adaugă în zilele_sapt ‘luni’ - nu permite duplicate
# print(zile_sapt)
# print(type(zile_sapt))

"""
14.Folosește un if și verifică dacă:
Weekend este un subset al zilelor din săptămânii.
Weekend nu este un subset al zilelor din săptămânii.


"""
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
#
# if weekend.issubset(zile_sapt):
#     print('Weekend este un subset al zilelor din săptămânii.')
# else:
#     print('Weekend nu este un subset al zilelor din săptămânii.')

"""
15. Afișează diferențele dintre aceste 2 seturi.
"""
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
#
# print(zile_sapt.difference(weekend)) # {'luni', 'joi', 'miercuri', 'marți', 'vineri'}

"""
16. Afișează intersecția elementelor din aceste 2 seturi.

"""
# print(zile_sapt.intersection(weekend)) #{'sâmbăta', 'duminică'}
