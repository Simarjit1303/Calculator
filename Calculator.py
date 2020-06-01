import tkinter as tk
from tkinter import *
from tkinter import messagebox

background_colour = '#707371'
button_color = '#18c9c1'

root = tk.Tk()
root.geometry("250x400+300+300")
root.title("Calculator")
root.resizable(0, 0)
root.configure()


data = StringVar()
val = ""
A = 0
operator = ""


# Value Buttons
def btn1_isclicked():
	global val
	val = val + "1"
	data.set(val)

def btn2_isclicked():
	global val
	val = val + "2"	
	data.set(val)

def btn3_isclicked():
	global val
	val = val + "3"	
	data.set(val)	

def btn4_isclicked():
	global val
	val = val + "4"
	data.set(val)

def btn5_isclicked():
	global val
	val = val + "5"	
	data.set(val)

def btn6_isclicked():
	global val
	val = val + "6"	
	data.set(val)	

def btn7_isclicked():
	global val
	val = val + "7"
	data.set(val)

def btn8_isclicked():
	global val
	val = val + "8"	
	data.set(val)

def btn9_isclicked():
	global val
	val = val + "9"	
	data.set(val)	

def btn0_isclicked():
	global val
	val = val + "0"	
	data.set(val)


# Operands	
def btnPlus_isclicked():
	global val, A, operator
	A = int(val)
	operator = "+"
	val = val + "+"
	data.set(val)

def btnMinus_isclicked():
	global val, A, operator
	A = int(val)
	operator = "-"
	val = val + "-"	
	data.set(val)

def btnMulti_isclicked():
	global val, A, operator
	A = int(val)
	operator = "X"
	val = val + "X"
	data.set(val)

def btnDivid_isclicked():
	global val, A, operator
	A = int(val)
	operator = "%"
	val = val + "%"
	data.set(val)
	
def btnClear_isclicked():
	global val, A, operator
	A = 0
	operator = ""
	val = ""
	data.set(val)


# Function for calculating result
def calculate():
	global val
	if operator == "%":
		x = int((val.split("%")[1]))
		if x == 0:
			messagebox.showerror("Error!!, Division by 0 not allowed")
			A = ""
			val = ""
			data.set(val)
	else:
		calc = val

		data.set(str(eval(calc)))





# Visuals
lbl = Label(root, text='Label', font=20, anchor=SE, textvariable = data)
lbl.pack(expand=True, fill='both')

btnrow1 = Frame(root)
btnrow1.pack(expand=True, fill="both")

btnrow2 = Frame(root, bg=background_colour)
btnrow2.pack(expand=True, fill="both")

btnrow3 = Frame(root, bg=background_colour)
btnrow3.pack(expand=True, fill="both")

btnrow4 = Frame(root, bg=background_colour)
btnrow4.pack(expand=True, fill="both")


# Adding Buttons
# First Row
btn1 = Button(btnrow1, text="1", font=20, border=0, bg=background_colour, command=btn1_isclicked)
btn1.pack(side=LEFT, expand=True, fill="both")

btn2 = Button(btnrow1, text="2", font=20, border=0, bg=background_colour, command=btn2_isclicked)
btn2.pack(side=LEFT, expand=True, fill="both")

btn3 = Button(btnrow1, text="3", font=20, border=0, bg=background_colour, command=btn3_isclicked)
btn3.pack(side=LEFT, expand=True, fill="both")

btn4 = Button(btnrow1, text="+", font=20, border=0, bg=background_colour, command=btnPlus_isclicked)
btn4.pack(side=LEFT, expand=True, fill="both")


# Second Row
btn5 = Button(btnrow2, text="4", font=20, border=0, bg=background_colour, command=btn4_isclicked)
btn5.pack(side=LEFT, expand=True, fill="both")

btn6 = Button(btnrow2, text="5", font=20, border=0, bg=background_colour, command=btn5_isclicked)
btn6.pack(side=LEFT, expand=True, fill="both")

btn7 = Button(btnrow2, text="6", font=20, border=0, bg=background_colour, command=btn6_isclicked)
btn7.pack(side=LEFT, expand=True, fill="both")

btn8 = Button(btnrow2, text="-", font=20, border=0, bg=background_colour, command=btnMinus_isclicked)
btn8.pack(side=LEFT, expand=True, fill="both")


# Third Row
btn9 = Button(btnrow3, text="7", font=20, border=0, bg=background_colour, command=btn7_isclicked)
btn9.pack(side=LEFT, expand=True, fill="both")

btn10 = Button(btnrow3, text="8", font=20, border=0, bg=background_colour, command=btn8_isclicked)
btn10.pack(side=LEFT, expand=True, fill="both")

btn11 = Button(btnrow3, text="9", font=20, border=0, bg=background_colour, command=btn9_isclicked)
btn11.pack(side=LEFT, expand=True, fill="both")

btn12 = Button(btnrow3, text="X", font=20, border=0, bg=background_colour, command=btnMulti_isclicked)
btn12.pack(side=LEFT, expand=True, fill="both")


# Fourth Row
btn13 = Button(btnrow4, text="C", font=20, border=0, bg=background_colour, command=btnClear_isclicked)
btn13.pack(side=LEFT, expand=True, fill="both")

btn14 = Button(btnrow4, text="0", font=20, border=0, bg=background_colour, command=btn0_isclicked)
btn14.pack(side=LEFT, expand=True, fill="both")

btn15 = Button(btnrow4, text="=", font=20, border=0, bg=background_colour, command=calculate)
btn15.pack(side=LEFT, expand=True, fill="both")

btn16 = Button(btnrow4, text="%", font=20, border=0, bg=background_colour, command=btnDivid_isclicked)
btn16.pack(side=LEFT, expand=True, fill="both")



root.mainloop()