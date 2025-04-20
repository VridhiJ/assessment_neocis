def read_file(path):
    with open(path) as file:
        lines = file.readlines()

    num_vertices, num_faces = lines[0].strip().split()

    vertices = {}
    faces = []

    for i in range(1, num_vertices+1):
        vertex_id, x, y, z = lines[i].strip().split()
        vertices[vertex_id] = (x, y, z)     

    for j in range(num_vertices + 1, num_faces + num_vertices + 1):
        v1_id, v2_id, v3_id = lines[i].strip().split()
        faces.append((v1_id, v2_id, v3_id))

    return vertices, faces    

