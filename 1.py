from tkinter import *
from tkinter.ttk import *

entry = None
severity_health_level = {
	'normal' : 100,
	'mild' : 80,
	'moderate' : 60,
	'severe' : 40,
	'emergency' : 20
}
Body_Temperature = {
		'normal' : (36, 38),
		'mild' : (35, 39),
		'moderate' : (33, 41),
		'severe' : (30, 44),
		'emergency' : (-100, 100)
}

def calculate_health():
	value = int(entry.get())
	for level in Body_Temperature:
		low, high = Body_Temperature[level]
		if low < value <= high: # if temperature in level normal, mild, etc
			health = severity_health_level[level]
			progress_bar['value'] = health
			break


root = Tk()

Label(root, width=20, text='Body_Temperature').pack(side=LEFT)
entry = Entry(root)
progress_bar = Progressbar(root)
progress_bar.pack(side=RIGHT)
entry.pack(fill=X)

Button(root, text='Calculate', command=calculate_health).pack()

root.mainloop()