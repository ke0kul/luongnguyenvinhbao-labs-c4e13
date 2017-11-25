from random import *
from calculator import eval

def generate_quiz():
    x = randint(0, 10)
    y = randint(0, 10)
    error = randint(-1, 1)
    op = choice(['+', '-', '*', '/'])
    return [x, y, op, eval(x, y, op) + error]

def check_answer(x, y, op, result, user_choice):
    true_result = eval(x, y, op)
    if user_choice:
        if true_result == result:
            return True
        else:
            return False
    else:
        if true_result == result:
            return False
        else:
            return True
