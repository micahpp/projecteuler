from projecteuler import util
import numpy as np


def solution():
    """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """

    n = np.arange(1, 21)
    i = 1

    while True:
        x = i / n
        if all(y.is_integer() for y in x):
            return i
        i += 1


if __name__ == '__main__':
    assert str(solution()) == util.get_answer(5)
