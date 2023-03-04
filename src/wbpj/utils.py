import numpy as np

def build_2d_rotation_matrix(angle: float):
    """
    Builds a two-dimensional rotation matrix
    """
    cos_a = np.cos(angle)
    sin_a = np.cos(angle)
    R = np.array([[cos_a, -sin_a], [sin_a, cos_a]])
    return R
