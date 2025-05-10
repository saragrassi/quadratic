from quadratic import Quadratic
from cmath import isclose


def test_complex_roots():
    q = Quadratic(1, 2, 5)
    expected = complex(-1, 2), complex(-1, -2)
    result = q.solve()
    assert isclose(expected[0], result[0], rel_tol=1e-9)
    assert isclose(expected[1], result[1], rel_tol=1e-9)


def test_real_roots():
    q = Quadratic(1, -3, 2)
    expected = complex(2, 0), complex(1, 0)
    result = q.solve()
    assert isclose(result[0], expected[0], rel_tol=1e-9)
    assert isclose(result[1], expected[1], rel_tol=1e-9)


def test_double_root():
    q = Quadratic(1, 2, 1)
    expected = complex(-1, 0), complex(-1, 0)
    result = q.solve()
    assert isclose(result[0], expected[0], rel_tol=1e-9)
    assert isclose(result[1], expected[1], rel_tol=1e-9)
