# Module 5
#   Programming Assignment 6
#       Prob-6.py

# eddy
from graphics import *


def main():
    win = GraphWin("shapes", 823, 620)

    # lego1
    lego1 = Rectangle(Point(15, 50), Point(380, 160))
    lego1.setFill("blue")
    lego1.setOutline("black")
    lego1.setWidth(6)
    lego1.draw(win)

    # jiggy parts
    jeg = Rectangle(Point(25, 30), Point(70, 50))
    jeg.setFill("blue")
    jeg.setOutline("black")
    jeg.setWidth(6)
    jeg.draw(win)

    jeg2 = jeg.clone()
    jeg2.move(70, 0)
    jeg2.draw(win)

    jeg3 = jeg.clone()
    jeg3.move(140, 0)
    jeg3.draw(win)

    jeg4 = jeg.clone()
    jeg4.move(210, 0)
    jeg4.draw(win)

    jeg4 = jeg.clone()
    jeg4.move(290, 0)
    jeg4.draw(win)

    # lego2
    lego2 = lego1.clone()
    lego2.move(420, 0)
    lego2.setFill("Green")
    lego2.draw(win)

    # lego3
    lego3 = lego1.clone() + jeg + jeg2 + jeg3 + jeg4.clone()

    lego3 = lego1.clone()
    lego3.move(420, 50)
    lego3.setFill("Green")
    lego3.draw(win)
    # lego4

    # lego5

    # lego6

    input()


main()
