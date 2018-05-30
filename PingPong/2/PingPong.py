from tkinter import *
from random import randint
from math import sqrt
t = Tk()

h = 600
w = 600
r = 40
barW = 30
barH = 100
barOffset = 30
barSpeed = 5
vectorX = -0.2
vectorY = 0.1
score = 0
isUp = False
isDown = False
c = Canvas(t, width=w, height=h)
c.pack()

dot = c.create_oval((w-r)/2, (h-r)/2, (w+r)/2, (h+r)/2, fill="blue")
bar = c.create_rectangle(barOffset, (h-barH)/2, barOffset + barW, (h+barH) / 2, fill = "red")
text = c.create_text(w/2, h-20, text="Score: 0", font=('Times', 30))

isRunning = False
def startIfNot():
    global isRunning
    if not(isRunning):
        isRunning = True
        t.after(10, onTimer)

def isCollide(side):
    global dot
    global bar
    global vectorX
    ballCoords = c.coords(dot)
    if side == "up":
        return ballCoords[1] <= 0
    if side == "down":
        return ballCoords[3] >= h
    if side == "right":
        return ballCoords[2] >= w
    if side == "left":
        return ballCoords[0] <= 0
    if side == "bar":
        barCoords = c.coords(bar)
        #return vectorX < 0 and ballCoords[0] <= barCoords[2] and \
        #       ballCoords[3] >= barCoords[1] and ballCoords[1] <= barCoords[3]

        # Checks if ball is travelling right. Prevents ball going back and forth
        if vectorX >= 0:
            return False
        # Check if ball reached bar. 
        if ballCoords[0] > barW + barOffset:
            return False
        # Check if ball isn't too far above bar
        if ballCoords[3] < barCoords[1]:
            return False
        # Check if ball isn't too far below bar
        if ballCoords[1] > barCoords[3]:
            return False
        ballCenter = center(ballCoords)
        # Check if ball is inside top right corner of bar
        if distance([barCoords[2], barCoords[1]], ballCenter) < r/2:
            return True
        # Check if ball is inside bottom right corner of bar
        if distance([barCoords[2], barCoords[3]], ballCenter) < r/2:
            return True

        # If all of those checks failed, the ball must be somewhere inside the bar or just next to one of the two corners

        # Check if it is next to the top right corner
        if barW + barOffset < ballCoords[0] or barCoords[1] < ballCoords[3]:
            return False
        # Check if it is next to the bottom right corner
        if barW + barOffset < ballCoords[0] or barCoords[3] > ballCoords[1]:
            return False

        # If those two checks failed as well, the ball must be inside the bar
        return True



def center(coords):
    return [(coords[0] + coords[2])/2, (coords[1] + coords[3])/2]

def distance(coords1, coords2):
    return sqrt( \
            ( coords1[0] - coords2[0] )**2 \
            + \
            ( coords1[1] - coords2[1] )**2 \
            )
            
def reflect(side):
    global vectorX
    global vectorY
    if side == "up" or side == "down":
        vectorY *= -1
    if side == "left" or side == "right" or side == "bar":
        vectorX *= -1

def up():
    coords = c.coords(bar)
    if coords[1] > 0:
        c.move(bar, 0, -barSpeed)

def down():
    coords = c.coords(bar)
    if coords[3] < h:
        c.move(bar, 0, barSpeed)

def press(e):
    global isUp
    global isDown
    startIfNot()
    if e.keysym == "Up":
        isUp = True
    if e.keysym == "Down":
        isDown = True

def release(e):
    global isUp
    global isDown
    if e.keysym == "Up":
        isUp = False
    if e.keysym == "Down":
        isDown = False

def incrementScore():
    global text
    global score
    score += 1
    c.itemconfig(text, text="Score: %s" % score)

def endGame():
    global text
    global score
    c.itemconfig(text, text="Game Over!. Score: %s" % score)

def onTimer():
    global isUp
    global isDown
    if isUp:
        up()
    if isDown:
        down()
    c.move(dot, vectorX, vectorY)
    for side in ["up", "down", "right", "bar"]:
        if isCollide(side):
            reflect(side)
            if side == "bar":
                incrementScore()
    if isCollide("left"):
        endGame()
    else:
        t.after(10, onTimer)

t.bind("<KeyPress-Up>", press)
t.bind("<KeyPress-Down>", press)
t.bind("<KeyRelease-Up>", release)
t.bind("<KeyRelease-Down>", release)
t.mainloop()
