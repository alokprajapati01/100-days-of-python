#painting
import turtle
import turtle as t
import random

#set a turtle
t = t.Turtle()
t.speed("fastest") # set speed
t.penup()
turtle.colormode(255)#it is use for RGB colors

screen = turtle.Screen()# set screen 

t.setheading(225) 
t.forward(300)
t.setheading(0)

color_list = [ (250, 246, 249), (234, 239, 244), (243, 249, 247), (201, 170, 116), (155, 181, 192), (218, 204, 123), (151, 184, 173), (192, 161, 180), (161, 204, 214), (166, 209, 196), (208, 178, 195), (206, 151, 40), (174, 189, 214), (209, 186, 177), (219, 201, 33)]


dot_count = 100

for i in range(1, dot_count + 1):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    if i % 10 == 0: # This conditaion help to create 10 X 10 painting canva 😊
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)
