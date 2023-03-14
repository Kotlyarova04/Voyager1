"""
Dreamteam:
Kotlyarova Polina
Rafaevich Vita
Leonov Kirill
"""

# Import reguired modules.
import turtle as t
import math


# Used functions.
def pear(x, y, pensizee, pencolor, fillcolor):
    """
    Function for drawing a pear.
    :param x: first coordinate of the start of drawing pear
    :param y: second coordinate of the start of drawing pear
    :param pensizee: contour width
    :param pencolor: colour of the contour
    :param fillcolor: pear fillcolor
    :return: None
    """
    t.color(pencolor, fillcolor)
    t.pensize(pensizee)
    t.begin_fill()
    t.pu()
    t.goto(x, y)
    t.pd()
    t.rt(0)
    t.fd(31)
    t.rt(50)
    t.fd(50)
    t.rt(40)
    t.fd(60)
    t.lt(45)
    t.fd(50)
    t.rt(45)
    t.fd(30)
    t.lt(45)
    t.fd(50)
    t.rt(45)
    t.fd(70)
    t.rt(60)
    t.fd(80)
    t.rt(30)
    t.fd(120)
    t.rt(30)
    t.fd(80)
    t.rt(60)
    t.fd(70)
    t.rt(45)
    t.fd(50)
    t.lt(45)
    t.fd(30)
    t.rt(45)
    t.fd(50)
    t.lt(45)
    t.fd(60)
    t.rt(40)
    t.fd(50)
    t.rt(50)
    t.fd(22)
    t.end_fill()
    t.pu()


def rhomb(x, y, a, b, fillcolor, pensizee, pencolour):
    """
    Function for drawing a rhomb.
    :param x: first coordinate of the start of drawing rhomb
    :param y: second coordinate of the start of drawing rhomb
    :param a: length of the first side of the rhomb
    :param b: length of the second side of the rhomb
    :param fillcolor: rhomb fillcolor
    :param pensizee: contour width
    :param pencolour: colour of the contour
    :return: None
    """
    t.goto(x, y)
    t.color(pencolour, fillcolor)
    t.pensize(pensizee)
    t.begin_fill()
    t.pd()
    t.lt(20)
    for i in range(2):
        t.fd(a)
        t.rt(60)
        t.fd(b)
        t.rt(120)
    t.end_fill()
    t.pu()
    t.setheading(0)


def triangle(x, y, a, fillcolor, pensizee, pencolour):
    """
    Function for drawing a triangle.
    :param a: length of the side of the triangle
    :param y: second coordinate of the start of drawing triangle
    :param x: first coordinate of the start of drawing rectangle
    :param fillcolor: triangle fillcolor
    :param pensizee: contour width
    :param pencolour: colour of the contour
    :return: None
    """
    t.pu()
    t.goto(x, y)
    t.color(pencolour, fillcolor)
    t.pensize(pensizee)
    t.begin_fill()
    t.pd()
    for i in range(3):
        t.fd(a)
        t.lt(120)
    t.end_fill()
    t.pu()
    t.setheading(0)


def rectangle(x, y, a, b, fillcolor, pensizee, pencolour):
    """
    Function for drawing a rectangle.
    :param x: first coordinate of the start of drawing rectangle
    :param y: second coordinate of the start of drawing triangle
    :param a: length of the first side of the rectangle
    :param b: length of the second side
    :param fillcolor: rectangle fillcolor
    :param pensizee: contour width
    :param pencolour: colour of the contour
    :return: None
    """
    t.goto(x, y)
    t.color(pencolour, fillcolor)
    t.pensize(pensizee)
    t.begin_fill()
    t.pd()
    for i in range(2):
        t.fd(a)
        t.lt(90)
        t.fd(b)
        t.lt(90)
    t.end_fill()
    t.pu()
    t.setheading(0)


def circlee(x, y, pensizee, r, pencolor, fillcolor):
    """
    This function draws a circle.
    :param x: first coordinate of the start of drawing circle
    :param y: second coordinate of the start of drawing circle
    :param pensizee: contour width
    :param r: radius of circle
    :param pencolor: colour of the contour
    :param fillcolor: circle fillcolor
    :return: None
    """
    t.goto(x, y)
    t.pd()
    t.rt(45)
    t.pensize(pensizee)
    t.color(pencolor, fillcolor)
    t.begin_fill()
    t.circle(r)
    t.pu()
    t.end_fill()


def smile(x, y, pensizee, r, pencolor):
    """
    This function draws a smile in the form of a semicircle.
    :param x: first coordinate of the start of drawing smile
    :param y: second coordinate of the start of drawing smile
    :param pensizee: contour width
    :param r: radius of smile
    :param pencolor: colour of the contour
    :return: None
    """
    t.goto(x, y)
    t.pd()
    t.pensize(pensizee)
    t.color(pencolor)
    t.circle(r, 180)
    t.pu()


def semicircle(x, y, pensizee, r, pencolor, fillcolor):
    """
    This function draws a shaded semicircle.
    :param x: first coordinate of the start of drawing semicircle
    :param y: second coordinate of the start of drawing semicircle
    :param r: radius of semicircle
    :param pensizee: contour width
    :param fillcolor: semicircle fillcolor
    :param pencolor: colour of the contour
    :return: None
    """
    t.goto(x, y)
    t.pd()
    t.pensize(pensizee)
    t.color(pencolor, fillcolor)
    t.begin_fill()
    t.circle(r, 180)
    t.end_fill()
    t.pu()
    t.lt(180)


def ellipsoid(bigrad, littlerad, deg):
    """
    This function draws an ellips.
    :param bigrad: radius along the OX axis
    :param littlerad: radius along the OY axis
    :param deg: ellipse sector angle (=360 if we want to draw a full ellipse)
    :return: None
    """
    dx = t.xcor()
    dy = t.ycor()
    for i in range(deg):
        rad = math.radians(i)
        x = bigrad * math.sin(rad) + dx
        y = -littlerad * math.cos(rad) + littlerad + dy
        t.goto(x, y)


def pattern(change1, change2, change3, change4, change5, standard):
    """
    This function draws half of the Python logo, and with opposite (in sign) change-arguments, draws the other half.
    :param change1: x-radius of ellipse
    :param change2: y-radius of ellipse
    :param change3: x-diameter of ellipse
    :param change4: x-adjustment for drawing a circle
    :param change5: y-adjustment for drawing a circle
    :param standard: length of the center line before turns
    :return: None
    """

    t.begin_fill()
    t.pd()
    t.fd(standard)
    t.circle(standard//4,90)
    t.fd(standard)
    t.pu()
    t.goto(t.xcor() - change1, t.ycor() - change2)
    t.pd()

    ellipsoid(change1,change2,270)
    t.rt(180)
    t.fd(abs(change2))
    t.lt(90)
    t.fd(abs(change1))
    t.rt(90)
    t.fd(standard//8)
    t.rt(90)
    t.fd(abs(change1) + 40)
    t.pu()
    t.goto(t.xcor(),t.ycor() - change3)
    t.pd()

    ellipsoid(change2,change1,360)
    t.lt(180)
    t.fd(standard//8*3)
    t.lt(90)
    t.fd(standard//8*3)
    t.circle(-standard//8*3,90)
    t.end_fill()
    t.pu()

    t.goto(t.xcor() + change4,t.ycor() + change5)
    t.pd()
    t.fillcolor('white')
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.pu()


# General part.
t.setup(width = 1.0, height = 1.0)
t.speed(0)
t.pu()
t.setheading(0)
# Part of Kirill
change1, change2, change3, change4, change5, standard = 60, 30, 120, 5, 85, 80

t.goto(-550,5)
t.pensize(2)
t.pencolor('Cornflowerblue')
t.fillcolor('Cornflowerblue')

pattern(change1, change2, change3, change4, change5, standard)
t.goto(t.xcor() + 75, t.ycor() - 95)
t.setheading(180)

t.pencolor('DarkGoldenrod1')
t.fillcolor('DarkGoldenrod1')
pattern(-change1, -change2, -change3, -change4, -change5, standard)
t.setheading(0)
t.pu()

# letter P
rectangle(-650, 200, 8, 60, 'DarkGoldenrod1', 2, 'DarkGoldenrod1')
semicircle(-642, 220, 1, 20, 'DarkGoldenrod1', 'DarkGoldenrod1')
semicircle(-642, 230, 1, 10, 'white', 'white')

# letter Y
rectangle(-596, 200, 8, 30, 'DarkGoldenrod1', 2, 'DarkGoldenrod1')
t.lt(30)
rectangle(-588, 230, -8, 35, 'DarkGoldenrod1', 2, 'DarkGoldenrod1')
t.rt(30)
rectangle(-596, 230, 8, 35, 'DarkGoldenrod1', 2, 'DarkGoldenrod1')

# letter T
rectangle(-542, 200, 8, 60, 'DarkGoldenrod1', 2, 'DarkGoldenrod1')
t.lt(90)
rectangle(-518, 260, -8, 40, 'DarkGoldenrod1', 2, 'DarkGoldenrod1')

# letter H
rectangle(-504, 200, 8, 60, 'DarkGoldenrod1', 2, 'DarkGoldenrod1')
rectangle(-472, 200, 8, 60, 'DarkGoldenrod1', 2, 'DarkGoldenrod1')
t.lt(90)
rectangle(-464, 234, -8, 40, 'DarkGoldenrod1', 2, 'DarkGoldenrod1')

# letter O
t.goto(-430, 200)
t.begin_fill()
t.pd()
ellipsoid(20, 30, 360)
t.end_fill()
t.goto(-430, 210)
t.fillcolor('white')
t.begin_fill()
ellipsoid(10, 20, 360)
t.end_fill()
t.pu()

# letter N
rectangle(-395, 200, 8, 60, 'DarkGoldenrod1', 2, 'DarkGoldenrod1')
rectangle(-363, 200, 8, 60, 'DarkGoldenrod1', 2, 'DarkGoldenrod1')
t.begin_fill()
t.pd()
t.goto(-387, 244)
t.goto(-387, 260)
t.goto(-363, 216)
t.goto(-363, 200)
t.end_fill()
t.pu()

# Part of Polina.
# Pear with smile, twig and leaf.
pear(-3, 70, 5, "yellowgreen", "greenyellow")
rectangle(0, 70, 5, 55, "brown", 3, "brown")
rhomb(6, 120, 60, 60, "green", 3, "green")
circlee(-30, -20, 2, 10, "black", "black")
circlee(19, -12, 2, 10, "black", "black")
smile(-13, -90, 3, 15, "black")
circlee(55, -55, 2, 5, "pink", 'pink')
circlee(-45, -55, 2, 5, "pink", 'pink')

# Letter P.
rectangle(-130, 200, 8, 60, "goldenrod", 5, "goldenrod")
semicircle(-120, 215, 1, 23, "goldenrod", "goldenrod")
semicircle(-120, 230, 1, 10, "white", "white")

# Letter E.
rectangle(-70, 200, 8, 57, "goldenrod", 5, "goldenrod")
rectangle(-70, 200, 45, 8, "goldenrod", 5, "goldenrod")
rectangle(-70, 225, 45, 8, "goldenrod", 5, "goldenrod")
rectangle(-70, 250, 45, 8, "goldenrod", 5, "goldenrod")
t.setheading(65)

# Letter A.
rectangle(10, 200, 65, 8, "goldenrod", 5, "goldenrod")
t.setheading(210)
rectangle(35, 260, 8, 65, "goldenrod", 5, "goldenrod")
t.setheading(0)
rectangle(20, 220, 30, 8, "goldenrod", 5, "goldenrod")
t.setheading(0)
rectangle(95, 200, 8, 60, "goldenrod", 5, "goldenrod")

# Letter R.
semicircle(105, 220, 1, 21, "goldenrod", "goldenrod")
semicircle(105, 230, 1, 10, "white", "white")
t.setheading(245)
rectangle(105, 220, 8, 30, "goldenrod", 5, "goldenrod")

# Part of Vita
# Drawing mountains.
t.pd()
triangle(310, -100, 190, "light blue", 3, "grey")
triangle(440, -100, 110, "light blue", 3, "grey")
triangle(500, -100, 220, "light blue", 3, "grey")
# Drawing trees.
t.setheading(270)
circlee(330, -60, 1, 20, "grey", "green")
rectangle(340, -110, 7, 50, "brown", 1, "black")
circlee(385, -90, 1, 17, "grey", "green")
circlee(415, -90, 1, 17, "grey", "green")
rectangle(406, -110, 10, 40, "brown", 1, "black")
circlee(400, -75, 1, 17, "grey", "green")
circlee(600, -90, 1, 15, "grey", "green")
circlee(630, -90, 1, 15, "grey", "green")
rectangle(621, -110, 7, 40, "brown", 1, "black")
circlee(615, -75, 1, 15, "grey", "green")
circlee(670, -60, 1, 20, "grey", "green")
rectangle(680, -110, 7, 50, "brown", 1, "black")
# Drawing white peaks.
triangle(380, 21, 50, "white", 3, "grey")
triangle(480, -31, 30, "white", 3, "grey")
triangle(590, 56, 40, "white", 3, "grey")

# Letter P.
rectangle(400, 200, 8, 60, 'light blue', 2, 'light blue')
semicircle(408, 220, 1, 20, 'light blue', 'light blue')
semicircle(408, 230, 1, 10, 'white', 'white')

# Letter E.
rectangle(450, 200, 8, 60, 'light blue', 2, 'light blue')
rectangle(458, 200, 24, 8, 'light blue', 2, 'light blue')
rectangle(458, 226, 24, 8, 'light blue', 2, 'light blue')
rectangle(458, 252, 24, 8, 'light blue', 2, 'light blue')

# Letter A.
t.rt(20)
rectangle(506, 204, 8, 62, 'light blue', 2, 'light blue')
t.goto(552, 230)
t.rt(160)
rectangle(540, 260, 8, 60, 'light blue', 2, 'light blue')
t.pu()
rectangle(520, 226, 24, 8, 'light blue', 2, 'light blue')

# Letter K.
rectangle(584, 200, 8, 60, 'light blue', 2, 'light blue')
t.rt(45)
rectangle(592, 230, -8, 35, 'light blue', 2, 'light blue')
t.pu()
t.goto(592, 230)
t.rt(135)
rectangle(592, 230, 8, 35, 'light blue', 2, 'light blue')
t.done()