import math
import cProfile
import timeit
from matplotlib import pyplot


def prime(ind: int) -> []:
    if ind == 1:
        return 2

    i = 1
    number = 2
    while i < ind:
        number += 1
        for n in range(2, int(math.sqrt(number)) + 1):
            if not number % n:
                break
        else:
            i += 1

    return number


with cProfile.Profile() as profile:
    primes = []
    for index in range(1, 1000):
        primes.append(prime(index))

profile.print_stats()

# 3674996 function calls in 2.528 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 cProfile.py:133(__exit__)
#       999    2.112    0.002    2.528    0.003 impl_2.py:7(prime)
#   3672996    0.416    0.000    0.416    0.000 {built-in method math.sqrt}
#       999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


time_results = []
for index in range(1, 1000, 100):
    time_result = timeit.timeit(stmt=f"prime({index})", setup="from __main__ import prime", number=100)
    time_results.append(time_result)
    print(f'N = {index: >3d}: {time_result:.12f}')

# N =   1: 0.000006600000
# N = 101: 0.024544300000
# N = 201: 0.060799900000
# N = 301: 0.104256700000
# N = 401: 0.146682600000
# N = 501: 0.192845600000
# N = 601: 0.244885400000
# N = 701: 0.277393700000
# N = 801: 0.327189600000
# N = 901: 0.386499500000


time_results = []
for index in range(1, 10000, 100):
    time_result = timeit.timeit(stmt=f"prime({index})", setup="from __main__ import prime", number=10)
    time_results.append(time_result)

pyplot.xlabel('N, index')
pyplot.ylabel('Time, seconds')
pyplot.plot()
pyplot.plot(range(1, 10000, 100), time_results, label='prime')
pyplot.legend()
pyplot.show()
