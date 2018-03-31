from projecteuler import util


def solution():
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
    """

    primes = util.prime_sieve(2000000)
    return sum(primes)


if __name__ == '__main__':
    assert str(solution()) == util.get_answer(10)
