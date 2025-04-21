import tkinter as tk
import math
import numpy as np

class Viewer3D:
    def __init__(self, object3d, width=700, height=700):
        self.mode = "part1"
        self.object = object3d
        self.width = width
        self.height = height
        self.angle_x = 0
        self.angle_y = 0
        self.last_mouse = [0, 0]

        self.root = tk.Tk()
        self.root.title("3D Wireframe Viewer")
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="white")
        self.canvas.pack()
        self.toggle_button = tk.Button(self.root, text="Switch to Part 2", command=self.toggle_mode)
        self.toggle_button.pack()

        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)

        self.draw()
    
    def toggle_mode(self):
        if self.mode == "part1":
            self.mode = "part2"
            self.toggle_button.config(text="Switch to Part 1")
        else:
            self.mode = "part1"
            self.toggle_button.config(text="Switch to Part 2")
        self.draw()

    def rotate_vertex(self, vertex, return_3d=False):
        x, y, z = vertex.coordinates()
        cos_x, sin_x = math.cos(self.angle_x), math.sin(self.angle_x)
        y, z = y * cos_x - z * sin_x, y * sin_x + z * cos_x
        cos_y, sin_y = math.cos(self.angle_y), math.sin(self.angle_y)
        x, z = x * cos_y + z * sin_y, -x * sin_y + z * cos_y
        if return_3d:
            return (x, y, z)
        else:
            return (x, y)
    
    def compute_normal(self, v1, v2, v3):
        """
        Computes the normal vector of the triangle
        """
        a = np.array(v2) - np.array(v1)
        b = np.array(v3) - np.array(v1)
        normal = np.cross(a, b)
        return normal / np.linalg.norm(normal) if np.linalg.norm(normal) != 0 else normal

    def transform_to_canvas(self, x, y):
        scale = min(self.width, self.height) / 6
        return int(x * scale + self.width / 2), int(-y * scale + self.height / 2)

    def draw(self):
        self.canvas.delete("all")
        projected = {}
        rotated_3d = {}

        for vid, vertex in self.object.vertices.items():
            projected[vid] = self.transform_to_canvas(*self.rotate_vertex(vertex))
            rotated_3d[vid] = self.rotate_vertex(vertex, return_3d=True)

        if self.mode == "part2":
            # Filled triangles with shading
            for face in self.object.faces:
                n1, n2, n3 = rotated_3d[face.v1], rotated_3d[face.v2], rotated_3d[face.v3]
                normal = self.compute_normal(n1, n2, n3)
                z_axis = np.array([0, 0, 1])
                cos_angle = abs(np.dot(normal, z_axis))
                color = self.interpolate_color(cos_angle)

                p1, p2, p3 = projected[face.v1], projected[face.v2], projected[face.v3]
                self.canvas.create_polygon([p1, p2, p3], fill=color, outline="black")
        else:
            # Wireframe view from Part 1
            for face in self.object.faces:
                p1, p2, p3 = projected[face.v1], projected[face.v2], projected[face.v3]
                self.canvas.create_line(*p1, *p2, fill="blue")
                self.canvas.create_line(*p2, *p3, fill="blue")
                self.canvas.create_line(*p3, *p1, fill="blue")

            for x, y in projected.values():
                self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="blue")


    def interpolate_color(self, angle_cosine):
        """
        Maps cosine of angle to hex color between #00005F and #0000FF
        """
        min_rgb = (0, 0, 95)
        max_rgb = (0, 0, 255)
        r = 0
        g = 0
        b = int(min_rgb[2] + (max_rgb[2] - min_rgb[2]) * angle_cosine)
        return f'#{r:02x}{g:02x}{b:02x}'

    def on_mouse_drag(self, event):
        dx = event.x - self.last_mouse[0]
        dy = event.y - self.last_mouse[1]
        self.angle_y += dx * 0.01
        self.angle_x += dy * 0.01
        self.last_mouse = [event.x, event.y]
        self.draw()

    def run(self):
        self.root.mainloop()
