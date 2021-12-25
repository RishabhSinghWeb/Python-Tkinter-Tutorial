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
health_level = {
	'Body_Temperature' : {
		'normal' : (36, 38),
		'mild' : (35, 39),
		'moderate' : (33, 41),
		'severe' : (30, 44),
		'emergency' : (25, 55)
	},
}

def calculate_health():
	TestName = 'Body_Temperature'
	value = int(entry.get())
	Test = health_level[TestName]
	for level in Test:
		current_level = Test[level]
		if current_level[0] < value <= current_level[1]:
			health = severity_health_level[level]
			progress_bar['value'] = health
			break


root = Tk()

Label(root, text="Patient Details").pack()

row_frame = Frame(root)
Label(row_frame, width=20, text='ID').pack(side=LEFT)
Entry(row_frame).pack(fill=X)
row_frame.pack(fill=X)

row_frame = Frame(root)
Label(row_frame, width=20, text='Name').pack(side=LEFT)
Entry(row_frame).pack(fill=X)
row_frame.pack(fill=X)

row_frame = Frame(root)
Label(row_frame, width=20, text='Body_Temperature').pack(side=LEFT)
entry = Entry(row_frame)
progress_bar = Progressbar(row_frame)
progress_bar.pack(side=RIGHT)
entry.pack(fill=X)
row_frame.pack(fill=X)

Button(root, text='Calculate', command=calculate_health).pack()

root.mainloop()