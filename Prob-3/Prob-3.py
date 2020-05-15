# Module 5
#   Programming Assignment 6
#       Prob-3.py

# eddy
from graphics import *


def main():
    # yellow
    win = GraphWin("shapes", 600, 600)
    circ = Circle(Point(300, 300), 180)
    circ.setFill('gray')
    circ.draw(win)
    # red
    circ = Circle(Point(300, 300), 140)
    circ.setFill('black')
    circ.draw(win)
    # blue
    circ = Circle(Point(300, 300), 110)
    circ.setFill('blue')
    circ.draw(win)
    # black
    circ = Circle(Point(300, 300), 70)
    circ.setFill('red')
    circ.draw(win)
    # white
    circ = Circle(Point(300, 300), 30)
    circ.setFill('yellow')
    circ.draw(win)

    input()


main()

# notes for me
# yellow surrounded by concentric rings of red, blue, black and white
