import tkinter
from random import randint

window = tkinter.Tk()
window.minsize(550,550)
label = tkinter.Label(window, text="Score: 0")
label.place(x=0, y=0)
counter = 0

seconds = 30
label2 = tkinter.Label(window, text="Timer: %s" % seconds)
label2.place(x=0, y=20)

labelNews = tkinter.Label(window, text = "Log")

button = tkinter.Button(window, text="Start")
button.place(x=75, y=5)

buttonRules = tkinter.Button(window, text="Rules")
buttonRules.place(x=125, y=5)

labelRules = tkinter.Label(window, text ="There are 5 different buttons: \n1 - You get 5 Points\n2 - You lose 5 Points\n3 - You get 5 seconds\n4 - You lose 5 seconds\n5 - You dont lose or get anything\n - Get as many points as you can before the time runs out!")


def onClickClose():
    global buttonRules
    global labelRules
    global button2
    labelRules.pack_forget()
    button2.destroy()
    buttonRules.place(x=125, y=5)
def onClickRules():
    global buttonRules
    global labelRules
    global button2
    labelRules.pack()
    button2 = tkinter.Button(window, text="Close")
    button2.pack()
    button2.configure(command = onClickClose)
    buttonRules.place_forget()
buttonRules.configure(command = onClickRules)
def onClick():
    global counter
    global label
    global button
    global buttonBait
    global buttonAdd
    global onClickAdd
    global buttonRules
    labelNews.pack()
    a = randint(75, 500)
    b = randint(5, 500)
    c = randint(0, 15)
    d = randint(0, 15)
    e = randint(0, 500)
    f = randint(0, 500)
    buttonRules.place_forget()
    if button["text"] == "Start":
        button.after(1000, onTimer)
        button["text"] = "Click"
    counter += 1
    label["text"] = "Score: %s" % counter
    button.place(x=a, y=b)
    if c and d == 1:
        buttonAddScore = tkinter.Button(window, text = "Bonus!")
        buttonAddScore.place(x=e, y=f)
        def buttonBonusAddScore():
            labelNews.config(text = "You get 5 Points !")
            global counter
            buttonAddScore.place_forget()
            counter += 5
            if buttonAddScore["text"] == "Bonus!":
                buttonAddScore["text"] = "+ 5 Points!"
        buttonAddScore.configure(command = buttonBonusAddScore)
    elif c and d == 2:
        buttonRemoveScore = tkinter.Button(window, text = "Click")
        buttonRemoveScore.place(x=e, y=f)
        def buttonBonusRemoveScore():
            labelNews.config(text = "You lose 5 Points !")
            global counter
            buttonRemoveScore.place_forget()
            counter -= 5
            if buttonRemoveScore["text"] == "Click":
                buttonRemoveScore["text"] = "- 5 Points!"
        buttonRemoveScore.configure(command = buttonBonusRemoveScore)
    elif c and d == 3:
        buttonRemoveTime = tkinter.Button(window, text = "Click")
        buttonRemoveTime.place(x=e, y=f)
        def buttonBonusRemoveTime():
            labelNews.config(text = "You lose 5 Seconds !")
            global seconds
            buttonRemoveTime.place_forget()
            seconds -= 5
            if buttonRemoveTime["text"] == "Click":
                buttonRemoveTime["text"] = "- 5 Seconds!"
        buttonRemoveTime.configure(command = buttonBonusRemoveTime)
    elif c and d == 4:
        buttonAddTime = tkinter.Button(window, text = "Bonus!")
        buttonAddTime.place(x=e, y=f)
        def buttonBonusAddTime():
            labelNews.config(text = "You get 5 Seconds !")
            global seconds
            buttonAddTime.place_forget()
            seconds += 5
            if buttonAddTime["text"] == "Bonus!":
                buttonAddTime["text"] = "+ 5 Seconds!"
        buttonAddTime.configure(command = buttonBonusAddTime)
    elif c and d == 5:
        buttonDoNothing = tkinter.Button(window, text = "Click")
        buttonDoNothing.place(x=e, y=f)
        def buttonBonusDoNothing():
            labelNews.config(text = "You got Baited !")
            global seconds
            buttonDoNothing.place_forget()
        buttonDoNothing.configure(command = buttonBonusDoNothing)
        
button.configure(command = onClick)    
def onTimer():
    global label2
    global button
    global seconds
    seconds -= 1
    label2["text"] = "Timer: %s" % seconds
    if seconds <= 0:
        button.place_forget()
        
    else:
        button.after(1000, onTimer)

window.mainloop()

