from geometry_utils import GeometryUtils
import tkinter as tk
import numpy as np

class Viewer3D:
    """
    A simple interactive 3D viewer using tkinter.

    This viewer supports two display modes:
    - Part 1: Wireframe view with vertex dots and edges
    - Part 2: Shaded solid view with color interpolation based on face orientation
    """

    def __init__(self, object, width=700, height=700):
        """
        Initialize the viewer window and setup GUI elements.

        Parameters:
        object: The object to visualize
        width: Width of the canvas window in pixels
        height: Height of the canvas window in pixels
        """
        self.mode = "part1" # Initial view mode
        self.object = object
        self.width = width
        self.height = height
        self.angle_x = 0 # Rotation angle around x-axis
        self.angle_y = 0 # Rotation angle around y-axis
        self.last_mouse = [0, 0] # Last mouse position for tracking

        # Set up tkinter window and canvas
        self.root = tk.Tk()
        self.root.title("3D Object Viewer")
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="white")
        self.canvas.pack()

        # Add a button to toggle between part 1 and part 2
        self.toggle_button = tk.Button(self.root, text="Switch to Part 2", command=self.toggle_mode)
        self.toggle_button.pack()

        # Bind mouse dragging to rotation
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)

        # Initial draw
        self.draw()
    
    def toggle_mode(self):
        """
        Toggle between Part 1 and Part 2 view modes.
        """
        if self.mode == "part1":
            self.mode = "part2"
            self.toggle_button.config(text="Switch to Part 1")
        else:
            self.mode = "part1"
            self.toggle_button.config(text="Switch to Part 2")
        self.draw()

    def transform_to_canvas(self, x, y):
        """
        Project coordinates into the tkinter canvas coordinate space.

        Parameters:
        x, y: original coordinates

        Returns a tuple of coordinates scaled and centered for tkinter canvas
        """
        scale = min(self.width, self.height) / 6
        return int(x * scale + self.width / 2), int(-y * scale + self.height / 2)

    def draw(self):
        """
        Render the object on the canvas based on the current mode.
        """
        self.canvas.delete("all")
        projected = {}
        rotated_3d = {}

        # Precompute rotated and projected vertices
        for vid, vertex in self.object.vertices.items():
            rotated = GeometryUtils.rotate_vertex(vertex, self.angle_x, self.angle_y, return_3d=True)
            rotated_3d[vid] = rotated
            projected[vid] = self.transform_to_canvas(*rotated[:2])

        if self.mode == "part2":
            # Part 2: Draw shaded triangles based on face normal and z-axis angle
            for face in self.object.faces:
                n1, n2, n3 = rotated_3d[face.v1], rotated_3d[face.v2], rotated_3d[face.v3]
                normal = GeometryUtils.compute_normal(n1, n2, n3)
                z_axis = np.array([0, 0, 1])
                cos_angle = abs(np.dot(normal, z_axis))
                color = self.interpolate_color(cos_angle)

                p1, p2, p3 = projected[face.v1], projected[face.v2], projected[face.v3]
                self.canvas.create_polygon([p1, p2, p3], fill=color, outline="black")
        else:
            # Part1: Wireframe view: draw edges and vertex dots
            for face in self.object.faces:
                p1, p2, p3 = projected[face.v1], projected[face.v2], projected[face.v3]
                self.canvas.create_line(*p1, *p2, fill="blue")
                self.canvas.create_line(*p2, *p3, fill="blue")
                self.canvas.create_line(*p3, *p1, fill="blue")

            # Draw vertices as small circles
            for x, y in projected.values():
                self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="blue")


    def interpolate_color(self, angle_cosine):
        """
        Interpolate between dark and light blue based on face angle.

        Parameters:
        angle_cosine: Cosine of angle between face normal and z-axis

        Returns the hex color code based on angle
        """
        min_rgb = (0, 0, 95)
        max_rgb = (0, 0, 255)
        r = 0
        g = 0
        b = int(min_rgb[2] + (max_rgb[2] - min_rgb[2]) * angle_cosine)
        return f'#{r:02x}{g:02x}{b:02x}'

    def on_mouse_drag(self, event):
        """
        Rotate the object based on mouse drag movement.

        Parameters:
        event: Tkinter event containing mouse coordinates
        """
        dx = event.x - self.last_mouse[0]
        dy = event.y - self.last_mouse[1]
        self.angle_y += dx * 0.01
        self.angle_x += dy * 0.01
        self.last_mouse = [event.x, event.y]
        self.draw()

    def run(self):
        """
        Start the Tkinter GUI event loop.
        """
        self.root.mainloop()
