from vertex import Vertex
from face import Face

def load_object(filepath):

    vertices = {}
    faces = []
    with open(filepath) as file:
        lines = file.readlines()

    line1 = lines[0].strip().split(",")
    num_vertices = int(line1[0])
    num_faces = int(line1[1])

    

    for i in range(1, num_vertices+1):
        parts = lines[i].strip().split(",")
        vertex_id = int(parts[0])
        x, y, z = map(float, parts[1:])
        vertices[vertex_id] = Vertex(vertex_id, x, y, z)     

    for j in range(num_vertices + 1, num_faces + num_vertices + 1):
        v1, v2, v3 = [int(float(x)) for x in lines[j].strip().split(",")]
        faces.append(Face(v1, v2, v3))

    return vertices, faces    

