class Face:
    def __init__(self, index1, index2, index3):
        self.v1 = index1
        self.v2 = index2
        self.v3 = index3

    def get_vertices(self):
        return (self.v1, self.v2, self.v3)
