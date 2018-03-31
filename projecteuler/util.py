import json
from pathlib import Path
from timeit import default_timer as timer


# TODO: add n_primes function that returns a list of n primes

project_path = Path(__file__).parents[1]
answers_path = Path(project_path, "data/answers.json")

with open(answers_path) as f:
    answers = json.load(f)


def get_answer(n):
    return answers.get(str(n))


def time_problem(problem):
    """runs and times a function"""
    start = timer()
    print(problem.__name__, problem())
    print('time elapsed:', timer() - start)


def prime_sieve(n):
    """ returns a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def factors(n):
    """returns the factors of n"""
    return [i for i in range(1, n // 2 + 1) if not n % i] + [n]


if __name__ == '__main__':
    print(get_answer(1))
