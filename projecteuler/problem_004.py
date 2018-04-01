import numpy as np
from projecteuler import util


def is_palindrome(value):
    return str(value) == str(value)[::-1]


def solution():
    """
    A palindromic number reads the same both ways.
    The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    greatest = 0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            product = i * j
            if is_palindrome(product) and product > greatest:
                greatest = product
    return greatest


def solution1():
    r = np.arange(100, 1000)
    products = np.multiply.outer(r, r)
    palindromes = [x.tolist() for x in np.nditer(products) if is_palindrome(x)]
    return max(palindromes)


if __name__ == '__main__':
    answer = util.get_answer(4)
    assert str(solution()) == answer
    assert str(solution1()) == answer
