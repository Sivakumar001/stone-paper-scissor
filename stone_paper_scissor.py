from tkinter import *
from tkinter import ttk
import random


_values = ['stone', 'paper', 'scissor']


def done():
    r = random.choice(_values)
    if r == cmbo.get():
        winlabel.config(text='its a draw')
    elif r == _values[0] and cmbo.get() == _values[1]:
        winlabel.config(text='you win')
    elif r == _values[0] and cmbo.get() == _values[2]:
        winlabel.config(text='you lost')
    elif r == _values[1] and cmbo.get() == _values[0]:
        winlabel.config(text='you win')
    elif r == _values[1] and cmbo.get() == _values[2]:
        winlabel.config(text='you lost')
    elif r == _values[2] and cmbo.get() == _values[0]:
        winlabel.config(text='you win')
    elif r == _values[2] and cmbo.get() == _values[1]:
        winlabel.config(text='you lost')


main = Tk('stone,paper,scissor')
main.config(bg='light grey')
main.geometry('300x300')


# labelling values
Label(main, text='stone,paper,scissor', fg='blue',
      bg='light grey', font='timesnewroman 14 bold').pack()
Label(main, text='enter your choice', bg='light grey').pack()
winlabel = Label(main, text='your win is declared here', bg='light grey')

# options
# option commands
cmbo = ttk.Combobox(main, state='readonly',
                    values=['stone',
                            'paper',
                            'scissor'])
cmbo.current(0)
cmbo.pack()
# button
Button(main, text='set', activebackground='green', command=done).pack()

winlabel.pack()
main.mainloop()
