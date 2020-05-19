# Module 5
#   Programming Assignment 6
#       Prob-7.py

# Edward
"""i need two eyes, a nose, a mouth with some teeth, two ears and some hair"""

from graphics import *


def main():
    win = GraphWin("shapes", 750, 700)
    anOval = Oval(Point(200, 100), Point(600, 600))
    anOval.setFill(color_rgb(233, 227, 184))
    anOval.draw(win)

    # eyes
    eye1 = Circle(Point(290, 250), 30)
    eye1.setFill("white")
    eye1.draw(win)

    eye2 = eye1.clone()
    eye2.move(200, 0)
    eye2.draw(win)

    pupe = Circle(Point(290, 250), 10)
    pupe.setFill("black")
    pupe.draw(win)

    pupe2 = pupe.clone()
    pupe2.move(200, 0)
    pupe2.draw(win)

    # mouth
    mouth = Rectangle(Point(330, 400), Point(450, 500))
    mouth.setFill("black")
    mouth.setOutline(color_rgb(255, 204, 204))
    mouth.setWidth(10)
    mouth.draw(win)

    # teeth
    teeth = Rectangle(Point(330, 400), Point(450, 430))
    teeth.setFill("white")
    teeth.draw(win)

    line1 = Line(Point(390, 400), Point(390, 430))
    line1.draw(win)

    line2 = line1.clone()
    line2.move(30, 0)
    line2.draw(win)

    line3 = line1.clone()
    line3.move(-30, 0)
    line3.draw(win)

    line4 = line1.clone()
    line4.move(45, 0)
    line4.draw(win)

    line5 = line1.clone()
    line5.move(-45, 0)
    line5.draw(win)

    # toung
    toung = Rectangle(Point(330, 490), Point(450, 500))
    toung.setFill("red")
    toung.draw(win)

    # nose
    nose = Polygon(Point(420, 300), Point(380, 300),
                   Point(360, 350), Point(440, 350))
    nose.draw(win)

    # hair
    hair = Polygon(Point(600, 70), Point(575, 230), Point(
        490, 170), Point(300, 170), Point(225, 230), Point(200, 70))
    hair.setFill(color_rgb(172, 148, 96))
    hair.draw(win)
    input()

    # ears ear1.setFill(color_rgb(243, 217, 134))
    """ear1 = Oval(Point(550, 250), Point(600, 280))"""
    ear1 = Circle(Point(50, 50), 100)
    ear1.setFill("black")
    ear1.draw(win)

    red = Rectangle(Point(100, 100), Point(200, 200))
    red.draw(win)


main()
