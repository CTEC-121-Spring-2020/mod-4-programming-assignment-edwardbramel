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
    circ1 = Circle(Point(200, 500), 60)
    circ1.setFill("black")
    circ1.draw(win)

    circ2 = Circle(Point(550, 500), 60)
    circ2.setFill("black")
    circ2.draw(win)

    input()


main()
