from projecteuler import utilities as utl


def solution():
    """
    A palindromic number reads the same both ways.
    The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    """

    ans = 0
    r = range(999, 100, -1)
    for x in r:
        for y in r:
            z = x * y
            if str(z) == str(z)[::-1] and z > ans:
                ans = z
    return ans


if __name__ == '__main__':
    assert str(solution()) == utl.get_answer(4)
