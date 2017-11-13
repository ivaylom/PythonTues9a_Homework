import tkinter
import random

def randcolor():
    s=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    res='#'
    for i in range(6):
        res=res+random.choice(s)
    return res

window = tkinter.Tk()
window.minsize(550,460)
buttons=[None]*16
label = tkinter.Label(window, text="Score: 0")
label.place(x=0, y=0)
counter = 0
different=0
main_color=0
diff_color=0

seconds = 30
label2 = tkinter.Label(window, text="Timer: %s" % seconds)
label2.place(x=0, y=20)

def genbut():
    global different
    global main_color
    global diff_color
    different=random.randint(0,15)
    main_color=randcolor()
    diff_color=randcolor()

    n=0
    for i in range(4):
        for j in range(4):
            buttons[n] = tkinter.Button(window, width=10, height=10, bg = main_color)
            buttons[n].place(x=50 + i * 100, y=50 +j * 100)
            if n==different:
                buttons[n]["bg"] = diff_color
            n=n+1

genbut()

def onClickmain():
    global counter
    global label
    global buttons
    buttons[0].after(1000, onTimer)

def onClickdiff():
    global counter
    global label
    global button
    buttons[0].after(1000, onTimer)
    counter += 1
    label["text"] = "Score: %s" % counter
    genbut()
    for i in range(16):
        buttons[i].configure(command = onClickmain)
    buttons[different].configure(command=onClickdiff)

for i in range(16):
    buttons[i].configure(command = onClickmain)
buttons[different].configure(command=onClickdiff)

def onTimer():
    global label2
    global buttons
    global seconds
    seconds -= 1
    label2["text"] = "Timer: %s" % seconds
    if seconds <= 0:
        for i in range(16):
            buttons[i].config(state='disabled')
    else:
        buttons[0].after(1000, onTimer)

window.mainloop()
