"""

temperature = int(input('Enter your Body Temperature in Celcius: '))

if temperature >= 39:
	print('Your Temperature is High')
elif temperature <= 35:
	print('Your Temperature is Low')
else:
	print('Your Temperature is Normal')

"""

from tkinter import *

def Check():
	temperature = int(entry.get())

	if 36 < temperature < 38:
		label.config(text='Your Temperature is Normal')
	else:
		label.config(text='Your Temperature is Abnormal')

root = Tk()

Label(root, text="Enter Your Body Temperature in Celcius").pack()

entry = Entry(root)
entry.pack()

Button(root, text='Check', command= Check).pack()

label = Label(root)
label.pack()

root.mainloop()
