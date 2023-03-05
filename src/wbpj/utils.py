import numpy as np


def build_2d_rotation_matrix(angle: float):
    """
    Builds a two-dimensional rotation matrix.

    Args:
        angle (float): The angle of the rotation to apply.

    Returns:
        np.ndarray: The rotation matrix.
    """
    cos_a = np.cos(angle)
    sin_a = np.sin(angle)
    R = np.array([[cos_a, -sin_a], [sin_a, cos_a]])
    return R
