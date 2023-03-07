import numpy as np
import finufft
import logging
from utils import build_2d_rotation_matrix


def calculate_coords(xaxis: np.ndarray, angle: float) -> np.ndarray:
    """
    Calculates the coordinates of a Fourier slice located at specific angle.

    Args:
        xaxis (np.ndarray): coordinates of each point.
        angle (float): Angle in radians of the Fourier slice.

    Returns:
        np.ndarray: rotated coordinates
    """
    coords = np.vstack([xaxis, np.zeros_like(xaxis)]).T
    R = build_2d_rotation_matrix(angle)
    coords_rot = coords @ R
    return coords_rot


def apply_ramp_filter(coords: np.ndarray, intensities: np.ndarray) -> np.ndarray:
    """
    Applies a ramp filter to a function supported on a point cloud.

    Args:
        coords (np.ndarray): coordinates of each point.
        intensities (np.ndarray): Value of the function on each point

    Returns:
        np.ndarray: ramped intensities.
    """
    magnitude_of_coords = np.linalg.norm(coords, axis=1)
    return intensities * magnitude_of_coords


def weighted_backprojection_1d(
    image_stack: np.ndarray, angles: np.ndarray
) -> np.ndarray:
    """
    Simple implementation of the weighted backprojection algorithm for
    one-dimensional tomogram reconstruction.

    Args:
        image_stack (np.ndarray): Stack of images.  First dimension is the
            image index and the second is the image coordinate.
            Assumed to be centered at the rotation axis.
        angles (np.ndarray): Angle at which each image is taken

    Returns:
        np.ndarray: the reconstructied volume.
    """
    npixels = np.max([i.shape[0] for i in image_stack])
    xaxis = np.linspace(-1, 1, npixels)

    logging.info("Taking Fourier transform of 1D images")
    all_coords = []
    imgs_in_Fourier = []
    for img, angle in zip(image_stack, angles):
        logging.debug("Transforming image at angle %.3f pi" % (angle / np.pi))
        all_coords.append(calculate_coords(xaxis, angle))
        imgft = finufft.nufft1d1(xaxis, img.astype("complex"), n_modes=xaxis.shape)
        imgs_in_Fourier.append(imgft)

    logging.info("Slotting in images and applying ramp filter")
    all_coords = np.concatenate(all_coords, axis=0)
    all_coords /= np.max(np.abs(all_coords))
    imgs_in_Fourier = np.concatenate(imgs_in_Fourier, axis=0)
    imgs_in_Fourier = imgs_in_Fourier.astype("complex")
    imgs_in_Fourier = apply_ramp_filter(all_coords, imgs_in_Fourier)

    logging.info("Taking Inverse Fourier transform to build volume")
    out = finufft.nufft2d1(
        all_coords[:, 0],
        all_coords[:, 1],
        imgs_in_Fourier,
        isign=-1,
        n_modes=(npixels, npixels),
    )
    return out[:, ::-1]  # For some reason everything is coming out flipped?
