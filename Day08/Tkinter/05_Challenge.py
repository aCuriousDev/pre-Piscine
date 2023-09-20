import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import os


def normalize(vector):
    return vector / np.linalg.norm(vector)


def reflected(vector, axis):
    return vector - 2 * np.dot(vector, axis) * axis


def sphere_intersect(center, radius, ray_origin, ray_direction):
    b = 2 * np.dot(ray_direction, ray_origin - center)
    c = np.linalg.norm(ray_origin - center) ** 2 - radius ** 2
    delta = b ** 2 - 4 * c
    if delta > 0:
        t1 = (-b + np.sqrt(delta)) / 2
        t2 = (-b - np.sqrt(delta)) / 2
        if t1 > 0 and t2 > 0:
            return min(t1, t2)
    return None


def nearest_intersected_object(objects, ray_origin, ray_direction):
    distances = [sphere_intersect(
        obj['center'], obj['radius'], ray_origin, ray_direction) for obj in objects]
    nearest_object = None
    min_distance = np.inf
    for index, distance in enumerate(distances):
        if distance and distance < min_distance:
            min_distance = distance
            nearest_object = objects[index]
    return nearest_object, min_distance


def render_scene():
    width = 300
    height = 200
    max_depth = 3

    camera = np.array([0, 0, 1])
    ratio = float(width) / height
    screen = (-1, 1 / ratio, 1, -1 / ratio)  # left, top, right, bottom

    light_position = np.array([float(light_x_entry.get()), float(
        light_y_entry.get()), float(light_z_entry.get())])
    light = {'position': light_position, 'ambient': np.array(
        [1, 1, 1]), 'diffuse': np.array([1, 1, 1]), 'specular': np.array([1, 1, 1])}

    sphere_color = np.array([float(red_scale.get()), float(
        green_scale.get()), float(blue_scale.get())])

    objects = [
        {'center': np.array([0, 0, -5]), 'radius': 1, 'ambient': sphere_color, 'diffuse': sphere_color,
         'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5},
        {'center': np.array([0, -5001, 0]), 'radius': 5000, 'ambient': np.array([0.5, 0.5, 0.5]), 'diffuse': np.array(
            [0.5, 0.5, 0.5]), 'specular': np.array([1, 1, 1]), 'shininess': 1000, 'reflection': 0}
    ]

    image = np.zeros((height, width, 3))
    for i, y in enumerate(np.linspace(screen[1], screen[3], height)):
        for j, x in enumerate(np.linspace(screen[0], screen[2], width)):
            pixel = np.array([x, y, 0])
            origin = camera
            direction = normalize(pixel - origin)

            color = np.zeros((3))
            reflection = 1

            for k in range(max_depth):
                nearest_object, min_distance = nearest_intersected_object(
                    objects, origin, direction)
                if nearest_object is None:
                    break

                intersection = origin + min_distance * direction
                normal_to_surface = normalize(
                    intersection - nearest_object['center'])
                shifted_point = intersection + 1e-5 * normal_to_surface
                intersection_to_light = normalize(
                    light['position'] - shifted_point)

                _, min_distance = nearest_intersected_object(
                    objects, shifted_point, intersection_to_light)
                intersection_to_light_distance = np.linalg.norm(
                    light['position'] - intersection)
                is_shadowed = min_distance < intersection_to_light_distance

                if is_shadowed:
                    break

                illumination = np.zeros((3))

                # ambiant
                illumination += nearest_object['ambient'] * light['ambient']

                # diffuse
                illumination += nearest_object['diffuse'] * light['diffuse'] * \
                    np.dot(intersection_to_light, normal_to_surface)

                # specular
                intersection_to_camera = normalize(camera - intersection)
                H = normalize(intersection_to_light + intersection_to_camera)
                illumination += nearest_object['specular'] * light['specular'] * np.dot(
                    normal_to_surface, H) ** (nearest_object['shininess'] / 4)

                # reflection
                color += reflection * illumination
                reflection *= nearest_object['reflection']

                origin = shifted_point
                direction = reflected(direction, normal_to_surface)

            image[i, j] = np.clip(color, 0, 1)

    plt.imsave('rendered_image.png', image)


def render():
    loader_label.config(text="Rendering...")
    root.update()
    render_scene()
    if os.path.exists('rendered_image.png'):
        image = Image.open('rendered_image.png')
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.image = photo
        loader_label.config(text="Rendering Complete!")
    else:
        loader_label.config(text="Rendering Failed!")


root = tk.Tk()
root.title("Ray Tracing with Tkinter")

frame = ttk.LabelFrame(root, text="Controls")
frame.pack(pady=20)

red_scale = ttk.Scale(frame, from_=0, to=1, orient="horizontal", value=0.5)
red_scale.grid(row=0, column=0, sticky="ew")
green_scale = ttk.Scale(frame, from_=0, to=1, orient="horizontal", value=0.5)
green_scale.grid(row=1, column=0, sticky="ew")
blue_scale = ttk.Scale(frame, from_=0, to=1, orient="horizontal", value=0.5)
blue_scale.grid(row=2, column=0, sticky="ew")

light_x_entry = ttk.Entry(frame)
light_x_entry.grid(row=0, column=1)
light_x_entry.insert(0, "5")

light_y_entry = ttk.Entry(frame)
light_y_entry.grid(row=1, column=1)
light_y_entry.insert(0, "5")

light_z_entry = ttk.Entry(frame)
light_z_entry.grid(row=2, column=1)
light_z_entry.insert(0, "5")

render_button = ttk.Button(frame, text="Render", command=render)
render_button.grid(row=3, column=0, columnspan=2)

loader_label = ttk.Label(frame, text="")
loader_label.grid(row=4, column=0, columnspan=2)

canvas = tk.Canvas(root, width=300, height=200)
canvas.pack(pady=20)

root.mainloop()
