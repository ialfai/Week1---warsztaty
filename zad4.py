# Zaimplementuj odwróconą grę w zgadywanie liczb w aplikacji webowej przy pomocy frameworka Flask.
# Użytkownik dostaje do dyspozycji formularz z trzema guzikami: To small, To big, You win.
#
# Informacje o aktualnych zmiennych min i max przechowuj w ukrytych polach formularza (pole typu hidden).
#
#     Uwaga – nie jest to rozwiązanie bezpieczne, bo użytkownik może ręcznie zmienić tego htmla,
#     np. przy pomocy Firebuga. W tej sytuacji jednak zupełnie wystarczające. Najwyżej zepsuje sobie zabawę ;)


from flask import Flask, render_template, request
import datetime
import random
from zad3_ import reversed_lotto

app = Flask('Witaj użytkowniku!')\

@app.route('/')
def index():
    return 'Witaj użytkowniku!'\

@app.route('/reversed_lotto', methods =['GET', 'POST'])
def reversed_lotto():
    minimum = 0
    maximum = 1000
    count = 0
    while True:
        guess = int((maximum - minimum) / 2) + minimum
        count += 1
        if count <= 10:
            if request.method == 'GET':
                return render_template('index.html', minimum=0, maximum=1000)
            else: # so it's POST
                if request.form['hint'] == 'too small':
                    return render_template('zgadywanie.html', nazwa='Za mała liczba, podaj na nowo.',
                                   right_number=request.form['right_number'])
                elif request.form['hint'] == 'too big':
                    return render_template('zgadywanie.html', nazwa='Za duża liczba, podaj na nowo.',
                                   right_number=request.form['right_number'])
                elif request.form['hint'] =='you win':
                    return "I won! "






    #
    #     minimum = 0
    #     maximum = 1000
    #     count = 0
    #     while True:
    #         guess = int((maximum - minimum) / 2) + minimum
    #         print("I\'m guessing: ", guess)
    #         answer = input("Your reply?: ")
    #         count += 1
    #         if count <= 10:
    #             if answer == 'you win':
    #                 print('I won!')
    #                 break
    #             elif answer == 'too small':
    #                 minimum = guess
    #                 continue
    #             elif answer == 'too big':
    #                 maximum = guess
    #                 continue
    #         else:
    #             if answer == 'you win':
    #                 print('I won!')
    #                 break
    #             else:
    #                 print('Don\'nt cheat! ')
    #                 continue
    #
    #
    # if request.method == 'GET':
    #     return render_template('zgadywanie.html', right_number=random.randint(1, 100))
    # else: #więc post
    #     if request.form['liczba'] == str(request.form['right_number']):
    #         return "Gratulacje, udało Ci się!"
    #     elif request.form['liczba'] > str(request.form['right_number']):
    #         return render_template('zgadywanie.html', nazwa='Za duża liczba, podaj na nowo.',
    #                                right_number=request.form['right_number'])
    #     elif request.form['liczba'] < str(request.form['right_number']):
    #         return render_template('zgadywanie.html', nazwa='Za mała liczba, podaj na nowo.',
    #                                right_number=request.form['right_number'])
    #

app.run(debug=True)