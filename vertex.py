class Vertex:
    """
    Represents a single vertex in 3D space using coordinates x, y, z.
    """
    def __init__(self, vertex_id, x, y, z):
        """
        Initialize a Vertex object.

        Parameters:
        vertex_id: Unique identifier for the vertex
        x: X-coordinate
        y: Y-coordinate
        z: Z-coordinate
        """
        self.id = vertex_id
        self.x = x
        self.y = y
        self.z = z

    def coordinates(self):
        """
        Return the coordinates of the vertex as a tuple.
        """
        return(self.x, self.y, self.z)    