from turtle import *
def draw_star(x, y, length):
    for i in range(5):
        forward(length)
        right(144)
    penup()
    goto(x, y)
    pendown()

draw_star(10, 10, 100)
mainloop()
