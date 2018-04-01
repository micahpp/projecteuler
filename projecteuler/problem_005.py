import numpy as np
from projecteuler import util

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def solution():
    dividend = 11
    divisors = np.arange(1, 21)
    while True:
        quotients = dividend / divisors
        if all(x.is_integer() for x in quotients):
            return dividend
        dividend += 1


if __name__ == "__main__":
    assert str(solution()) == util.get_answer(5)
