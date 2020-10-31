from tkinter import*
root = Tk()

equal = ""

# want the text to update this helps do that
equation = StringVar()
#when equation updates with StringVar, update the calcualtion
calculation = Label(root, textvariable=equation)
calculation.grid(columnspan=5)

equation.set("Enter your equation:")

def buttonPress(num):
    global equal
    equal = equal + str(num)
    equation.set(equal)

def equalPress():
    global equal
    total_sum = str(eval(equal))
    equation.set(total_sum)
    equal = ""



def clearPress():
    global equal
    equal=""
    equation.set("")

Button9 = Button(root,text="9",command=lambda:buttonPress(9), height = 2, width = 3)
Button9.grid(row=1, column=2, padx=3, pady=3)

Button8 = Button(root,text="8",command=lambda:buttonPress(8), height = 2, width = 3)
Button8.grid(row=1, column=1, padx=3, pady=3)

Button7 = Button(root,text="7",command=lambda:buttonPress(7), height = 2, width = 3)
Button7.grid(row=1, column=0, padx=3, pady=3)

Addition = Button(root,text="+",command=lambda:buttonPress("+"), height = 2, width = 3)
Addition.grid(row=1, column=3, padx=3, pady=3)

Button6 = Button(root,text="6",command=lambda:buttonPress(6), height = 2, width = 3)
Button6.grid(row=2, column=2, padx=3, pady=3)

Button5 = Button(root,text="5",command=lambda:buttonPress(5), height = 2, width = 3)
Button5.grid(row=2, column=1, padx=3, pady=3)

Button4 = Button(root,text="4",command=lambda:buttonPress(4), height = 2, width = 3)
Button4.grid(row=2, column=0, padx=3, pady=3)

Multiply = Button(root,text="*",command=lambda:buttonPress("*"), height = 2, width = 3)
Multiply.grid(row=2, column=3, padx=3, pady=3)

Button3 = Button(root,text="3",command=lambda:buttonPress(3), height = 2, width = 3)
Button3.grid(row=3, column=2, padx=3, pady=3)

Button2 = Button(root,text="2",command=lambda:buttonPress(2), height = 2, width = 3)
Button2.grid(row=3, column=1, padx=3, pady=3)

Button1 = Button(root,text="1",command=lambda:buttonPress(1), height = 2, width = 3)
Button1.grid(row=3, column=0, padx=3, pady=3)

Subtract = Button(root,text="-",command=lambda:buttonPress("-"), height = 2, width = 3)
Subtract.grid(row=3, column=3, padx=3, pady=3)


Button0 = Button(root,text="0",command=lambda:buttonPress(0), height = 2, width = 3)
Button0.grid(row=4, column=1, pady=3)


Divide = Button(root,text="/",command=lambda:buttonPress("/"), height = 2, width = 3)
Divide.grid(row=4, column=3, pady=3)

ButtonEqual = Button(root,text="=", command=equalPress, bg="grey", height = 2, width = 3)
ButtonEqual.grid(row=4, column=2, pady=3)

ButtonClear = Button(root,text="C", command=clearPress, bg="grey", height = 2, width = 3)
ButtonClear.grid(row=4, column=0, pady=3)

root.mainloop()
