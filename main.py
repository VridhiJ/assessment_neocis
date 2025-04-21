from object_3d import Object3D
from viewer import Viewer3D


if __name__ == "__main__":
    object3d = Object3D("object.txt")
    viewer = Viewer3D(object3d)
    viewer.run()

