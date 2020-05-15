# Module 5
#   Programming Assignment 6
#       Prob-2.py

# <YOUR NAME>

from graphics import *


def main():
    win = GraphWin()
    # added rectangle instead of circle and had to add another point on x,y for the rectangle
    shape = Rectangle(Point(50, 50), Point(120, 120))
    # made it a new color just cause also got rid of outline
    shape.setFill("Blue")
    shape.draw(win)
    for i in range(5):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx, dy)
    win.close()


main()
