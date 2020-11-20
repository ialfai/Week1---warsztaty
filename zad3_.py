# Odwróćmy teraz sytuację z pierwszego zadania: ("Gra w zgadywanie liczb").
# Niech użytkownik pomyśli sobie liczbę z zakresu 1-1000, a komputer będzie zgadywał.
# Zrobi to maksymalnie w 10 ruchach (pod warunkiem, że gracz nie będzie oszukiwał).
#
# Zadaniem gracza będzie udzielanie odpowiedzi "To small", "To big", "You win".
#
# Do tego warsztatu dołączony jest schemat blokowy algorytmu. Zaimplementuj go w Pythonie.

def reversed_lotto():
    print('Think about one particular number from 1 to 1000 and let the computer guess it.\n'
          'If the computer\'s guess is wrong, give it a hint: "too small" or "too big"\n'
          'If the computer\'s guess is right, write "You win"')
    minimum = 0
    maximum = 1000
    count = 0
    while True:
        guess = int((maximum - minimum)/2) + minimum
        print("I\'m guessing: ", guess)
        answer = input("Your reply?: ")
        count += 1
        if count <= 10:
            if answer == 'you win':
                print('I won!')
                break
            elif answer == 'too small':
                minimum = guess
                continue
            elif answer == 'too big':
                maximum = guess
                continue
        else:
            if answer == 'you win':
                print('I won!')
                break
            else:
                print('Don\'nt cheat! ')
                continue



reversed_lotto()
