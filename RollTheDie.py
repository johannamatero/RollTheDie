### Load modules
from tkinter import *   # to create GUI
import random

### Create and design the window
window = Tk()
window.title('ROLL THE DIE')
window.geometry('200x190')

### Create the die graphics
lbl = Label(window, font=("Courier", 200))
lbl.place(x=50, y=30)

### Define function what to happen when the die is rolled
def roll():
    die_symbol = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    lbl.config(text=f'{random.choice(die_symbol)}', foreground='#B5D2F4')   # randomly choose from above list
    lbl.pack()

    
### Create button
btn = Button(window, text='Roll the die :)', command=roll)  # create button instance
btn.place(x=50, y=7)                                        # place the button

window.mainloop()