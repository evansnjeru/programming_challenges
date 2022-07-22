"""
The game mode is REVERSE: You do not have access to the statement. You have to
guess what to do by observing the following set of tests:
    01
    Test 1
    Input
    Expected output

    1

    1

    02
    Test 2
    Input
    Expected output

    10

    123456789101234567891012345678910123456789101234567891012345678910123456789
    10123456789101234567891012345678910

    03
    Test 3
    Input
    Expected output

    12

    123456789101112123456789101112123456789101112123456789101112123456789101112
    123456789101112123456789101112123456789101112123456789101112123456789101112
    123456789101112123456789101112

    04
    Test 4
    Input
    Expected output

    6

    123456123456123456123456123456123456


"""


def looper(num: int) -> str:
    """
    Solves the problem above
    """
    accu = ""

    for i in range(num):
        accu += str(i + 1)

    accu *= num

    return accu
