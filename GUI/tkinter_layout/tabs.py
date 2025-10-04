# https://www.geeksforgeeks.org/python/creating-tabbed-widget-with-python-tkinter/
# ttk is the themed widget set introduced in Tkinter 8.5, which provides a more modern look and feel to the standard Tkinter widgets.
# ttk includes a Notebook widget that allows you to create tabbed interfaces.

import tkinter as tk
# import ttk widgets:
from tkinter import ttk

root = tk.Tk()
root.title("Tab Widget")
tabControl = ttk.Notebook(root, padding=10)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Tab 1')
tabControl.add(tab2, text='Tab 2')
# pack to make visible, expand to fill space in both directions
tabControl.pack(expand=1, fill="both")

ttk.Label(tab1, text="Welcome to Design of Data Acquisition Systems").grid(
    column = 0, 
    row = 0,
    padx = 30,
    pady = 30)

ttk.Label(tab2, text="This is the second tab").grid(
    column = 0,
    row = 0, 
    padx = 30,
    pady = 30,
    sticky = 'w') # sticky='w' to align to the left (west)

# Add a Button to tab2:
ttk.Button(tab2, text="Click Me").grid(
    column = 0,
    row = 1, # row 1, below the label (which is in row 0)
    padx = 30,
    pady = 30,
    sticky = 'w')

# Ensure column 0 of tab2 expands to fit and aligns to the left
tab2.columnconfigure(0, weight=1)

root.mainloop()
