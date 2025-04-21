import numpy as np

class GeometryUtils:

    def rotate_vertex(vertex, angle_x, angle_y, return_3d=False):
        """
        Rotate a vertex around the x and y axes.

        Parameters:
            vertex: The vertex to rotate
            angle_x: Rotation angle around x-axis 
            angle_y: Rotation angle around y-axis
            return_3d: If True, returns x, y, z; otherwise just x, y

        Returns a tuple of rotated coordinates
        """
        x, y, z = vertex.coordinates()

        # Rotate around X-axis
        cos_x, sin_x = np.cos(angle_x), np.sin(angle_x)
        y, z = y * cos_x - z * sin_x, y * sin_x + z * cos_x

        # Rotate around Y-axis
        cos_y, sin_y = np.cos(angle_y), np.sin(angle_y)
        x, z = x * cos_y + z * sin_y, -x * sin_y + z * cos_y

        if return_3d:
            return (x, y, z) 
        else:
            return (x, y)


    def compute_normal(v1, v2, v3):
        """
        Compute the normal vector of a triangle defined by 3 points.

        Parameters:
            v1, v2, v3: 3D coordinates of the triangle's vertices

        Returns a unit normal vector
        """
        a = np.array(v2) - np.array(v1)
        b = np.array(v3) - np.array(v1)
        normal = np.cross(a, b)
        return normal / np.linalg.norm(normal) if np.linalg.norm(normal) != 0 else normal
