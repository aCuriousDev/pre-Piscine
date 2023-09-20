import tkinter as tk
from PIL import Image, ImageTk


class ResizableImageBackground(tk.Tk):
    def __init__(self, image_path, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Load the image and create an ImageTk.PhotoImage object
        self.original_image = Image.open(image_path)
        self.image = ImageTk.PhotoImage(self.original_image)

        # Create a canvas to display the image
        self.canvas = tk.Canvas(
            self, width=self.image.width(), height=self.image.height())
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)

        # Display the image on the canvas
        self.image_on_canvas = self.canvas.create_image(
            0, 0, anchor=tk.NW, image=self.image)

        # Bind the window's resize event to the update_image function
        self.bind("<Configure>", self.update_image)

    def update_image(self, event=None):
        # Calculate the new size preserving the image's aspect ratio
        width_ratio = event.width / self.original_image.width
        height_ratio = event.height / self.original_image.height
        new_ratio = min(width_ratio, height_ratio)

        new_width = int(self.original_image.width * new_ratio)
        new_height = int(self.original_image.height * new_ratio)

        # Resize the image and update the PhotoImage object
        resized_image = self.original_image.resize((new_width, new_height))
        self.image = ImageTk.PhotoImage(resized_image)

        # Update the image on the canvas
        self.canvas.itemconfig(self.image_on_canvas, image=self.image)

        # Center the image on the canvas
        self.canvas.coords(self.image_on_canvas, (event.width -
                           new_width) // 2, (event.height - new_height) // 2)


if __name__ == "__main__":
    app = ResizableImageBackground(
        "/home/quentin/Dev/pre-Piscine/Day08/Tkinter/5479107.png")
    app.mainloop()
