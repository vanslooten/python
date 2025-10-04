# add a Listbox to a frame using pack layout manager
import tkinter as tk

BG_COLOR = 'lightblue'
HEADER_FOOTER_COLOR = 'darkblue'

# list of fruits to choose from
FRUITS = ("Apple", "Banana", "Cherry", "Date", "Elderberry")

root = tk.Tk()
root.geometry('400x400')
root.title("Tkinter pack Layout Example")

header = tk.Frame(root, bg=HEADER_FOOTER_COLOR, height=30)
content = tk.Frame(root, bg=BG_COLOR)
footer = tk.Frame(root, bg=HEADER_FOOTER_COLOR, height=30)

header.pack(fill='both') #, side='top')
content.pack(fill='both', expand=True)
footer.pack(fill='both', side='bottom')

# add Label to content frame
label = tk.Label(content, text="Select from list:", bg=BG_COLOR)
# Anchor to the top (north) and give small top/bottom padding so label sits near the top
label.pack(anchor='n', pady=(8,4))

# Create a horizontal container so listbox and scrollbar sit side-by-side
list_container = tk.Frame(content, bg=BG_COLOR)
list_container.pack(anchor='n', pady=(0,8))

# create the listbox and a vertical scrollbar
listbox = tk.Listbox(list_container, height=8)
vscroll = tk.Scrollbar(list_container, orient='vertical', command=listbox.yview)
listbox.config(yscrollcommand=vscroll.set)

# add fruits to listbox
for i, fruit in enumerate(FRUITS):
    listbox.insert(i, fruit)

# pack listbox and scrollbar side-by-side
listbox.pack(side='left', fill='y')
vscroll.pack(side='left', fill='y')

root.mainloop()
