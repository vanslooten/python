# Basic pack layout with header and footer with fixed height in pixels
# uses side='bottom' to put footer at the bottom

import tkinter as tk

BG_COLOR = 'lightgrey'
UI_WIDTH = 400
UI_HEIGHT = 150

# Create the main window
root = tk.Tk()
root.title("Place layout example")

root.geometry(f"{UI_WIDTH}x{UI_HEIGHT}") # Use variables for width and height

# --- Content Area (Frame) ---
content = tk.Frame(root, bg=BG_COLOR, bd=2, relief=tk.GROOVE)

# 1. Fill the width of the parent (root)
# relx=0: Start at 0% of the parent's width
# rely=0: Start at 0% of the parent's height
# relwidth=1.0: Make it 100% of the parent's width
# relheight=0.7: Make it 70% of the parent's height
content.place(relx=0, rely=0, relwidth=1.0, relheight=0.7)

# --- Label inside the Content Area ---
label = tk.Label(
    content,
    text="This Label is at the top of the content area and is also full width.",
    bg=BG_COLOR,
    wraplength=UI_WIDTH-50 # Allows the text to wrap
)

# 2. Position the Label inside the Frame
# relx=0.0 and relwidth=1.0 make it stretch across the Frame's width.
# rely=0.05 positions it near the top (5% down)
label.place(relx=0.0, rely=0.05, relwidth=1.0, relheight=0.3)

# --- Button inside the Content Area ---
button = tk.Button(content, text="The Button is underneath the Label")

# 3. Position the Button underneath the Label inside the Frame
# relx=0.5: Center the button horizontally (starts at 50% mark)
# rely=0.6: Position it further down (60% down)
# anchor='n': Tells 'place' to center the widget's top edge at the x,y point.
button.place(relx=0.5, rely=0.6, anchor='n')

# Start the Tkinter event loop
root.mainloop()