# Zaimplementuj grę 2001. Poniżej znajdziesz zasady.
# 2001 – Zasady Gry
#
#     Każdy z graczy zaczyna z liczbą punktów równą 0.
#     W swojej turze, gracz rzuca 2 kośćmi do gry (standardowe kości sześciościenne).
#     Wyrzucona liczba oczek jest dodawana do sumarycznej liczby punktów.
#     Począwszy od drugiej tury:
#         jeśli gracz wyrzuci 7, dzieli swoją liczbę punktów przez tę wartość odrzucając część ułamkową,
#         jeśli wyrzuci 11, mnoży aktualną liczbę punktów przez tę wartość.
#     Wygrywa gracz, który jako pierwszy uzyska 2001 punktów.
#
# Implementacja
#
#     Zaimplementuj grę w wersji dla dwóch graczy.
#     Niech będzie to aplikacja konsolowa.
#     Niech drugim graczem będzie komputer.
#     Po każdej turze wyświetl aktualną liczbę punktów.
#     Rzut gracza, powinien odbywać się po naciśnięciu przez użytkownika klawisza enter.
#     Rzut komputera następuje automatycznie, po rzucie gracza. Zakończ program w momencie,
#     gdy gracz, lub komputer osiągnie więcej niż 2001 punktów.
import random

def truornot(a, b):
    if a < 2001:
        z = True
    else:
        z = False
    if b < 2001:
        y = True
    else:
        y = False
    if z + y == 2:
        return True
    elif z + y < 2:
        return False



def gra2001():
    player1 = 0
    player2 = 0
    while truornot(player1, player2):
        throw_command = input("")
        if throw_command == "":
            throw_dice1 = random.randint(2, 12)
            print("dice throw result:", throw_dice1)
            if throw_dice1 == 7:
                player1 = int(player1/7)
            elif throw_dice1 == 11:
                player1 = int(player1 * 11)
            else:
                player1 += throw_dice1
            print("player 1 result: ", player1)
            throw_dice2 = random.randint(2, 12)
            print("dice throw result:", throw_dice2)
            if throw_dice2 == 7:
                player2 = int(player2/7)
            elif throw_dice2 == 11:
                player2 = int(player2 * 11)
            else:
                player2 += throw_dice2
            print("player 2 result: ", player2)
    if player1 > 2001:
        return "Player1 won!"
    else:
        return "Player2 won!"

print(gra2001())





# Modyfikacja 1
#
# Zauważyłeś pewno, że gra w obecnej wersji jest mało interaktywna i sprowadza się tylko
# i wyłącznie, do klikania klawisza enter. Spróbujmy uczynić ją trochę bardziej interaktywną.
#
#     Przed każdym rzutem, daj graczowi wybór.
#     Niech wybierze 2 kości z zestawu: D3, D4, D6, D8, D10, D12, D20, D100.
#     Kości mogą się powtarzać, gracz może też użyć 2 różnych kości.
#     Niech wybór kości odbywa się za pomocą wprowadzenia odpowiedniego łańcucha znaków przez gracza
#     (po jednym na każdą z kości).
#     Możesz wykorzystać kod z zadania Kostka do gry.
#     Wybór kości przez komputer niech będzie losowy.
#
# Reszta zasad pozostaje bez zmian.
# Modyfikacja 2
#
# Spróbuj teraz przenieść swoją grę na serwer przy użyciu Flaska. Aby przechowywać informację między turami,
# wykorzystaj ukryte pola formularza. Nie jest to najlepsze rozwiązanie (może być podatne na oszukiwanie),
# ale na tę chwilę się tym nie przejmujemy. Wybór kości przed rzutem, powinien odbywać się za pomocą formularza.