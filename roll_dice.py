"""
19. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Ia numărul ghicit de la utilizator
Verifică și afișează dacă utilizatorul a ghicit
Vei avea 3 opțiuni
Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
Ai ghicit. Felicitări! Ai ales x si zarul a fost y.

"""


import random

# Generarea unui număr random între 1 și 6 (pentru simularea aruncării unui zar)
# dice_roll = random.randint(1, 6)
#
# # Citirea numărului ghicit de la utilizator
# guess = int(input("Ghicește numărul (între 1 și 6): "))
#
# if guess == dice_roll:
#     print(f'Ai ghicit. Felicitări! Ai ales {guess} si zarul a fost {dice_roll}.')
# elif guess < dice_roll:
#     print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {guess} dar a fost {dice_roll}.')
# else:
#     print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.')

# while True :
#     choice = input('Wanna play again yes or no?')
#     if choice != "no":
#         roll_dice = random.randint(1, 6)
#         print(roll_dice)
#         user_choice = int(input('Guess the number : '))
#         if roll_dice == user_choice:
#             print('Congrats you guessed')
#         else:
#             print(f'Sadly that\'s not the number, the roll was {roll_dice} ')
#     else:
#         print('Byeee!!!')
#         break

