# final version of tkinter hello world with input
# tutorial: https://home.et.utwente.nl/slootenvanf/2024/02/20/python-hello-world/

import tkinter as tk

def say_hello():
    print('What was entered:'+entry.get())
    message.set('Hello '+entry.get())

window = tk.Tk()

greeting = tk.Label(text="Hello world!")

greeting.pack()

# input part:
input_frame = tk.Frame()
namelabel = tk.Label(master = input_frame, text = 'Enter name:')
entry = tk.Entry(master = input_frame)
button = tk.Button(master = input_frame, text='Ok', command = say_hello)
namelabel.pack(side = 'left')
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

# add message:
message = tk.StringVar();
output_label = tk.Label(font='Calibri 22', textvariable=message)
output_label.pack()

# run
window.mainloop()

