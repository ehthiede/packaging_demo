import numpy as np
from wbpj.utils import build_2d_rotation_matrix
from wbpj.weighted_backprojection import weighted_backprojection_1d


def _perform_single_projection(angle: float, ax: np.ndarray, centers: np.ndarray):
    R = build_2d_rotation_matrix(angle)

    rotated_centers = centers @ R
    proj_centers = (rotated_centers[:, 0]).reshape(-1, 1)

    dx = ax - proj_centers
    gaussians = np.exp(-dx**2 / .2)
    return gaussians.sum(axis=0)


def _setup_images():
    centera = np.array([1.0, 0.])
    centerb = np.array([0.0, 1.])
    centerc = np.array([-1.0, -1.0])
    centers = np.vstack([centera, centerb, centerc])

    angles = np.linspace(0, np.pi, 16, endpoint=False)
    ax = np.linspace(-4, 4, 101)

    # Build the projection images
    imgs = []
    for angle in angles:
        imgs.append(_perform_single_projection(angle, ax, centers))

    XX, YY = np.meshgrid(ax, ax)

    dX = centers[:, 0].reshape(-1, 1, 1) - XX
    dY = centers[:, 1].reshape(-1, 1, 1) - YY

    sq_distance = dX**2 + dY**2
    gaussians = np.exp(-sq_distance / .2)
    volume = np.sum(gaussians, axis=0)

    return imgs, volume


def test_weighted_backprojection_1d():
    imgs, vol = _setup_images()
