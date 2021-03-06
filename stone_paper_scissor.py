from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import random


_values = ['stone', 'paper', 'scissor']
cmpoints = 0
playpoints = 0

# should have used classes fml


def setnew():
    global cmpoints, playpoints
    playerscorelabel.config(text="player score")
    compscorelabel.config(text="computer score")
    cmpoints, playpoints = (0, 0)


def done():
    global cmpoints, playpoints
    r = random.choice(_values)
    c = cmbo.get()
    if r == _values[0]:
        compimglabel.config(image=stoneimg)
    if r == _values[1]:
        compimglabel.config(image=paperimg)
    if r == _values[2]:
        compimglabel.config(image=scissorimg)
    if c == _values[0]:
        playerimglabel.config(image=stoneimg)
    if c == _values[1]:
        playerimglabel.config(image=paperimg)
    if c == _values[2]:
        playerimglabel.config(image=scissorimg)
    if r == c:
        winlabel.config(text='its a draw')
    elif r == _values[0] and c == _values[1]:
        winlabel.config(text='you win')
        playpoints = playpoints + 1
    elif r == _values[0] and c == _values[2]:
        winlabel.config(text='you lost')
        cmpoints = cmpoints + 1
    elif r == _values[1] and c == _values[0]:
        winlabel.config(text='you lost')
        cmpoints = cmpoints + 1
    elif r == _values[1] and c == _values[2]:
        winlabel.config(text='you win')
        playpoints = playpoints + 1
    elif r == _values[2] and c == _values[0]:
        winlabel.config(text='you win')
        playpoints = playpoints + 1
    elif r == _values[2] and c == _values[1]:
        winlabel.config(text='you lost')
        cmpoints = cmpoints + 1
    playerscorelabel.config(text=f'player:{playpoints}',
                            font='arial 14', bg='light grey')
    compscorelabel.config(text=f'computer:{cmpoints}',
                          font='arial 14', bg='light grey')


# window screen
main = Tk()
main.title('Stone Paper Scissors')
main.config(bg='light grey')
iconpicture = ImageTk.PhotoImage(file='resources/jankenponicon.png')
main.iconphoto(False, iconpicture)
main.geometry('500x500')
main.resizable(0, 0)

# labelling values
Label(main, text='Stone Paper Scissors', fg='blue',
      bg='light grey', font='timesnewroman 18 bold').pack()
Label(main, text='enter your choice', bg='light grey').pack()
winlabel = Label(main, bg='light grey', font='arial 18')
playerscorelabel = Label(main, text='player score',
                         font='arial 14', bg='light grey')
compscorelabel = Label(main, text='computer score',
                       font='arial 14', bg='light grey')
# options
# option commands
playerimglabel = Label(main, bg='light grey')
compimglabel = Label(main, bg='light grey')

stoneimg = Image.open('resources/stone.jpg')
stoneimg = stoneimg.resize((150, 150))
stoneimg = ImageTk.PhotoImage(stoneimg)

paperimg = Image.open('resources/paper.jpg')
paperimg = paperimg.resize((150, 150))
paperimg = ImageTk.PhotoImage(paperimg)

scissorimg = Image.open('resources/scissors.jpg')
scissorimg = scissorimg.resize((150, 150))
scissorimg = ImageTk.PhotoImage(scissorimg)

cmbo = ttk.Combobox(main, state='readonly',
                    values=['stone',
                            'paper',
                            'scissor'])
cmbo.current(0)
cmbo.place(x=190, y=60)
# button
Button(main, width=10, height=2, text='ok',
       activebackground='green', command=done).place(x=210, y=100)
Button(main, width=10, text='reset',
       activebackground='red',
       command=setnew).place(x=210, y=355)

playerimglabel.place(x=50, y=150)
compimglabel.place(x=300, y=150)
winlabel.place(x=200, y=400)
playerscorelabel.place(x=80, y=450)
compscorelabel.place(x=290, y=450)
main.mainloop()
