import numpy as np
from wbpj.utils import build_2d_rotation_matrix


class TestRotations:
    def test_zero(self):
        R = build_2d_rotation_matrix(0)
        assert np.allclose(R, np.eye(2))

    def test_pi_over_two(self):
        R = build_2d_rotation_matrix(np.pi / 2)
        true = np.array([[0, -1], [1, 0]])
        assert np.allclose(R, true)

    def test_pi_over_four(self):
        R = build_2d_rotation_matrix(np.pi / 4)
        true = np.array([[np.sqrt(0.5), -np.sqrt(0.5)], [np.sqrt(0.5), np.sqrt(0.5)]])
        assert np.allclose(R, true)
