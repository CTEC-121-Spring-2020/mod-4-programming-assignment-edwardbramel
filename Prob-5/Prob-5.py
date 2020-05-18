# Module 5
#   Programming Assignment 6
#       Prob-5.py

# eddy
from graphics import *


def main():
    win = GraphWin("shapes", 800, 600)
    # rec xy and xy
    rect = Rectangle(Point(150, 350), Point(600, 500))
    rect.setFill("blue")
    rect.draw(win)

    # wheels
    circ1 = Circle(Point(230, 500), 60)
    circ1.setFill("black")
    circ1.setOutline("gray")
    circ1.draw(win)
    circ1 = Circle(Point(230, 500), 40)
    circ1.setFill("silver")
    circ1.setOutline("gray")
    circ1.draw(win)

    circ2 = Circle(Point(520, 500), 60)
    circ2.setFill("black")
    circ2.setOutline("gray")
    circ2.draw(win)
    circ2 = Circle(Point(520, 500), 40)
    circ2.setFill("silver")
    circ2.setOutline("gray")
    circ2.draw(win)

    # lines
    line1 = Line(Point(380, 250), Point(380, 500))
    line1.draw(win)
    line2 = Line(Point(160, 350), Point(160, 490))
    line2.draw(win)

    # seat
    rec2 = Rectangle(Point(380, 350), Point(480, 250))
    rec2.setOutline("blue")
    rec2.setFill("blue")
    rec2.draw(win)

    # bumpers
    rec3 = Rectangle(Point(140, 490), Point(160, 470))
    rec3.setFill("gray")
    rec3.draw(win)

    rec4 = Rectangle(Point(590, 490), Point(620, 470))
    rec4.setFill("gray")
    rec4.draw(win)

    # lets see if this works
    window = Polygon(Point(480, 250), Point(480, 350), Point(600, 350))
    window.setFill("black")
    window.draw(win)

    input()


main()
