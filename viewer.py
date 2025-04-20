import tkinter as tk
import math

class WireframeViewer:
    def __init__(self, object3d, width=1000, height=1000):
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
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)

        self.draw()

    def rotate_vertex(self, vertex):
        x, y, z = vertex.coordinates()
        cos_x, sin_x = math.cos(self.angle_x), math.sin(self.angle_x)
        y, z = y * cos_x - z * sin_x, y * sin_x + z * cos_x
        cos_y, sin_y = math.cos(self.angle_y), math.sin(self.angle_y)
        x, z = x * cos_y + z * sin_y, -x * sin_y + z * cos_y
        return (x, y)

    def transform_to_canvas(self, x, y):
        scale = min(self.width, self.height) / 3
        return int(x * scale + self.width / 2), int(-y * scale + self.height / 2)

    def draw(self):
        self.canvas.delete("all")
        projected = {}
        for vid, vertex in self.object.vertices.items():
            px, py = self.rotate_vertex(vertex)
            projected[vid] = self.transform_to_canvas(px, py)

        for face in self.object.faces:
            v1, v2, v3 = face.get_indices()
            p1, p2, p3 = projected[v1], projected[v2], projected[v3]
            self.canvas.create_line(*p1, *p2, fill="blue")
            self.canvas.create_line(*p2, *p3, fill="blue")
            self.canvas.create_line(*p3, *p1, fill="blue")

        for x, y in projected.values():
            self.canvas.create_oval(x-2, y-2, x+2, y+2, fill="blue")

    def on_mouse_drag(self, event):
        dx = event.x - self.last_mouse[0]
        dy = event.y - self.last_mouse[1]
        self.angle_y += dx * 0.01
        self.angle_x += dy * 0.01
        self.last_mouse = [event.x, event.y]
        self.draw()

    def run(self):
        self.root.mainloop()
