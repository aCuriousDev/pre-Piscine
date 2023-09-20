import tkinter as tk

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

# Create a Frame (though the task does not specify what to do with it)
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Run the tkinter main loop
root.mainloop()
