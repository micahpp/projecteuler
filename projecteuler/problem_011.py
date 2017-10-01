from projecteuler import utilities as utl
from functools import reduce
from operator import mul


def solution():
    """
    In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
    The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
    What is the greatest product of four adjacent numbers in the same direction
    (up, down, left, right, or diagonally) in the 20×20 grid?
    """

    ans = 0

    # create grid
    grid = [[int(x) for x in line.split()] for line in
            open("../data/problem_011_data.txt")]

    for i in range(len(grid)):
        for j in range(len(grid)):

            # horizontal
            tmp = reduce(mul, grid[i][j:j + 4])
            if tmp > ans:
                ans = tmp

            # vertical
            v_bound = min(i + 4, len(grid))
            tmp = []
            for k in range(i, v_bound):
                tmp.append(grid[k][j])
            tmp = reduce(mul, tmp)
            if tmp > ans:
                ans = tmp

            # down & right
            tmp = []
            h_bound = min(j + 4, len(grid))
            for k, l in zip(range(i, v_bound), range(j, h_bound)):
                tmp.append(grid[k][l])
            tmp = reduce(mul, tmp)
            if tmp > ans:
                ans = tmp

            # down & left
            tmp = []
            h_bound = max(-1, j - 4)
            for k, l in zip(range(i, v_bound), range(j, h_bound, -1)):
                tmp.append(grid[k][l])
            tmp = reduce(mul, tmp)
            if tmp > ans:
                ans = tmp
    return ans


if __name__ == '__main__':
    assert str(solution()) == utl.get_answer(11)
