from object_loader import load_object

class Object3D:
    def __init__(self, filepath):
        self.vertices, self.faces = load_object(filepath)

    def get_vertex_by_id(self, vertex_id):
        return self.vertices[vertex_id]
