#!/usr/bin/env python3

import turtle
import math

kyna = turtle.Turtle()
kyna.speed(1)

def tehtava_1(matka):
    """Piirretään neliö"""
    for i in range(4):
        kyna.forward(matka)
        kyna.right(90)

    turtle.done()

def tehtava_2():
    """Piirretään 2 neliötä, toinen vasempaan yläreunaan ja toinen oikeaan alareunaan"""
    kyna.penup()
    kyna.goto(-200, 200)
    kyna.pendown()

    for i in range(4):
        kyna.forward(60)
        kyna.right(90)

    kyna.penup()
    kyna.goto(200, -200)
    kyna.pendown()

    for i in range(4):
        kyna.forward(20)
        kyna.right(90)

    turtle.done()

def tehtava_3(matka, kulma):
    kyna.fillcolor('red')
    kyna.begin_fill()
    for i in range(6):
        kyna.forward(matka)
        kyna.right(kulma)
    kyna.end_fill()
    turtle.done()

def tehtava_5(sivun_pituus, kulmien_maara):
    kulma = (kulmien_maara - 2) * 180 / kulmien_maara
    kulma = 180 - kulma # Piirrettävä kulma on ulkokulma
    for i in range(kulmien_maara):
        kyna.forward(sivun_pituus)
        kyna.right(kulma)
    turtle.done()

def suorakulmainen_kolmio(a, b):
    c = math.sqrt(a**2 + b**2)
    kulma = 180 - math.atan2(a, b) * 180 / math.pi
    print(c, kulma)
    kyna.forward(a)
    kyna.right(90)
    kyna.forward(b)
    kyna.right(kulma)
    kyna.forward(c)
    turtle.done()

def tehtava_8(sivu):
    for i in range(4):
        kyna.forward(sivu)
        kyna.left(90)

    print(f'Neliön pinta-ala on {sivu*sivu}')

    sade = math.sqrt(sivu*sivu / math.pi)

    print(f'Samankokoisen ympyrän säde on {sade}')

    kyna.penup()
    kyna.goto(-200, 0)
    kyna.pendown()
    kyna.circle(sade)
    turtle.done()


if __name__ == '__main__':
    # tehtava_1(40)
    # tehtava_2()
    # tehtava_3(100, 60)
    # tehtava_5(50, 9)
    # suorakulmainen_kolmio(60, 80)
    # tehtava_8(12)
    tehtava_8(100)
