"""A small Tkinter example: click a button to change a label."""

import tkinter as tk


def change_message():
    """Change the label's text when the button is clicked."""
    message_label.config(text="You clicked the button!")


# Create the main application window.
window = tk.Tk()
window.title("Tkinter Button Example")
window.geometry("350x180")

# A Label displays text in the window.
# We save it in a variable so the callback can update it later.
message_label = tk.Label(
    window,
    text="Click the button to change this message.",
    font=("Arial", 12),
)
message_label.pack(pady=20)

# A Button responds to a click.
# Pass the function itself (without parentheses) to `command`.
# The function passed to `command` will be called when the button is clicked: this is the eventhandler.
# Tkinter will call it when the button is pressed.
change_button = tk.Button(
    window,
    text="Click me",
    command=change_message,
)
change_button.pack()

# Start Tkinter's event loop. It waits for events such as button clicks
# and keeps the window responsive until the user closes it.
window.mainloop()