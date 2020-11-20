# Jak zapewne wiesz, LOTTO to gra liczbowa polegająca na losowaniu 6 liczb z zakresu 1 – 49.
# Zadaniem gracza jest poprawne wytypowanie losowanych liczb. Nagradzane jest trafienie
# 3, 4, 5 lub 6 poprawnych liczb.
#
# Napisz program, który:
#
#     zapyta o typowane liczby, przy okazji sprawdzi następujące warunki:
#         czy wprowadzony ciąg znaków jest poprawną liczbą - ok
#         czy użytkownik nie wpisał tej liczby już poprzednio - to do
#         czy liczba należy do zakresu 1-49 - ok
#         po wprowadzeniu 6 liczb, posortuje je rosnąco i wyświetli na ekranie - ok
#         wylosuje 6 liczb z zakresu i wyświetli je na ekranie - ok
#         poinformuje gracza, ile liczb trafił - ok

import random

def lotto():
    players_numbers_int = []
    numbers_all = list(range(1, 50))
    random.shuffle(numbers_all)
    numbers_six = numbers_all[0: 6]
    correct_guesses = 0
    while True:
        players_numbers = input('Submit 6 numbers within the range of 1 and 49 (separate you numbers with a \'sprace\')\nDon\'t choose the same number twice: ')
        print('random numbers are: ', numbers_six)
        try:
            players_numbers = list(players_numbers.split(" "))
            for i in players_numbers:
                players_numbers_int.append(int(i))
            players_numbers_int.sort()
            print('Player\'s numbers are: ', players_numbers_int)
            if len(players_numbers_int) != 6:
                print('You have writen too many or too few numbers. Write exactly 6. ')
                continue
            elif max(players_numbers_int) > 49:
                print('You can submit only numbers within the range of 1 to 49: ')
                continue
            else:
                for i in range(0, 6):
                    if i in numbers_six:
                        correct_guesses +=1
                    else:
                        correct_guesses = correct_guesses
        except ValueError:
            print('Submit only numbers. ')
            continue
        if correct_guesses > 3:
            return f"You won a prize, you guessed correctly {correct_guesses} numbers"
        else:
            return f"you guessed correctly only {correct_guesses} numbers. You haven't won anything."

print(lotto())