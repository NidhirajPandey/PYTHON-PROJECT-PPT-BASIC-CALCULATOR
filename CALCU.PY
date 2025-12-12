# Source - https://stackoverflow.com/q
# Posted by Matias Salgo, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-24, License - CC BY-SA 4.0

from tkinter import *
import tkinter as tk
import math

expression = ""

inverted = False

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression
        total = eval(expression)
        equation.set(total)
        expression = str(total)

    except:
        equation.set(" Error ")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")
    return



if __name__ == "__main__":
    gui = Tk()

    gui.configure(background="green")

    gui.title("MyCalculator")

    gui.geometry("400x220")

    equation = StringVar()
    A = StringVar()
    B = StringVar()

    expression_field = Entry(gui, textvariable=equation)

    expression_field.grid(columnspan=65, ipadx=300)

    equation.set('Enter Your Expression')


    button1 = Button(gui, text="1",font=("Ariel",10,"bold"),bd=6,height=2,width=6,command=lambda: press("1"))
    button1.grid(row=4, column=0)

    button2 = Button(gui, text="2",font=("Ariel",10,"bold"),bd=6,height=2,width=6,command=lambda: press("2"))
    button2.grid(row=4, column=1)

    button3 = Button(gui, text="3",font=("Ariel",10,"bold"),bd=6,height=2,width=6,command=lambda: press("3"))
    button3.grid(row=4, column=2)

    button4 = Button(gui, text="4",font=("Ariel",10,"bold"),bd=6,height=2,width=6,command=lambda: press("4"))
    button4.grid(row=3, column=0)

    button5 = Button(gui, text="5",font=("Ariel",10,"bold"),bd=6,height=2,width=6,command=lambda: press("5"))
    button5.grid(row=3, column=1)

    button6 = Button(gui, text="6",font=("Ariel",10,"bold"),bd=6,height=2,width=6,command=lambda: press("6"))
    button6.grid(row=3, column=2)

    button7 = Button(gui, text="7",font=("Ariel",10,"bold"),bd=6,height=2,width=6,command=lambda: press("7"))
    button7.grid(row=2, column=0)

    button8 = Button(gui, text="8",font=("Ariel",10,"bold"),bd=6,height=2,width=6,command=lambda: press("8"))
    button8.grid(row=2, column=1)

    button9 = Button(gui, text="9",font=("Ariel",10,"bold"),bd=6,height=2,width=6,command=lambda: press("9"))
    button9.grid(row=2, column=2)

    button0 = Button(gui, text="0",font=("Ariel",10,"bold"),bd=6,height=2,width=6,command=lambda: press("0"))
    button0.grid(row=5, column=1)

    plus = Button(gui, text="+",font=("Ariel",10,"bold"),bd=6,height=2,width=6,command=lambda: press("+"))
    plus.grid(row=2, column=3)

    minus = Button(gui,text='-',font=("Ariel",10,"bold"),bd=6,height=2,width=6,command=lambda: press("-"))
    minus.grid(row=3, column=3)

    multiply = Button(gui, text="*",font=("Ariel",10,"bold"),bd=6,height=2,width=6,command=lambda: press("*"))
    multiply.grid(row=4, column=3)

    divide = Button(gui, text="/",font=("Ariel",10,"bold"),bd=6,height=2,width=6,command=lambda: press("/"))
    divide.grid(row=5, column=3)

    equalpress = Button(gui, text="=",font=("Ariel",10,"bold"),bd=6,height=2,width=6,command= equalpress)
    equalpress.grid(row=5, column=2)

    clear = Button(gui, text="clear",font=("Ariel",10,"bold"),bd=6,height=2,width=6,command=clear)
    clear.grid(row=2, column=6)

    dec = Button(gui, text=".",font=("Ariel",10,"bold"),bd=6,height=2,width=6,command=lambda: press("."))
    dec.grid(row=5, column=0)

   
gui.mainloop()
