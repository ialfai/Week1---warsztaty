
from flask import Flask, render_template, request
import datetime
import random


def dice(code):
    dice_sum = 0
    if "D" not in code:
        print('Wrong code')
    else:
        code_splited = list(code.split("D"))
        if code_splited[0] == "":
            x = 1
        else:
            x = int(code_splited[0])
        y = int(code_splited[1].replace("+", "-").split("-")[0])
        if y not in [3, 4, 6, 8, 10, 12, 20, 100]:
            print('Wrong code')
        else:
            if "+" in code:
                z = int(code[-2:])
            elif "-" in code:
                z = int(code[-2:])
            else:
                z = 0
            for i in range(0, x):
                throw = random.randint(1, y)
                dice_sum += throw
            return dice_sum + z


app = Flask('Witaj użytkowniku!')\

@app.route('/')
def index():
    return 'Witaj użytkowniku!'\

@app.route('/gra2001', methods =['GET', 'POST'])
def gra2001():

    if request.method == 'GET':
        return render_template('2001.html')

    else: # so it's POST
        dices = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']
        throw_code1 = request.form['throw-code1']
        throw_code2 = request.form['throw-code2']
        dice_result1 = dice(throw_code1)
        dice_result2 = dice(throw_code2)
        dice_result = str(dice_result1+dice_result2)
        computer_dice_result1 = dice(dices[random.randint(0, 7)])
        computer_dice_result2 = dice(dices[random.randint(0, 7)])
        computer_dice_result = computer_dice_result1 + computer_dice_result2
        return render_template('2001.html', dice_result=dice_result, computer_dice_result=computer_dice_result)
        # elif request.form['hint'] == 'too big':
        #     guess = int((maximum - minimum) / 2) + minimum
        #     return render_template('2001.html', minimum=minimum, maximum=guess, guess=guess)
        # elif request.form['hint'] =='you win':
        #     return "I won! "


app.run(debug=True)