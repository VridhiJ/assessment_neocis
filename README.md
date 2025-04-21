# 3D Objects Viewer

This is a basic 3D viewer written in Python using only 2D graphics (`tkinter`). It reads a 3D object from a `.txt` file, renders it as a wireframe, and can also display shaded faces based on their orientation.

## Features
- Rotatable 3D model using mouse drag
- Part 1: Wireframe display with vertex dots
- Part 2: Shaded triangle faces with lighting effect
- Toggle between modes with a button

## File Format (`object.txt`)
```
6,8                      # Number of vertices, number of faces
1,1.0,0.0,0.0            # Vertex ID, x, y, z
...
1,2,3                   # Face defined by 3 vertex IDs
...
```

## How to Run

```bash
python3 main.py [filename]
```
You can pass a filename to load a specific object file, if no filename is provided, it defaults to object.txt.
Make sure the specified file is in the same folder as `main.py`.

##  Requirements
- Python 3.7+
- `tkinter`
- `numpy`
