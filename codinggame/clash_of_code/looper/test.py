"""
Tests solution
"""
from solution import looper


def test_solution():
    """
    Tests solution
    """
    assert looper(1) == "1"
    assert (
        looper(10) == "1234567891012345678910123456789101234567891012345"
        "6789101234567891012345678910123456789101234567891012345678910"
    )
