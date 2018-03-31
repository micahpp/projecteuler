from projecteuler import util


def solution():
    """
    Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
    """

    tmp = sum([int(x.rstrip()) for x in
               open('data/problem_013_data.txt').readlines()])
    ans = str(tmp)[:10]
    return ans


if __name__ == '__main__':
    assert str(solution()) == util.get_answer(13)
