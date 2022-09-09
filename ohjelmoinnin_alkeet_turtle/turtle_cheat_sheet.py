import turtle

# Aloitus

kyna = turtle.Turtle() # Luodaan kynä jolla voi piirtää
kyna.speed(1) # Kynän nopeus: 0-10, 0 nopein, 1 hitain
kyna.penup() # Nostaa kynän ilmaan
kyna.pendown() # Laskee kynän
kyna.pensize(3) # Kynän paksuus: positiivinen luku

# Liikkuminen

kyna.forward(10) # Liikkuu eteenpäin 10 askelta
kyna.left(90) # Kääntyy vasemmalle 90 astetta
kyna.forward(10) # Liikkuu taakepäin 10 askelta
kyna.left(90) # Kääntyy vastapäivään 90 astetta
kyna.right(90) # Kääntyy myötäpäivään 90 astetta
kyna.goto(0, 0) # Siirtyy koordinaattipisteeseen (0, 0)

# Väritys

kyna.pencolor('blue') # Muuttaa kynän värin siniseksi
kyna.fillcolor('yellow') # Muuttaa täyttövärin keltaiseksi
kyna.begin_fill() # Aloittaa täyttövärjäyksen
kyna.end_fill() # Lopettaa täyttövärjäyksen

# Ympyrä

kyna.circle(30) # Piirtää ympyrän, jonka säde on 30

turtle.exitonclick()