import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Colored Stickman Drawing")

# Create a canvas for drawing
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack(pady=20)

# Draw the head (a circle) - Green
canvas.create_oval(175, 50, 225, 100, fill="lime", width=0)

# Draw the body (a line) - Dark Green
canvas.create_line(200, 100, 200, 200, fill="dark green", width=5)

# Draw the left arm - Red
canvas.create_line(200, 150, 150, 120, fill="red", width=5)

# Draw the right arm - Blue
canvas.create_line(200, 150, 250, 120, fill="blue", width=5)

# Draw the left leg - Purple
canvas.create_line(200, 200, 150, 250, fill="purple", width=5)

# Draw the right leg - Yellow
canvas.create_line(200, 200, 250, 250, fill="orange", width=5)

# Add text near the stickman's head
canvas.create_text(200, 30, text="Hello, I'm Colored Stickman!")

# Run the main loop
root.mainloop()
