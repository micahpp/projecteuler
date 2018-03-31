from projecteuler import util


def solution():
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """
    goal = 1000

    for a in range(1, goal + 1):
        for b in range(a + 1, goal + 1):
            c = goal - a - b
            if a ** 2 + b ** 2 == c ** 2 and sum((a, b, c)) == goal:
                return a * b * c


if __name__ == '__main__':
    assert str(solution()) == util.get_answer(1)
