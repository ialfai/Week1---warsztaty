# Warsztat: Gra w zgadywanie liczb.
#
# Napisz prostą grę w zgadywanie liczb. Komputer musi wylosować liczbę w zakresie 1 – 100. Następnie:
#
#     Zadać pytanie: "Guess the number: " i pobrać liczbę z klawiatury.
#     Sprawdzić, czy wprowadzony napis, to rzeczywiście liczba i w razie błędu wyświetlić komunikat "It's not a number!", po czym wrócić do pkt. 1
#     Jeśli liczba podana przez użytkownika jest mniejsza niż wylosowana, wyświetlić komunikat "To small!", po czym wrócić do pkt. 1.
#     Jeśli liczba podana przez użytkownika jest większa niż wylosowana, wyświetlić komunikat "To big!", po czym wrócić do pkt. 1.
#     Jeśli liczba podana przez użytkownika jest równa wylosowanej, wyświetlić komunikat "You win!", po czym zakończyć działanie programu.
#
# Przykład:
# Guess the number: cześć
# It's not a number!
# Guess the number: 50
# To small!
# Guess the number: 75
# To big!
# Guess the number: 63
# You win!
#     Pamiętaj, aby obsłużyć odpowiednie błędy!
import random


def guessing():
    random_number = random.randint(1, 101)
    while True:
        users_number = input("Guess the number: ")
        try:
            users_number_int = int(users_number)
            if random_number == users_number_int:
                return "You win!"
            elif random_number > users_number_int:
                print("Too small! ")
                continue
            elif random_number < users_number_int:
                print("Too big! ")
                continue
        except ValueError:
            print('This is not a number. ')



print(guessing())