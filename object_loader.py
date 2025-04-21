from vertex import Vertex
from face import Face

def load_object(filepath):
    """
    Loads the object from a file and return its vertices and faces.

    The file format is expected to be:
        - First line: Number of vertices, Number of faces
        - Vertices lines: id, x, y, z
        - Faces lines: vertex ids of the face

    Parameters:
    filepath: Path of the file

    Returns a dictionary of vertices and a list of faces
    """

    vertices = {}
    faces = []

    # Read all lines and remove any empty ones
    with open(filepath) as file:
        lines = file.readlines()

    # Parse the first line to get number of vertices and faces
    line1 = lines[0].strip().split(",")
    num_vertices = int(line1[0])
    num_faces = int(line1[1])

    
    # Load vertices from lines
    for i in range(1, num_vertices+1):
        parts = lines[i].strip().split(",")
        vertex_id = int(parts[0])
        x, y, z = map(float, parts[1:])
        vertices[vertex_id] = Vertex(vertex_id, x, y, z)     

    # Load faces from lines
    for j in range(num_vertices + 1, num_faces + num_vertices + 1):
        v1, v2, v3 = [int(float(x)) for x in lines[j].strip().split(",")]
        faces.append(Face(v1, v2, v3))

    return vertices, faces    

