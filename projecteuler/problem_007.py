from projecteuler import utilities as utl


def solution():
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
    we can see that the 6th prime is 13.
    What is the 10001st prime number?
    """

    n = 64
    p = 2
    primes = []
    while len(primes) < 10001:
        for i in range(2, p):
            if p % i == 0:
                p += 1
                break
        else:
            primes.append(p)
            p += 1
    return primes[-1]


if __name__ == '__main__':
    assert str(solution()) == utl.get_answer(7)
