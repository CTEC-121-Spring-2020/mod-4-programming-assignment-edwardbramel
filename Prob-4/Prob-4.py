# Module 5
#   Programming Assignment 6
#       Prob-4.py

# Eddy

from graphics import *


def main():
    # makes the tab open 800,600 big
    win = GraphWin("shapes", 800, 600)
    # draws a rectangle tab

    # get p1
    p1 = win.getMouse()
    # get p2
    p2 = win.getMouse()
    # draw rectangle
    rect = Rectangle(Point(p1.getX(), p1.getY()), Point(p2.getX(), p2.getY()))
    rect.draw(win)

    # door
    p3 = win.getMouse()
    # get p1
    # sidthdoor = (p2x - p1x) // 5
    widthDoor = p2.getX() - p1.getY() // 5
    # halfdoorwidth = widthdoor // 2
    halfdoorwidth = widthDoor // 2

    # pointfill = p1x - halfdoorwidth
    Rec2 = Rectangle(Point(p3.getX() - halfdoorwidth, p1.getY()),
                     Point(p3.getX() + halfdoorwidth, p1.getY()))
    Rec2.draw(win)

    input()


main()
