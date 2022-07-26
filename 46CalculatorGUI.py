from ast import Expression, Lambda
from re import A
import tkinter
from tkinter import *

root = tkinter.Tk()
root.title('Calculator')
equation = StringVar()

digital = tkinter.Entry(root, width = 55, borderwidth = 9, textvariable= equation)
digital.grid(row = 0, column = 0, columnspan= 5, padx = 15, pady = 15)

expression = ''

def button_click(number):
    global expression
    expression = expression + str(number)
    equation.set(expression)

def button_equall():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ''
    except:
        equation.set(' ')
        expression = ''

def button_delete():
    global expression
    expression = ''
    equation.set('')

def button_backspacee():
    return
        
button_1 = tkinter.Button(root, text= '1', font= 40, padx=40, pady=20, command= lambda: button_click(1), borderwidth=4)
button_2 = tkinter.Button(root, text= '2', font= 40, padx=40, pady=20, command= lambda: button_click(2), borderwidth=4)
button_3 = tkinter.Button(root, text= '3', font= 40, padx=40, pady=20, command= lambda: button_click(3), borderwidth=4)
button_4 = tkinter.Button(root, text= '4', font= 40, padx=40, pady=20, command= lambda: button_click(4), borderwidth=4)
button_5 = tkinter.Button(root, text= '5', font= 40, padx=40, pady=20, command= lambda: button_click(5), borderwidth=4)
button_6 = tkinter.Button(root, text= '6', font= 40, padx=40, pady=20, command= lambda: button_click(6), borderwidth=4)
button_7 = tkinter.Button(root, text= '7', font= 40, padx=40, pady=20, command= lambda: button_click(7), borderwidth=4)
button_8 = tkinter.Button(root, text= '8', font= 40, padx=40, pady=20, command= lambda: button_click(8), borderwidth=4)
button_9 = tkinter.Button(root, text= '9', font= 40, padx=40, pady=20, command= lambda: button_click(9), borderwidth=4)
button_0 = tkinter.Button(root, text= '0', font= 40, padx=40, pady=20, command= lambda: button_click(0), borderwidth=4)
button_plus = tkinter.Button(root, text= '+', font= 40, padx=39, pady=20, command=lambda: button_click('+'), borderwidth=4)
button_minus = tkinter.Button(root, text= '-', font= 40, padx=39, pady=20, command=lambda: button_click('-'), borderwidth=4)
button_multiply = tkinter.Button(root, text= '*', font= 40, padx=40, pady=20, command= lambda: button_click('*'), borderwidth=4)
button_divide = tkinter.Button(root, text= '/', font= 40, padx=40, pady=20, command= lambda: button_click('/'), borderwidth=4)
button_equal = tkinter.Button(root, text= '=', font= 40, padx=40, pady=20, command= button_equall, borderwidth=4)
button_comma = tkinter.Button(root, text= ',', font= 40, padx=40, pady=20, command= lambda: button_click('.'), borderwidth=4)
button_clear = tkinter.Button(root, text= 'C', font= 40, padx=40, pady=20, command=button_delete, borderwidth=4)
button_backspace = tkinter.Button(root, text= 'Back', font= 40, padx=30, pady=20, command=button_backspacee, borderwidth=4)

button_1.grid(row= 4, column= 1)
button_2.grid(row= 4, column= 2)
button_3.grid(row= 4, column= 3)
button_4.grid(row= 3, column= 1)
button_5.grid(row= 3, column= 2)
button_6.grid(row= 3, column= 3)
button_7.grid(row= 2, column= 1)
button_8.grid(row= 2, column= 2)
button_9.grid(row= 2, column= 3)
button_0.grid(row= 5, column= 2)
button_plus.grid(row= 2, column= 4)
button_minus.grid(row= 3, column= 4)
button_multiply.grid(row= 1, column= 4)
button_divide.grid(row= 1, column= 3)
button_equal.grid(row= 4, column= 4)
button_comma.grid(row= 5, column= 3)
button_clear.grid(row= 1, column= 1)
button_backspace.grid(row= 1, column= 2)

root.mainloop()