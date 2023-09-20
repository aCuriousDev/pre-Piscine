import tkinter as tk
from tkinter import PhotoImage

# Function to be called when the button is clicked


def display_uppercase_content():
    content = entry.get().upper()
    output_label.config(text=content)


# Create the main window
root = tk.Tk()
root.title("Tkinter Task")

# Create a LabelFrame
labelframe = tk.LabelFrame(root, text="Input Area")
labelframe.pack(padx=10, pady=10)

# Add an Entry widget (input field) inside the LabelFrame
entry = tk.Entry(labelframe)
entry.pack(padx=10, pady=10)

# Add a Button below the Entry widget inside the LabelFrame
button = tk.Button(labelframe, text="Display UPPERCASE",
                   command=display_uppercase_content)
button.pack(pady=10)

# Label to display the uppercase content below the button
output_label = tk.Label(labelframe, text="")
output_label.pack(pady=10)

# Create a Frame
frame = tk.Frame(root)
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Add a Canvas to the Frame
canvas = tk.Canvas(frame)
canvas.pack(fill=tk.BOTH, expand=True)

# Load a background image into the Canvas (ensure the image file path is correct)
bg_image = PhotoImage(
    file="/home/quentin/Dev/pre-Piscine/Day08/Tkinter/5479107.png")
canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

# Adjust the canvas size to match the image size
canvas.config(scrollregion=canvas.bbox(tk.ALL))

# Run the tkinter main loop
root.mainloop()
