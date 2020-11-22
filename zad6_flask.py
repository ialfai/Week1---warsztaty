
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


app = Flask('Witaj użytkowniku!')\

@app.route('/')
def index():
    return 'Witaj użytkowniku!'\

@app.route('/gra2001', methods =['GET', 'POST'])
def gra2001():

    if request.method == 'GET':
        total_result = 0
        computer_total = 0
        return render_template('2001.html', total_result=total_result, computer_total=computer_total)
    else: # so it's POST
        total_result = int(request.form['total_result'])
        computer_total = int(request.form['computer_total'])
        dices = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']
        throw_code1 = request.form['throw-code1']
        throw_code2 = request.form['throw-code2']
        #2 dice throws for player
        dice_result1 = dice(throw_code1)
        dice_result2 = dice(throw_code2)
        dice_result = dice_result1+dice_result2 # liczba
        #2 dice throws for computer
        computer_dice_result1 = dice(dices[random.randint(0, 7)])
        computer_dice_result2 = dice(dices[random.randint(0, 7)])
        computer_dice_result = computer_dice_result1 + computer_dice_result2 # liczba
        #calculating the total score, depending on the number
        if truornot(total_result, computer_total): # this is to know if the score is below 2001
            if dice_result == 7:
                total_result = int(total_result/7)
            elif dice_result == 11:
                total_result = total_result * 11
            else:
                total_result += int(dice_result)
            if computer_dice_result == 7:
                computer_total = int(computer_total/7)
            elif computer_dice_result == 11:
                computer_total = computer_total * 11
            else:
                computer_total += int(computer_dice_result)
            return render_template('2001.html', dice_result=dice_result, computer_dice_result=computer_dice_result,
                               total_result=total_result,
                               computer_total=computer_total)
        else:
            return render_template('2001.html',
                               total_result=total_result,
                               computer_total=computer_total, extra="We have a winner")



app.run(debug=True)