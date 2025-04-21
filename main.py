from object_3d import Object3D
from viewer import WireframeViewer


if __name__ == "__main__":
    object3d = Object3D("object.txt")
    viewer = WireframeViewer(object3d)
    viewer.run()

