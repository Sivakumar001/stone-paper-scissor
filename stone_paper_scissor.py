from tkinter import *
from tkinter import ttk
import random
import time

number_of_plays = 0
score_human_ = 0
score_computer_ = 0
_values = ['stone', 'paper', 'scissor']


def score_human():
    global score_human_
    score_human_ += 1


def score_computer():
    global score_computer_
    score_computer_ += 1


def show_score():
    global score_human_
    global score_computer_
    winlabel.config(text=f'the score of you is {score_human_}'
                    f'and computer is {score_computer_}')


def reset_score():
    global score_human_
    global score_computer_
    global number_of_plays
    winlabel.config(text='the score of you and the computer has been reset')
    score_human_ = 0
    score_computer_ = 0
    number_of_plays = 0


def number_of_play():
    global number_of_plays
    winlabel.config(text=f'the total number of plays is {number_of_plays}')


def done():
    global number_of_plays
    number_of_plays += 1
    r = random.choice(_values)
    if r == cmbo.get():
        winlabel.config(text='its a draw')
    elif r == _values[0] and cmbo.get() == _values[1]:
        winlabel.config(text='you win')
        score_human()
    elif r == _values[0] and cmbo.get() == _values[2]:
        winlabel.config(text='you lost')
        score_computer()
    elif r == _values[1] and cmbo.get() == _values[0]:
        winlabel.config(text='you win')
        score_human()
    elif r == _values[1] and cmbo.get() == _values[2]:
        winlabel.config(text='you lost')
        score_computer()
    elif r == _values[2] and cmbo.get() == _values[0]:
        winlabel.config(text='you win')
        score_human()
    elif r == _values[2] and cmbo.get() == _values[1]:
        winlabel.config(text='you lost')
        score_computer()
    time.sleep(0.5)


main = Tk()
main.title('Stone Paper Scissor')
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
Button(main, text='score', activebackground='green', command=show_score).pack()
Button(main, text='reset',
       activebackground='green', command=reset_score).pack()
Button(main, text='plays', activebackground='green',
       command=number_of_play).pack()
winlabel.pack()
main.mainloop()
