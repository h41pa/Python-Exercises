"""
## Generators
Implementați un generator pentru loteria 6/49 și noroc:
-	Primele 6 apelări către generator vor da cate un numar intre 1 si 49 (inclusiv
-	Ultima apelare va da un singur număr de “noroc” format din 7 cifre
"""
# import random
#
# def generator_loterie():
#     for _ in range(6):
#         yield random.randint(1, 49)
#
#     noroc = random.randint(1000000, 9999999)
#     yield noroc
#
# loterie = generator_loterie()
# for i in range(7):
#     numar = next(loterie)
#     if i < 6:
#         print(f' Numarul {i +1 } este {numar}')
#     else:
#         print(f'Numarul noroc este {numar}')

#                      ~~~alta modalitate~~~~

# import random
# def loto_gen():
#     my_list = random.sample(range(1,60),6)
#     for nr in my_list:
#         yield nr
#     yield random.randint(1_000_000, 9_999_999)
#
# for i in loto_gen():
#     print(i)

#                      ~~~alta modalitate~~~~

# import random
# def generator_loterie():
#     nr_generate = []
#     for i in range(6):
#         print(i)
#         numar = random.randint(1, 49)
#         print(numar)
#         while numar in nr_generate:
#             print(nr_generate)
#             numar = random.randint(1, 49)
#             print(numar)
#         nr_generate.append(numar)
#         print(nr_generate)
#         yield numar
#         print(numar)
#
# for nr in generator_loterie():
#     print(nr)

#                      ~~~alta modalitate~~~~

# import random
# def generator_loterie():
#     no_1 = random.randint(1, 49)
#     yield no_1
#     while True:
#         no_2 = random.randint(1,49)
#         if no_2 != no_1:
#             break
#     yield no_2
#     while True:
#         no_3 = random.randint(1,49)
#         if no_3 != no_2 and no_3 != no_1:
#             break
#     yield no_3
#     while True:
#         no_4 = random.randint(1, 49)
#         if no_4 != no_3 and no_4 != no_2 and no_4 != no_1:
#             break
#     yield no_4
#     while True:
#         no_5 = random.randint(1, 49)
#         if no_5 != no_4 and no_5 != no_3 and no_5 != no_2 and no_5 != no_1:
#             break
#     yield no_5
#     while True:
#         no_6 = random.randint(1, 49)
#         if no_6 != no_5 and no_6 != no_4 and no_6 != no_3 and no_6 != no_2 and no_6 != no_1:
#             break
#     yield no_6
#     no_noroc = ""
#     for i in range(7):
#         x = str(random.randint(1,49))
#         no_noroc = no_noroc + x
#     yield no_noroc
#
# gen_loto = generator_loterie()
#
# print(f'Primul numar castigator: {next(gen_loto)}')
# print(f'Al 2-lea numar castigator: {next(gen_loto)}')
# print(f'Al 3-lea numar castigator: {next(gen_loto)}')
# print(f'Al 4-lea numar castigator: {next(gen_loto)}')
# print(f'Al 5-lea numar castigator: {next(gen_loto)}')
# print(f'Al 6-lea numar castigator: {next(gen_loto)}')
# print(f'Numarul noroc este: {next(gen_loto)}')

