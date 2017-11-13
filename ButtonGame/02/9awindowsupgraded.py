import tkinter
import random

# settings
initial_seconds = 5
wait_between_games = 2000
wait_between_games_highscore = 4500

def initialClick():
	global score
	score = 1
	updateScores()
	button_main.place(x=random.randint(0, 500), y=random.randint(0, 500))
	label_timer.after(1000, onTimer)
	button_main.config(text="Click", command=onClick)

def onClick():
	global score
	score += 1
	updateScores()
	button_main.place(x=random.randint(0, 500), y=random.randint(0, 500))

def onTimer():
	global seconds
	global highscore
	seconds -= 1
	updateScores()
	if seconds > 0:
		label_timer.after(1000, onTimer)
	else:
		button_main.config(state='disabled', text="Time's up!")
		button_main.place(x=250, y=250)
		waiting = wait_between_games
		if score > highscore:
			button_main.config(text="Time's up! (NEW HIGH SCORE! %s -> %s)" % (highscore, score))
			waiting = wait_between_games_highscore
		highscore = max(highscore, score)
		seconds = initial_seconds
		updateScores()
		label_timer.after(waiting, lambda:button_main.config(text="Try again?", state='active', command=initialClick))

def updateScores():
	label_highscore.config(text="Highscore: %s" % highscore)
	label_score.config(text="Score: %s" % score)
	label_timer.config(text="Timer: %s" % seconds)

# creation of objects
window = tkinter.Tk()
window.minsize(550,550)
highscore = 0
label_highscore = tkinter.Label(window, text="Highscore: %s" % highscore)
score = 0
label_score = tkinter.Label(window, text="Score: %s" % score)
seconds = initial_seconds
label_timer = tkinter.Label(window, text="Timer: %s" % seconds)
button_main = tkinter.Button(window, text="Start", command=initialClick)

# positioning objects
label_score.place(x=0, y=0)
label_timer.place(x=0, y=20)
label_highscore.place(x=0, y=40)
button_main.place(x=100, y=100)
window.mainloop()
