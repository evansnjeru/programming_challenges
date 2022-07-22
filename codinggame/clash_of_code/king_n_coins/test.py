"""
Tests for kings problem
"""
from solution import king_n_coins


def test_solves_king_n_coins():
    """
    Tests for kings problem
    """
    assert king_n_coins(3, 15) is True
