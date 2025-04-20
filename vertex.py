class Vertex:
    def __init__(self, vertex_id, x, y, z):
        self.id = vertex_id
        self.x = x
        self.y = y
        self.z = z

    def coordinates(self):
        return(self.x, self.y, self.z)    