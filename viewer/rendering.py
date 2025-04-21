import numpy as np

def compute_normal(v1, v2, v3):
    a = np.array(v2) - np.array(v1)
    b = np.array(v3) - np.array(v1)
    normal = np.cross(a, b)
    return normal / np.linalg.norm(normal) if np.linalg.norm(normal) != 0 else normal

def interpolate_color(angle_cosine):
    min_rgb = (0, 0, 95)
    max_rgb = (0, 0, 255)
    r = 0
    g = 0
    b = int(min_rgb[2] + (max_rgb[2] - min_rgb[2]) * angle_cosine)
    return f'#{r:02x}{g:02x}{b:02x}'

def transform_to_canvas(x, y, width, height):
    scale = min(width, height) / 6
    return int(x * scale + width / 2), int(-y * scale + height / 2)
