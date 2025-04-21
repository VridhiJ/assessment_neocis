from object_3d import Object3D
from viewer import Viewer3D

def main():
    """
    Loads a 3D object from file and opens an interactive window 
    to visualize it either as a wireframe or as a shaded model.
    """
    # Load the object from file
    object3d = Object3D("object.txt")

    # Initialize the viewer with the object
    viewer = Viewer3D(object3d)

    # Start the interactive window
    viewer.run()


if __name__ == "__main__":
    main()

