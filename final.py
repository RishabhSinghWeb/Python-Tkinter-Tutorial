from tkinter import * # Button, Label, Frame, Entry, Listbox, simpledialog
from tkinter import simpledialog
from tkinter.ttk import * # Progressbar

ID = 0 # starting ID of adding new patients
patients_list = [] # list of all patients
selected_patient = None # is the selected patient of the listbox
entries = {} # all the gui entry health fields
progressbars = {} # all the gui progress bar health fields
fields = ('ID', 'Name', 'Date_of_Birth', 'Blood_Pressure', 'Blood_Sugar', 'Heart_Rate', 'Body_Temperature') # all the fields in gui
severity_health_level = { # precentage of health based on severity
	'normal' : 100,
	'mild' : 80,
	'moderate' : 60,
	'severe' : 40,
	'emergency' : 20
}
health_level = { # severity along with there (minimum, maximum) range
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

class Patient(object): # class Patient is a model of each individual patient, it can be used for all patients
	def __init__(self, Name, Date_of_Birth="", Heart_Rate="72", Blood_Pressure='120', Body_Temperature='37', Blood_Sugar='120', Health='5'): # when adding new patient __init__ function is call. Name, ID, etc are its attributes
		# super(Patient, self).__init__()
		global ID # by default ID on Patient class is different from ID at this application(at line 6), this global keyword make both variable the same i.e. this gets ID from application to this class
		ID+=1 # increment ID value by one, this is same as ID = ID + 1
		self.ID = str(ID)
		self.Name = Name
		self.Date_of_Birth = Date_of_Birth
		self.Heart_Rate = Heart_Rate
		self.Blood_Pressure = Blood_Pressure
		self.Body_Temperature = Body_Temperature
		self.Blood_Sugar = Blood_Sugar
		self.Health = Health
	def __str__(self):
		return str(self.ID) + " " + str(self.Name) + " " + str(self.Health) + "*Health"
		# return f'{self.ID} {self.Name} {self.Health} Health'
	

def calculate_health(entries):
	# values = {
	# 	'Blood_Sugar' : int(entries['Blood_Sugar'].get())  # getting values from tkinter gui entries to local variables
	# 	'Blood_Pressure' : int(entries['Blood_Pressure'].get())
	# 	'Heart_Rate' : int(entries['Heart_Rate'].get())
	# 	'Body_Temperature' : int(entries['Body_Temperature'].get())
	# }
	all_health = {}
	for TestName in health_level:
		entry = entries[TestName] # get the gui entry of current TestName
		progressbar = progressbars[TestName] # get the progress bar of current TestName
		str_value = entry.get() # getting string values from tkinter gui entries to local variables
		try: # try to convert string value to integer value, this is error control or Exception Handling
			value = int(str_value) # then convert string value into integer value
		except Exception as e: # if string is not converted into integer then there is a error, then this will run
			entry.delete(0, END) # remove the error value from gui entry
			progressbar['value'] = 0 # remove the value of the gui progressbar
			continue # there is no values for current TestName so skip this iteration of current TestName and continue to next TestName iteration
			# raise "Input Error: " + str_value
		else: # if string value is successfully converted
			Test = health_level[TestName] # get the test ranges of current TestName
			for level in Test: # inner loop for test severity levels like mild, moderate, emergency
				current_level = Test[level] # current severity level
				low, high = current_level[0], current_level[1] # first value is low and second value is high of the range of current severity
				if low < value <= high: # if value is in current range
					health = severity_health_level[level] # get health percentage
					all_health[TestName] = health # save it to dict which have all_health
					progressbar['value'] = health # set value of progress bar
					break # terminate the inner loop since 
			else: # the value is not in any range i.e. the value most likely to be wrong
				entry.delete(0, END) # clear the value from gui entry
				continue # skip to the next 
		# finally: 
		# 	pass
			
	if all_health: # if there is any successfully added test
		minimum_health = min(all_health.values()) # minimum health is the health of the patient
		selected_patient.Health = str(minimum_health) # set it to selected patient in listbox

def onSelect(event): # function for changing/updating patient when patient from listbox is selected
	global selected_patient # to get same global value of this application,
	if selected_patient: # if there is currently selected_patient patient in listbox save it first
		for entry in fields: # every attribute of patient class iterate to save from tkinter entries
			selected_patient.__setattr__(entry,entries[entry].get()) # saving value of each entry to class patient's attributes
	listbox_selections = event.widget.curselection() # event.widget is the listbox, this statement get currently selected_patient patient
	if listbox_selections: # if there any listbox_selection
		patient = listbox_selections[0] # 
		selected_patient = patients_list[patient] # getting patient that is just selected by clicking
		for entry in fields: # showing values of every attribute of just selected class patient to entries in the screen
			value = selected_patient.__getattribute__(entry) # value of the field
			entries[entry].delete(0, END) # clear the value of gui entry
			entries[entry].insert(0, value) # add the new value to gui entry
	calculate_health(entries) # calculate health on selection

def onKeyUp(event): # save values and update listbox whenever keyboard is pressed on entry 
	global selected_patient # to get same global value of this application,
	if selected_patient: # if there is currently selected_patient patient in listbox save it first
		for entry in fields: # every attribute of patient class iterate to save from tkinter entries
			selected_patient.__setattr__(entry,entries[entry].get()) # saving value of each entry to class patient's attributes
	listbox.delete(0, END) # clear all data of listbox
	for patient in patients_list: # one by one
		listbox.insert(END, patient) # add all the patient to listbox

def makeform(root):
	for i,field in enumerate(fields):
		row_frame = Frame(root)
		label = Label(row_frame, width=20, text=field+": ", anchor='w')
		entry = Entry(row_frame)
		if i>=3: # progress fields are added from third field
			# entry.insert(0, "0") # default values are zero
			progress_bar = Progressbar(row_frame, orient=HORIZONTAL, length=100, mode='determinate') # create new progress bar 
			progress_bar.pack(side=RIGHT, expand=True) # add progress bar on to screen
			progressbars[field] = progress_bar # save it to list
		label.pack(side=LEFT) # display lable on the screen
		entry.pack(fill=X, padx=5, pady=5) # display entry on the screen
		row_frame.pack(fill=X, padx=5, pady=5) # display row container frame on the screen
		entry.bind('<KeyRelease>', onKeyUp) # call onKeyUp function whenever keyboard is pressed on entry 
		entries[field] = entry # saving entry to the list
	for entry in fields: # showing values of every attribute of just first/default class patient to entries in the screen
		value = selected_patient.__getattribute__(entry) # value of the field
		entries[entry].delete(0, END) # clear the value of gui entry
		entries[entry].insert(0, value) # add the new value to gui entry
	calculate_health(entries) # calculate health on the start
	return entries # return/send the entries to the calling function/inplace of calling function

def add_patient(entries): # to add new patient to the Listbox
	Name = simpledialog.askstring("New Patient", "Enter Patient Name") # open new window to enter name of new patient
	patient = Patient(Name=Name) # create new patient by class Patient
	patients_list.append(patient) # add patient to patients list
	listbox.insert(END, patient) # insert new patient in the top or Listbox # use 0 to insert in the top or listbox.insert(END, Name) to insert in the end of the list

def del_patient(entries): # to delete patient from the Listbox
	selected_patients = listbox.curselection() # get all the selected_patient patient from the Listbox
	if len(selected_patients) >= 1: # if no. of selected_patient patients is greater than and equals to 1 then there is/are some patients selected_patient in the Listbox
		for selected_patient in selected_patients[::-1]: # iterate through all the selected_patient patients, if delete top entry then whole list shift up, [::-1] this reverse the list to delete from bottom
			listbox.delete(selected_patient) # to delete them one by one from listbox
			patients_list.remove(patients_list[selected_patient]) # also delete from the list
	else: # else no patient is selected_patient in the Listbox
		simpledialog.messagebox.showwarning("Patient Not Selected","Select a Patient in the Listbox to Delete") # show message that no patient is selected_patient which patient to delete

if __name__ == '__main__': # True/runs if class of this file is the main class
	root = Tk() # create a new GUI window (rectangular screen), root is the whole window (tkinter screen)

	frame = Frame(root) # create a new frame inside root, frame is a part of the GUI window
	frame.pack(side = LEFT) # add frame in the left of the screen

	Label(frame, text="	Patients").pack(anchor=W) # add Patients text label at W=west direction
	listbox = Listbox(frame) # create a new Listbox inside frame, can also use listbox = Listbox(frame, selectmode=MULTIPLE) to select multiple patient
	listbox.pack(side=LEFT) # add Listbox at the left of the frame
	listbox.bind('<<ListboxSelect>>', onSelect) # this is a event listener, whenever listbox is selected_patient onSelect function will be called
	patient1 = Patient(Name="", Heart_Rate='110', Body_Temperature='39', Blood_Pressure='120', Blood_Sugar='90') # creates new Patient without name
	listbox.insert(0, patient1) # add first Patient by default
	patients_list.append(patient1) # also add first Patient to patients_list
	selected_patient = patients_list[0] # if application just started and there is no selected_patient then get first created/default patient # get the first created/default patient

	Label(root, text="Patient Details").pack(side=TOP) # create Patient Details text label at top of the screen then add it to the top of the screen
	ents = makeform(root) # call the makeform function to make entries, progressbar,etc in the screen

	add_button = Button(frame, text='Add', command= (lambda e=ents: add_patient(e))) # create Add Button in Frame to add new patient
	add_button.pack(padx=5, pady=5) # add add_button to screen with padding(space inside button) 5 in both x(top-bottom) and y(left-right) direction

	delete_button = Button(frame, text='Delete', command= (lambda e=ents: del_patient(e))) # create Delete Button in Frame to add new patient
	delete_button.pack(padx=5, pady=5) # add delete_button to screen with padding(space inside button) 5 in both x(top-bottom) and y(left-right) direction

	calculate_button = Button(root, text='Calculate', command=(lambda e=ents: calculate_health(e))) # create Calculate Button
	calculate_button.pack(side=LEFT, padx=5, pady=5) # add button calculate_button to screen at left side of the screen with padding 5 

	quit_button = Button(root, text='Quit', command=root.quit) # create button to end the application
	quit_button.pack(side=LEFT, padx=5, pady=5)  # add quit button to screen

	root.mainloop() # runs the tkinter root window