import argparse
import logging
import numpy as np
from weighted_backprojection import weighted_backprojection_1d


def _parse_CLAs() -> argparse.ArgumentParser:
    """
    Parses Command Line Arguments

    Returns:
        argparse.ArgumentParser: parsed command line arguments
    """
    parser = argparse.ArgumentParser(description="Runs SMC Chain Growth")
    parser.add_argument(
        "image_file", type=str, help="Path to Image stack, saved as a numpy file"
    )
    parser.add_argument(
        "angle_range",
        type=float,
        nargs=2,
        help="First and last angle.  Angles are assumed to be equispaced.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="reconstructed_volume.npy",
        help="Location to save the reconstructed volume.",
    )

    parser.add_argument(
        "--degrees",
        action="store_true",
        help="Angles given are in degrees, not radians",
    )

    parser.add_argument(
        "-d",
        "--debug",
        help="Print lots of debugging statements",
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
        default=logging.WARNING,
    )

    parser.add_argument(
        "-v",
        "--verbose",
        help="Be verbose",
        action="store_const",
        dest="loglevel",
        const=logging.INFO,
    )

    return parser


def main(args: argparse.ArgumentParser):
    logging.basicConfig(level=args.loglevel)
    images = np.load(args.image_file)
    num_images = len(images)

    angles = np.linspace(args.angle_range[0], args.angle_range[1], num_images)
    if args.degrees:
        angles *= 180.0 / np.pi

    reconstructed_volume = weighted_backprojection_1d(images, angles)
    np.save(args.output, reconstructed_volume)


if __name__ == "__main__":
    parser = _parse_CLAs()
    args = parser.parse_args()

    main(args)
