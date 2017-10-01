from projecteuler import utilities as utl


def solution():
    """
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    """

    i, n = 2, 600851475143
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


if __name__ == '__main__':
    assert str(solution()) == utl.get_answer(3)
