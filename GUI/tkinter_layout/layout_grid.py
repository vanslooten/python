# Grid layout example with header, content and footer, where header and footer have fixed height in %
# Learn more about grids:
# https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/
# Learn more about layouts:
# https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/

import tkinter as tk

BG_COLOR = 'lightblue'
HEADER_FOOTER_COLOR = 'darkblue'

root = tk.Tk()
root.geometry('400x300')
# set title of window
root.title("Tkinter Layout Example")

header = tk.Frame(root, bg=HEADER_FOOTER_COLOR)
content = tk.Frame(root, bg=BG_COLOR)
footer = tk.Frame(root, bg=HEADER_FOOTER_COLOR)

# layout with grid: 1 column, 3 rows:
# https://www.tutorialspoint.com/python/tk_grid.htm
root.columnconfigure(0, weight=1) # 100% 

root.rowconfigure(0, weight=1) # 10%
root.rowconfigure(1, weight=8) # 80%
root.rowconfigure(2, weight=1) # 10%

header.grid(row=0, sticky='news') # sticky='news' to expand in cell (stick to North, East, West, South)
content.grid(row=1, sticky='news')
footer.grid(row=2, sticky='news')

# add Label to content frame
label = tk.Label(content, text="Content Area", bg=BG_COLOR)
label.pack(expand=True) # expand=True to center in content frame

root.mainloop()
