# https://www.geeksforgeeks.org/python/creating-tabbed-widget-with-python-tkinter/
# ttk is the themed widget set introduced in Tkinter 8.5, which provides a more modern look and feel to the standard Tkinter widgets.
# ttk includes a Notebook widget that allows you to create tabbed interfaces.

import tkinter as tk
# import ttk widgets:
from tkinter import ttk

# list of fruits to choose from
FRUITS = ("Apple", "Banana", "Cherry", "Date", "Elderberry")

root = tk.Tk()
root.title("Tab Widget")
tabControl = ttk.Notebook(root, padding=10)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Tab 1')
tabControl.add(tab2, text='Tab 2')
# pack to make visible, expand to fill space in both directions
tabControl.pack(expand=1, fill="both")

ttk.Label(tab1, text="Please take a fruit").grid(
    column = 0, 
    row = 0,
    padx = 30,
    pady = 30)

# Radio buttons in tab1 to select a fruit
selected_fruit = tk.StringVar(value=FRUITS[0])
rb_frame = ttk.LabelFrame(tab1, text="Choose a fruit")
rb_frame.grid(column=0, row=1, padx=30, pady=(0,30), sticky='w')

for i, fruit in enumerate(FRUITS):
    ttk.Radiobutton(rb_frame, text=fruit, value=fruit, variable=selected_fruit).grid(
        column=0, row=i, sticky='w', padx=10, pady=2)

# Label that displays the currently selected fruit
selection_label = ttk.Label(tab1, text=f"Selected: {selected_fruit.get()}")
selection_label.grid(column=0, row=2, padx=30, pady=(0,30), sticky='w')

# Callback function to update the label when selection changes
def _on_fruit_change(*args):
    selection_label.config(text=f"Selected: {selected_fruit.get()}")

# Use trace_add for Tk 8.6+/Python 3.6+; fallback to trace if not available
try:
    selected_fruit.trace_add('write', _on_fruit_change)
except AttributeError:
    # older tkinter versions
    selected_fruit.trace('w', _on_fruit_change)

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
