"""
The king wants to share his wealth with a certain number of people N in his
kingdom, so he has provided a certain amount of gold coins A. Knowing that
each person who receives gold coins wants twice as much as the person before
him (and that the first person receives only one gold coin), has the king
provided enough gold coins to give to the N people in his kingdom.

ex :

    there are 3 people
    the king has 15 gold coins

    person 1 : 1 gold coin
    person 2 : 2 gold coins
    person 3 : 4 gold coins

    --> 1+2+4 = 7 <= 15, the king has enough gold coins
"""


def king_n_coins(subjects: int, coins: int) -> bool:
    """
    Solves the problem
    """
    total = 1
    nxt = 1

    for _ in range(subjects - 1):
        nxt *= 2
        total += nxt

    return total <= coins
