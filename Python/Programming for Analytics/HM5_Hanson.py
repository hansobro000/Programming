# HM5_Hanson

#%%
# Chapter 4 problem 2

# This program draws an archery target.

from graphics import *

win = GraphWin("Archery Target", 500, 500)
win.setCoords(0.0,0.0,10.0,10.0)

win.setBackground("light sky blue")
ground = Rectangle(Point(0,0), Point(10,3))
ground.setFill("burlywood")
ground.setOutline("burlywood")
ground.draw(win)
stand = Rectangle(Point(3,2.25), Point(7,5))
stand.setFill("peru")
stand.setOutline("saddle brown")
stand.draw(win)
stand2 = Polygon(Point(7,2.25), Point(7,5), Point(7.25,2.5))
stand2.setFill("peru")
stand2.setOutline("saddle brown")
stand2.draw(win)
wCircle = Circle(Point(5,5), 2.5)
wCircle.setFill("white")
wCircle.draw(win)
bkCircle = Circle(Point(5,5), 2)
bkCircle.setFill("black")
bkCircle.draw(win)
blCircle = Circle(Point(5,5), 1.5)
blCircle.setFill("blue")
blCircle.draw(win)
rCircle = Circle(Point(5,5), 1)
rCircle.setFill("red")
rCircle.draw(win)
yCircle = Circle(Point(5,5), 0.5)
yCircle.setFill("yellow")
yCircle.draw(win)

#good

#%%

# Chapter 4 problem 3

# This program draws a face.

from graphics import *

win = GraphWin("Face", 500, 500)
win.setCoords(0.0,0.0,10.0,10.0)

win.setBackground("light sky blue")
ears = Oval(Point(3.3,4.7), Point(3.7,5.3))
ears.setFill("sandy brown")
ears.setOutline("saddle brown")
ears.draw(win)
ear2 = ears.clone()
ear2.move(3,0)
ear2.draw(win)
head = Oval(Point(3.5,3), Point(6.5,7))
head.setFill("sandy brown")
head.setOutline("saddle brown")
head.draw(win)
eye = Circle(Point(4.25,5), 0.5)
eye.setFill("white")
eye.setWidth(3)
eye.draw(win)
eye2 = eye.clone()
eye2.move(1.5,0)
eye2.draw(win)
mouth = Line(Point(4.75,3.5), Point(5.25,3.5))
mouth.draw(win)


# good

#%%

# Chapter 10 problem 3

# "Three Button Monte"
# This program promts user to guess which door is the magic door by clicking
# on any of the three door buttons. If correct, the user will be congradulated
# for winning. If incorrect, they will be told that they lost and what the
# winning door was. 
# Press the Quit button at any time to quit.

from random import *
from graphics import *
from button import Button

def start():
    
    # create the application window
    win = GraphWin("Monte", 500,500)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("olive")
    
    # create buttons and title
    door1 = Button(win, Point(2,5), 2, 1, "Door 1")
    door2 = Button(win, Point(5,5), 2, 1, "Door 2")
    door3 = Button(win, Point(8,5), 2, 1, "Door 3")
    quitButton = Button(win, Point(5,1), 2, 1, "Quit")
    title = Text(Point(5,8), "Click to guess the correct door to win")
    
    # Set all doors to active to start
    door1.activate()
    door2.activate()
    door3.activate()
    quitButton.activate()
    
    title.draw(win)
    
    return win, door1, door2, door3, quitButton, title

def choose(win, door1, door2, door3, quitButton):
    
    #Randomly pick a value 1-3 and return if the right door was clicked upon
    pick = randrange(1,4)
    pt = win.getMouse()
    guess = 0
    end = False
    while True:
        if quitButton.clicked(pt):
            end = True
            break
        if door1.clicked(pt):
            guess = 1
            break
        if door2.clicked(pt):
            guess = 2
            break
        if door3.clicked(pt):
            guess = 3
            break
        pt = win.getMouse()
    if guess == pick:
        return True, end, pick, guess
    else:
        return False, end, pick, guess

def main():
    win, door1, door2, door3, quitButton, title = start()
    end = False
    
    # Update the title to reflect the results of the game
    while not end:
        result, end, pick, guess = choose(win, door1, door2, door3, quitButton)
        
        if guess == pick:
            title.setText("Correct! You won!")
        else:
            title.setText("Wrong, you lost. The correct door was #{0:0.0f}".format(pick))
    
    
    win.close()

if __name__ == '__main__': main()

# good

#%%

