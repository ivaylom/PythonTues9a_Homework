import tkinter as tk
import random
window = tk.Tk()

def start(): # initial setup
	# generate buttons
	global buttons
	buttons = [0 for _ in range(16)]
	for x in range(4):
		for y in range(4):
			buttons[x*4+y] = tk.Button(window, width=4, height=2)
			buttons[x*4+y].place(x=(x*50+5), y=(y*50+5))

	# pass rest of stuff to the main function
	chosen_one = buttons[(5, 6, 9, 10)[random.randint(0, 3)]]
	chosen_one.config(text="Start", command=lambda: [ \
		chosen_one.config(text=''), 
		buttons[0].after(1000, time_tick), 
		buttons[0].config(text=time),
		buttons[15].config(text=score),
		main()])

def main(): # main loop
	# choose a random button
	chosen_one = buttons[random.randrange(1, 14)]
	# generate random button colors
	red, green, blue = [random.randint(0, 255) for _ in range(3)]
	redx, greenx, bluex = [i + abs(random.randint(-25, 25)) for i in [red, green, blue]]

	# configure all wrong buttons
	color = '#' + hex(red)[2:4].zfill(2) + hex(green)[2:4].zfill(2) + hex(blue)[2:4].zfill(2)
	for b in buttons:
		b.config(bg=color, command=wrong_click)
	buttons[0].config(command=lambda:None)
	buttons[15].config(command=lambda:None)

	# configure right button
	color = '#' + hex(redx)[2:4].zfill(2) + hex(greenx)[2:4].zfill(2) + hex(bluex)[2:4].zfill(2)
	chosen_one.config(bg=color, command=right_click)


def wrong_click(): # whenever the player clicks the wrong button
	global time
	time -= 5
	buttons[0].config(text=time)

score = 0
def right_click(): # whenever the player clicks the right button
	global score
	global time
	score += 1
	time = 15
	buttons[0].config(text=time)
	buttons[15].config(text=score)

	main()

time = 15
def time_tick(): # activates every second
	global time
	time -= 1
	buttons[0].config(text=time)
	if time <= 0:
		for b in buttons:
			b.config(state="disabled")
		buttons[5].config(text="Game")
		buttons[9].config(text="Over")
	else:
		buttons[0].after(1000, time_tick)

# starts off the chain reaction
start()
window.mainloop()