#Basic login using tkinter module
from tkinter import *

window=Tk()

#set label for user and passwor
l1=Label(window, text='User:')
l2=Label(window, text='Passwords')

#input
t1=Entry(window, textvariable=StringVar())
t2=Entry(window,show='*', textvariable=StringVar())

#Button
b1=Button(window, text='Log-in')
b2=Button(window, text='Register!')


l1.pack()
t1.pack()
l2.pack()
t2.pack()
b1.pack()
b2.pack()

window.mainloop()
