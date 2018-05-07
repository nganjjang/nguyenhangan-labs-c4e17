from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes

from random import choice, randint

def generate_quiz():
    text = choice(['BLUE', 'RED', 'YELLOW', 'GREEN'])
    color = choice(['#3F51B5', '#C62828', '#FFD600', '#4CAF50'])
    quiz_type = randint(0, 1)
    return [text, color, quiz_type]
    # return [
    #             'RED',
    #             '#4CAF50',
    #             randint(0, 1) # 0 : meaning, 1: color
    #         ]

def mouse_press(x, y, text, color, quiz_type):
    if quiz_type == 0:
        if text == 'BLUE':
            if 20 <= x <= 120 and 60 <= y <= 160:
                return True
            else:
                return False
        elif text == 'RED':
            if 140 <= x <= 240 and 60 <= y <= 160:
                return True
            else:
                return False
        elif text == 'YELLOW':
            if 20 <= x <= 120 and 180 <= y <= 280:
                return True
            else:
                return False
        elif text == 'GREEN':
            if 140 <= x <= 240 and 180 <= y <= 280:
                return True
            else:
                return False

    if quiz_type == 1:
        if color == '#3F51B5':
            if 20 <= x <= 120 and 60 <= y <= 160:
                return True
            else:
                return False
        elif color == '#C62828':
            if 140 <= x <= 240 and 60 <= y <= 160:
                return True
            else:
                return False
        elif color == '#FFD600':
            if 20 <= x <= 120 and 180 <= y <= 280:
                return True
            else:
                return False
        elif color == '#4CAF50':
            if 140 <= x <= 240 and 180 <= y <= 280:
                return True
            else:
                return False
    # return True
