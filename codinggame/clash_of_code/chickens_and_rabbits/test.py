"""
Tests case(s) for 'chickens and rabbits' problem on CodingGames
"""
from solution import chickens_n_rabbits


def test_chicken_n_rabbits_solves_test_cases():
    """
    Tests all cases
    """
    assert chickens_n_rabbits(30, 90) == (15, 15)
