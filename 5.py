from tkinter import *
from tkinter import simpledialog
from tkinter.ttk import *

ID = 0
patients_list = []
selected_patient = None
entries = {}
progressbars = {}
fields = ('ID', 'Name', 'Date_of_Birth', 'Blood_Pressure', 'Blood_Sugar', 'Heart_Rate', 'Body_Temperature')
severity_health_level = {
	'normal' : 100,
	'mild' : 80,
	'moderate' : 60,
	'severe' : 40,
	'emergency' : 20
}
health_level = {
	'Blood_Pressure' : {
		'normal' : (110, 130),
		'mild' : (100, 140),
		'moderate' : (90, 150),
		'severe' : (80, 160),
		'emergency' : (60, 250)
	},
	'Blood_Sugar' : {
		'normal' : (110, 130),
		'mild' : (100, 140),
		'moderate' : (90, 150),
		'severe' : (80, 160),
		'emergency' : (60, 250)
	},
	'Heart_Rate' : {
		'normal' : (65, 85),
		'mild' : (60, 100),
		'moderate' : (55, 120),
		'severe' : (50, 150),
		'emergency' : (45, 180)
	},
	'Body_Temperature' : {
		'normal' : (36, 38),
		'mild' : (35, 39),
		'moderate' : (33, 41),
		'severe' : (30, 44),
		'emergency' : (25, 55)
	},
}

class Patient(object):
	def __init__(self, Name):
		global ID
		ID+=1
		self.ID = str(ID)
		self.Name = Name
		self.Date_of_Birth = ''
		self.Heart_Rate = ''
		self.Blood_Pressure = ''
		self.Body_Temperature = ''
		self.Blood_Sugar = ''
		self.Health = ''
	def __str__(self):
		return self.Name
	

def calculate_health():
	all_health = {}
	for TestName in health_level:
		entry = entries[TestName]
		try:
			value = int(entry.get())
		except:
			continue
		Test = health_level[TestName]
		for level in Test:
			current_level = Test[level]
			if current_level[0] < value <= current_level[1]:
				health = severity_health_level[level]
				all_health[TestName] = health
				progressbars[TestName]['value'] = health
				break
	selected_patient.Health = str(min(all_health.values()))

patient1 = Patient(Name="")
patients_list.append(patient1)
selected_patient = patients_list[0]

root = Tk()

Label(root, text="Patient Details").pack()

for i,field in enumerate(fields):
	row_frame = Frame(root)
	label = Label(row_frame, width=20, text=field)
	entry = Entry(row_frame)
	if i>=3:
		progress_bar = Progressbar(row_frame)
		progress_bar.pack(side=RIGHT)
		progressbars[field] = progress_bar
	label.pack(side=LEFT)
	entry.pack(fill=X)
	row_frame.pack(fill=X)
	entries[field] = entry

Button(root, text='Calculate', command=calculate_health).pack(side=LEFT)

root.mainloop()