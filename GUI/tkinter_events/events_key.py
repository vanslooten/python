# https://realpython.com/python-gui-tkinter/#using-events-and-event-handlers
# Example of handling key press events in a Tkinter window

import tkinter as tk

window = tk.Tk()

def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

window.title("Key Press Event Example")
window.geometry("400x200")
window.mainloop()
