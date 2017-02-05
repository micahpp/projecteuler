from timeit import default_timer as timer

def time_problem(problem):
    start = timer()
    print(problem.__name__, problem())
    print('time elapsed:', timer() - start)
 
