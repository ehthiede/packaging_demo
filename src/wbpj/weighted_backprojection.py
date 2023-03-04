import numpy as np
import finufft
from wbpj.utils import build_2d_rotation_matrix


def calculate_coords(npixels: int, angle, float) -> np.ndarray:
    xaxis = np.arange(npixels)
    xaxis -= np.mean(xaxis)
    coords = np.hstack([xaxis, np.zeros_like(xaxis)]).T
    R = build_2d_rotation_matrix(angle)

    coords_rot = coords @ R
    return coords_rot


def apply_ramp_filter(coords: np.ndarray, intensities: np.ndarray) -> np.ndarray:
    magnitude_of_coords = np.linalg.norm(coords, axis=1)
    return intensities * magnitude_of_coords


def weighted_backprojection_1d(
    image_stack: np.ndarray, angles: np.ndarray
) -> np.ndarray:
    """
    Simple implementation of the weighted backprojection algorithm for
    one-dimensional tomogram reconstruction.
    """
    npixels = np.max([i.shape[0] for i in image_stack])

    all_coords = []
    imgs_in_Fourier = []
    for img, angle in zip(image_stack, angles):
        all_coords.append(calculate_coords(img.shape[0], angle))
        imgs_in_Fourier.append(np.fft.fftshift(img))

    all_coords = np.concatenate(all_coords)
    imgs_in_Fourier = np.concatenate(imgs_in_Fourier)
    filtered_imgs = apply_ramp_filter(all_coords, imgs_in_Fourier)
    out = finufft.nufft2d1(
        all_coords[:, 0],
        all_coords[:, 1],
        filtered_imgs,
        isign=-1,
        n_modes=(npixels, npixels),
    )
    return out
