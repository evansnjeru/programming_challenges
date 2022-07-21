"""
Solves 'chicken and rabbits' problem on CodingGames
"""
from typing import Tuple


def chickens_n_rabbits(heads: int, legs: int) -> Tuple[int, int]:
    """
    Takes number of heads and legs then return number of chickens and rabbits
    """
    rabbits, rem = divmod(legs, 4)
    chickens = rem // 2

    while (rabbits + chickens) != heads:
        rabbits -= 1
        chickens += 2

    return chickens, rabbits
