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

    """creating the top parts im calling them jegs"""

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

    jeg5 = jeg.clone()
    jeg5.move(290, 0)
    jeg5.draw(win)

    """new peice green"""

    # lego2
    lego2 = lego1.clone()
    lego2.move(420, 0)
    lego2.setFill("Green")
    lego2.draw(win)

    jeg11 = Rectangle(Point(450, 30), Point(495, 50))
    jeg11.setFill("green")
    jeg11.setOutline("black")
    jeg11.setWidth(6)
    jeg11.draw(win)

    jeg22 = jeg11.clone()
    jeg22.move(70, 0)
    jeg22.draw(win)

    jeg33 = jeg11.clone()
    jeg33.move(140, 0)
    jeg33.draw(win)

    jeg44 = jeg11.clone()
    jeg44.move(210, 0)
    jeg44.draw(win)

    jeg55 = jeg11.clone()
    jeg55.move(290, 0)
    jeg55.draw(win)

    # lego3
    lego3 = lego1.clone()
    lego3.move(0, 220)
    lego3.setFill("yellow")
    lego3.draw(win)

    jegy = Rectangle(Point(25, 250), Point(70, 270))
    jegy.setFill("yellow")
    jegy.setOutline("black")
    jegy.setWidth(6)
    jegy.draw(win)

    jegy2 = jegy.clone()
    jegy2.move(70, 0)
    jegy2.draw(win)

    jegy3 = jegy.clone()
    jegy3.move(140, 0)
    jegy3.draw(win)

    jegy4 = jegy.clone()
    jegy4.move(210, 0)
    jegy4.draw(win)

    jegy5 = jegy.clone()
    jegy5.move(290, 0)
    jegy5.draw(win)

    # lego4
    lego4 = lego1.clone()
    lego4.move(420, 220)
    lego4.setFill("red")
    lego4.draw(win)

    jegr = Rectangle(Point(450, 250), Point(495, 270))
    jegr.setFill("red")
    jegr.setOutline("black")
    jegr.setWidth(6)
    jegr.draw(win)

    jegr2 = jegr.clone()
    jegr2.move(70, 0)
    jegr2.draw(win)

    jegr3 = jegr.clone()
    jegr3.move(140, 0)
    jegr3.draw(win)

    jegr4 = jegr.clone()
    jegr4.move(210, 0)
    jegr4.draw(win)

    jegr5 = jegr.clone()
    jegr5.move(290, 0)
    jegr5.draw(win)

    # lego5
    lego4 = lego1.clone()
    lego4.move(0, 410)
    lego4.setFill(color_rgb(0, 204, 200))
    lego4.draw(win)

    jegl = Rectangle(Point(25, 440), Point(70, 460))
    jegl.setFill(color_rgb(0, 204, 200))
    jegl.setOutline("black")
    jegl.setWidth(6)
    jegl.draw(win)

    jegl2 = jegl.clone()
    jegl2.move(70, 0)
    jegl2.draw(win)

    jegl3 = jegl.clone()
    jegl3.move(140, 0)
    jegl3.draw(win)

    jegl4 = jegl.clone()
    jegl4.move(210, 0)
    jegl4.draw(win)

    jegl5 = jegl.clone()
    jegl5.move(290, 0)
    jegl5.draw(win)

    # lego6
    lego4 = lego1.clone()
    lego4.move(420, 410)
    lego4.setFill("black")
    lego4.draw(win)

    jegb = Rectangle(Point(450, 440), Point(495, 460))
    jegb.setFill("black")
    jegb.setOutline("black")
    jegb.setWidth(6)
    jegb.draw(win)

    jegb2 = jegb.clone()
    jegb2.move(70, 0)
    jegb2.draw(win)

    jegb3 = jegb.clone()
    jegb3.move(140, 0)
    jegb3.draw(win)

    jegb4 = jegb.clone()
    jegb4.move(210, 0)
    jegb4.draw(win)

    jegb5 = jegb.clone()
    jegb5.move(290, 0)
    jegb5.draw(win)

    input()


main()
