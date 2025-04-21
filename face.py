class Face:
    """
    Represents a single triangular face in a 3D object.
    Each face is defined by the indices of three vertices that form the corners of the triangle.  
    """
    def __init__(self, index1, index2, index3):
        """
        Initialize a face using the indices of its 3 vertices.
        Parameters:
        index1: Vertex id of the first corner
        index2: Vertex id of the second corner
        index3: Vertex id of the third corner
        """
        self.v1 = index1
        self.v2 = index2
        self.v3 = index3

    def get_indices(self):
        """
        Returns a tuple of the three vertex IDs that define the face.
        """
        return (self.v1, self.v2, self.v3)
