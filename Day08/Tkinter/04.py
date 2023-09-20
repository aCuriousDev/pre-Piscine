import tkinter as tk


def animate_arms():
    global direction, left_arm, right_arm, left_arm_coords, right_arm_coords

    # Depending on the direction, adjust the arm positions
    if direction == 'up':
        left_arm_coords[3] -= 1
        right_arm_coords[3] -= 1

        if left_arm_coords[3] <= 100:
            direction = 'down'
    else:
        left_arm_coords[3] += 1
        right_arm_coords[3] += 1

        if left_arm_coords[3] >= 120:
            direction = 'up'

    # Update arm coordinates
    canvas.coords(left_arm, left_arm_coords)
    canvas.coords(right_arm, right_arm_coords)

    # Continue animation
    root.after(10, animate_arms)


# Create the main window
root = tk.Tk()
root.title("Colored Stickman Drawing")

# Create a canvas for drawing
canvas = tk.Canvas(root, bg="white")
canvas.pack(pady=20)

# Draw the head (a circle) - Green
canvas.create_oval(175, 50, 225, 100, fill="lime", width=0)

# Draw the body (a line) - Dark Green
canvas.create_line(200, 100, 200, 200, fill="dark green", width=5)

# Initial arm coordinates
left_arm_coords = [200, 150, 150, 120]
right_arm_coords = [200, 150, 250, 120]

# Draw the left arm - Red
left_arm = canvas.create_line(left_arm_coords, fill="red", width=5)

# Draw the right arm - Blue
right_arm = canvas.create_line(right_arm_coords, fill="blue", width=5)

# Draw the left leg - Purple
canvas.create_line(200, 200, 150, 250, fill="purple", width=5)

# Draw the right leg - Yellow
canvas.create_line(200, 200, 250, 250, fill="orange", width=5)

# Add text near the stickman's head
canvas.create_text(200, 30, text="Hello, I'm Colored Stickman!")

direction = 'up'
animate_arms()

# Run the main loop
root.mainloop()
