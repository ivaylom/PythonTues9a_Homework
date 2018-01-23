import tkinter
import random
window = tkinter.Tk()
window.minsize(500,500)

label = tkinter.Label(window, text="Score: 0")
label.place(x=0, y=0)
counter = 0

seconds = 30
label2 = tkinter.Label(window, text="Timer: %s" % seconds)
label2.place(x=0, y=20)


def buttonGenerator():
	global buttons
	buttons = [0 for _ in range(16)]
	for i in range(4):
		for j in range(4):
			buttons[i*4+j] = tkinter.Button(window, width=8, height=4)
			buttons[i*4+j].place(x=50 + i * 100, y=50 +j * 100)
			
	button = buttons[(2, 7, 3, 5)[random.randint(0, 3)]]
	button.config(text="Start", command=lambda: [button.config(text=''), button.after(1000, onTimer), colourClicker()])
#tova s cvetovete e kopirano ot stack overflow ne sum gi izmislil sam !
def colourClicker():
	button = buttons[random.randrange(0, 15)]
	redWrong, greenWrong, blueWrong = [random.randint(0, 255) for _ in range(3)]
	color = '#' + hex(redWrong)[2:4].zfill(2) + hex(greenWrong)[2:4].zfill(2) + hex(blueWrong)[2:4].zfill(2)
	for b in buttons:
		b.config(bg=color, command=mistake)
	redRight, greenRight, blueRight = [i + abs(random.randint(-25, 25)) for i in [redWrong, greenWrong, blueWrong]]
	color = '#' + hex(redRight)[2:4].zfill(2) + hex(greenRight)[2:4].zfill(2) + hex(blueRight)[2:4].zfill(2)
	button.config(bg=color, command=correct)
def mistake():
	global seconds
	seconds -= 1
	label2["text"] = "Timer: %s" % seconds
def correct():
	global counter
	global seconds
	counter += 1
	label2["text"] = "Timer: %s" % seconds
	label["text"] = "Score: %s" % counter
	colourClicker()
def onTimer():
	global seconds
	seconds -= 1
	label2["text"] = "Timer: %s" % seconds
	if seconds <= 0:
		for b in buttons:
			b.config(state="disabled")
	else:
		label2.after(1000, onTimer)
buttonGenerator()
window.mainloop()

