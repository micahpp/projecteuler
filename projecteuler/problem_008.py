from projecteuler import utilities as utl
from functools import reduce
from operator import mul


def solution():
    """
    The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
    Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
    What is the value of this product?
    """

    ans = 0
    with open('../data/problem_008_data.txt') as f:
        n = [int(x) for x in f.read().replace('\n', '')]

    for i in range(len(n)):
        tmp = reduce(mul, n[i:i + 13])
        if tmp > ans:
            ans = tmp
    return ans


if __name__ == '__main__':
    assert str(solution()) == utl.get_answer(8)
