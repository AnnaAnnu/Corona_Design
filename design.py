import turtle
a=0
b=0
turtle.bgcolor("black")
turtle.speed(0)
turtle.pencolor("red")
turtle.penup()
turtle.goto(0,200)
turtle.pendown()

while True:
    turtle.backward(a)
    turtle.left(b)
    a+=3
    b+=1
    if b==201:
        break
turtle.close()    
