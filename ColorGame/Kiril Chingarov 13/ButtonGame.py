import tkinter
import random

window = tkinter.Tk()
window.minsize(550,550)
label = tkinter.Label(window, text="Score: 0")
label.place(x=0, y=0)
counter = 0

seconds = 3
label2 = tkinter.Label(window, text="Timer: %s" % seconds)
label2.place(x=0, y=20)

def onClick():
    global counter
    global label
    global button
    if button["bg"] == "blue":
        button.after(1000, onTimer)
        button["bg"] = "black"
    counter += 1
    label["text"] = "Score: %s" % counter

for i in range(4):
    for j in range(4):
        button = tkinter.Button(window, width=10, height=5, bg = 'blue', command = onClick)
        button.place(x=50 + i * 100, y=50 +j * 100)
        
def onTimer():
    global label2
    global button
    global seconds
    seconds -= 1
    label2["text"] = "Timer: %s" % seconds
    if seconds <= 0:
        button.config(state='disabled')
        tkinter.messagebox.showinfo("Game Over", "Time's up!")
    else:
        button.after(1000, onTimer)

window.mainloop()

