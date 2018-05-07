from random import *
from eval import calc

def generate_quiz():
    # Hint: Return [x, y, op, display_result]
    x = randint(1, 10)
    y = randint(1, 10)
    op = choice(['+', '-', '*', '/'])
    result = calc(x, y, op)

    error = choice([-1, 0, 1])
    display_result = result + error

    return [x, y, op, display_result]


def check_answer(x, y, op, display_result, user_choice):
    result = calc(x, y, op)
    if result == display_result:
        if user_choice == True:
            return True
        else:
            return False
    elif result != display_result:
        if user_choice == True:
            return False
        else:
            return True
    # user_choice: True, False
    # print(user_choice)
    # return True
    #return False
    # pass
    #function tra ra ket qua nguoi dung true hay false
