from projecteuler import utils as utl


def problem_1():
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    return sum([x for x in range(1000) if not x % 3 or not x % 5])


def problem_2():
    """
    Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    ans = 0
    fib = [1, 1]
    while fib[1] < 4000000:
        x = sum(fib)
        if not x % 2:
            ans += x
        fib = [fib[1], x]
    return ans


def problem_3():
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


def problem_4():
    """
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
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


def problem_5():
    """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """
    import numpy as np
    n = np.arange(1, 21)
    i = 1

    while True:
        x = i/n
        if all(y.is_integer() for y in x):
            return i
        i += 1


def problem_6():
    """
    The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 552 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    """
    sum_of_sqr = sum([i**2 for i in range(101)])
    sqr_of_sum = sum(range(101))**2
    return sqr_of_sum - sum_of_sqr


def problem_7():
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10001st prime number?
    """
    n = 64
    p = 2
    primes = []
    while len(primes) < 10001:
        for i in range(2, p):
            if p % i == 0:
                p+= 1
                break
        else:
            primes.append(p)
            p += 1
    return primes[-1]


def problem_8():
    """
    The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
    Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
    """
    from functools import reduce
    from operator import mul
    ans = 0
    f = open('data/p8_data.txt')
    n = [int(x) for x in f.read().replace('\n', '')]
    f.close()

    for i in range(len(n)):
        tmp = reduce(mul, n[i:i+13])
        if tmp > ans:
            ans = tmp
    return ans


def problem_9():
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """
    goal = 1000

    for a in range(1, goal+1):
        for b in range(a+1, goal+1):
            c = goal - a - b
            if a**2 + b**2 == c**2 and sum((a, b, c)) == goal:
                return a * b * c


def problem_10():
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
    """
    primes = utl.prime_sieve(2000000)
    return sum(primes)


def problem_11():
    """
    In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
    The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
    What is the greatest product of four adjacent numbers in the same direction
    (up, down, left, right, or diagonally) in the 20×20 grid?
    """
    from functools import reduce
    from operator import mul

    ans = 0

    # create grid
    grid = [[int(x) for x in line.split()] for line in open("data/p11_data.txt")]

    for i in range(len(grid)):
        for j in range(len(grid)):
            # i = row, j = column

            # horizontal
            tmp = reduce(mul, grid[i][j:j+4])
            if tmp > ans:
                ans = tmp

            # vertical
            v_bound = min(i+4, len(grid))
            tmp = []
            for k in range(i, v_bound):
                tmp.append(grid[k][j])
            tmp = reduce(mul, tmp)
            if tmp > ans:
                ans = tmp

            # down & right
            tmp = []
            h_bound = min(j+4, len(grid))
            for k, l in zip(range(i, v_bound), range(j, h_bound)):
                tmp.append(grid[k][l])
            tmp = reduce(mul, tmp)
            if tmp > ans:
                ans = tmp

            # down & left
            tmp = []
            h_bound = max(-1, j-4)
            for k, l in zip(range(i, v_bound), range(j, h_bound, -1)):
                tmp.append(grid[k][l])
            tmp = reduce(mul, tmp)
            if tmp > ans:
                ans = tmp
    return ans


def problem_12():
    """
    The sequence of triangle numbers is generated by adding the natural numbers.
    So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
    Let us list the factors of the first seven triangle numbers:
     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28
    We can see that 28 is the first triangle number to have over five divisors.
    What is the value of the first triangle number to have over five hundred divisors?
    """
    tmp, i = 0, 1
    while True:
        tmp += i
        factors = utl.factors(tmp)
        if len(factors) > 500:
            return tmp
        i += 1


def problem_13():
    """
    Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
    """
    tmp = sum([int(x.rstrip()) for x in open('data/p13_data.txt').readlines()])
    ans = str(tmp)[:10]
    return ans


def problem_14():
    """
    The following iterative sequence is defined for the set of positive integers:
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)
    Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
    Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
    Which starting number, under one million, produces the longest chain?
    NOTE: Once the chain starts the terms are allowed to go above one million.
    """
    ans = 0

    def aux(n):
        tmp = [n]
        while tmp[-1] != 1:
            n = 3*n+1 if n % 2 else n//2
            tmp.append(n)
        return len(tmp)

    for i in range(1000000):
        if not i % 100: print("working...")
        tmp = aux(i)
        if tmp > ans:
            ans = tmp

    return ans

if __name__ == '__main__':
    utl.time_problem(problem_14)
