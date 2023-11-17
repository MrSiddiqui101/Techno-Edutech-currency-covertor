from tkinter import font
from currency_converter import CurrencyConverter

import tkinter
from tkinter import *

a = CurrencyConverter()
root = Tk()
root.title("COnvertor By Sahil")
root.geometry("500x360")


def clicked():
  amount = int(e1.get())
  cur1 = e2.get()
  cur2 = e3.get()
  data = a.convert(amount, cur1, cur2)
  l5 = Label(root, text=data, font="times 25 bold").place(x=200, y=290)


l1 = Label(root, text="Currency convertor", font="Times 25 bold").place(x=100,
                                                                        y=30)
l2 = Label(root, text="Enter Amount:", font="Times 18 bold").place(x=50, y=80)

l3 = Label(root, text="Enter Currency:", font="Times 18 bold").place(x=50,
                                                                     y=130)

l4 = Label(root, text="required currency:", font="Times 18 bold").place(x=50,
                                                                        y=180)

B1 = Button(root, text="Submit", command=clicked).place(x=230, y=240)
e1 = Entry(root)
e1.place(x=300, y=90)
e2 = Entry(root)
e2.place(x=300, y=140)
e3=Entry(root)
e3.place(x=300,y=190)
root.mainloop()
