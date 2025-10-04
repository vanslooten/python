# Basic pack layout with header and footer with fixed height in pixels
# uses side='bottom' to put footer at the bottom
# Learn more about layouts:
# https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/

import tkinter as tk

BG_COLOR = 'lightblue'
HEADER_FOOTER_COLOR = 'darkblue'

root = tk.Tk()
root.geometry('400x300')
root.title("Tkinter pack Layout Example")

header = tk.Frame(root, bg=HEADER_FOOTER_COLOR, height=30)
content = tk.Frame(root, bg=BG_COLOR)
footer = tk.Frame(root, bg=HEADER_FOOTER_COLOR, height=30)

header.pack(fill='both') #, side='top')
content.pack(fill='both', expand=True)
footer.pack(fill='both', side='bottom')

# add Label to content frame
label = tk.Label(content, text="Content Area", bg=BG_COLOR)
label.pack(expand=True) # expand=True to center in content frame

root.mainloop()
