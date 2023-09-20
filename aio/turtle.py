from turtle import *

# t = Turtle()
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
t = turtle()
t.speed(0)
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)
    
t.screen.mainloop()