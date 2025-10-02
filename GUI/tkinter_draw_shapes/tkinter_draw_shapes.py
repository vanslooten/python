# tutorial:
# https://home.et.utwente.nl/slootenvanf/2024/04/30/python-drawing-shapes-userinterface/
# 
# drawing shapes:
# https://www.tutorialspoint.com/python/tk_canvas.htm
# https://www.geeksforgeeks.org/python-tkinter-create-different-shapes-using-canvas-class/
# https://tkinterpython.top/drawing/
# 
# changing color:
# https://stackoverflow.com/questions/46288428/changing-the-colour-of-tkinter-rectangles-using-entry-and-button
#
# convert r, g, b values to hex color code:
# https://stackoverflow.com/questions/51591456/can-i-use-rgb-in-tkinter
#
# Bind the Enter key to focus on next Entry widget:
# https://pythonexamples.org/python-tkinter-entry-on-enter-key-focus-next-widget/
#
# For the button, make Return key work as well:
# https://stackoverflow.com/questions/16996432/how-do-i-bind-the-enter-key-to-a-function-in-tkinter

from tkinter import *

window = Tk()
window.title('Draw colored shapes')

def go_to_next_element(event):
    event.widget.tk_focusNext().focus()

def setColor(r, g, b):
    # change color of a shape:
    canvas.itemconfig(rectangle1, fill=f'#{r:02x}{g:02x}{b:02x}') # convert r, g, b values to hex color code

def button_click(event=None):
    # read r, g, b values
    # set the color
    print("button_click()")
    # read r:
    try:
        r = int(entryR.get()) % 256
    except:
        r = 0
    print("r:",r)
    # read g:
    try:
        g = int(entryG.get()) % 256
    except:
        g = 0
    print("g:",g)
    # read b:
    try:
        b = int(entryB.get()) % 256
    except:
        b = 0
    print("b:",b)
    setColor(r, g, b)

canvas = Canvas(window, width=400, height=150)
canvas.pack()

# draw shapes:
# create_rectangle(x0, y0, x1, y1, option, ...)
# horizon:
background1 = canvas.create_rectangle(0, 0, canvas.winfo_reqwidth(), 60, outline = "blue", fill = "blue")
background2 = canvas.create_rectangle(0, 60, canvas.winfo_reqwidth(), canvas.winfo_reqheight(), outline = "blue", fill = "brown")
# more shapes:
rectangle1 = canvas.create_rectangle(230, 70, 300, 120,
                                     outline = "black", fill = "green",
                                     width = 2)
#circle = canvas.create_oval(30, 30, 100, 100, outline = "yellow", fill = "yellow")
sun = canvas.create_arc(30, 25, 100, 95, start=0,
            extent=180, outline="#fcba03", fill="#fcba03")

entryR = Entry(window, bg='lightgrey', width=10)

# bind Enter key to go to next element:
entryR.bind('<Return>', go_to_next_element)

# set focus to the first entry field:
entryR.focus() # set focus to this entry field

entryR.pack(padx=(10,0), side=LEFT)
entryG = Entry(window, bg='lightgrey', width=10)
entryG.bind('<Return>', go_to_next_element)
entryG.pack(padx=(10,0), side=LEFT)
entryB = Entry(window, bg='lightgrey', width=10)
entryB.bind('<Return>', go_to_next_element)
entryB.pack(padx=(10,0), side=LEFT)

button = Button(window, text='Change color', height=1, width=10, command=button_click)
button.bind('<Return>', button_click)
button.pack(padx=(10,0), side=LEFT)

# test setting the color:
#setColor(255, 0, 0)

window.mainloop()
