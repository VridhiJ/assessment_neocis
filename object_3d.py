from object_loader import load_object

class Object3D:
    """
    Loads data from object file and stores the geometry 
    as dictionaries of vertices and a list of faces.
    """
    def __init__(self, filepath):
        """
        Initialize the object by loading vertex and face data from a file.

        Parameters:
        filepath: Path of the object file
        """
        self.vertices, self.faces = load_object(filepath)

    def get_vertex_by_id(self, vertex_id):
        """
        Retrieve a vertex object by its id.

        Parameters:
        vertex_id: The unique id of the vertex to retrieve

        Returns the corresponding Vertex object.
        """
        return self.vertices[vertex_id]
