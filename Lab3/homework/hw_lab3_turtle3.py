from turtle import *
def draw_square(length, col):
    for _ in range(4):
        color(col)
        forward(length)
        left(90)

draw_square(100, 'red')
mainloop()
