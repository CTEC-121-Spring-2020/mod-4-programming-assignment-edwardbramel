# Module 5
#   Programming Assignment 6
#       Prob-1.py

# Edward LaManna

# INSTRUCTIONS:
#   Insert a comment above each line of code in the program below to describe
#   what the code does


from graphics import *


def main():
    # the win=graph makes a tabe open when you run the program and tells the computer hey were making a graph
    win = GraphWin()
    # the shape=circ lets the computer know that the circle should be at x,y on the graph with a radious of 20
    shape = Circle(Point(50, 50), 20)
    # .setoutline give the circle an outline of red
    shape.setOutline("red")
    # .setfill makes the inside of the circle red
    shape.setFill("red")
    # finally telling the computer to plot the previous varibles
    shape.draw(win)
    # giving i a range of 5 comming back to this i can click 5 times before the window shuts down
    for i in range(5):
        # .getmouse makes it to were the user can click with there mouse
        p = win.getMouse()
        # grabs the center of the previous circle
        c = shape.getCenter()
        # takes the previous x value and subtracts the new value
        dx = p.getX() - c.getX()
        # takes the y value and subtracts new value
        dy = p.getY() - c.getY()
        # finally moves the to the total new value caluclated were the user clicks
        shape.move(dx, dy)
    # after the computer runs everything it closes out the tab
    win.close()


main()
