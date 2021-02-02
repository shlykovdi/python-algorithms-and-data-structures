import cProfile
import timeit
from matplotlib import pyplot


def sieve(ind: int) -> []:
    n = ind * 20
    numbers = [value for value in range(n)]
    numbers[1] = 0

    for i in range(2, n):
        if not numbers[i]:
            continue

        for j in range(i * i, n, i):
            numbers[j] = 0

    return tuple(value for value in numbers if value)[ind - 1]


with cProfile.Profile() as profile:
    primes = []
    for index in range(1, 1000):
        primes.append(sieve(index))

profile.print_stats()

# 1206309 function calls in 1.540 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 cProfile.py:133(__exit__)
#   1203310    0.184    0.000    0.184    0.000 impl_1.py:18(<genexpr>)
#       999    1.177    0.001    1.540    0.002 impl_1.py:6(sieve)
#       999    0.180    0.000    0.180    0.000 impl_1.py:8(<listcomp>)
#       999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


time_results = []
for index in range(1, 1000, 100):
    time_result = timeit.timeit(stmt=f"sieve({index})", setup="from __main__ import sieve", number=100)
    time_results.append(time_result)
    print(f'N = {index: >3d}: {time_result:.12f}')

# N =   1: 0.000378200000
# N = 101: 0.026958300000
# N = 201: 0.053521200000
# N = 301: 0.079728100000
# N = 401: 0.106258400000
# N = 501: 0.132602200000
# N = 601: 0.161098400000
# N = 701: 0.190198900000
# N = 801: 0.224029500000
# N = 901: 0.250583300000


time_results = []
for index in range(1, 10000, 100):
    time_result = timeit.timeit(stmt=f"sieve({index})", setup="from __main__ import sieve", number=10)
    time_results.append(time_result)

pyplot.xlabel('N, index')
pyplot.ylabel('Time, seconds')
pyplot.plot()
pyplot.plot(range(1, 10000, 100), time_results, label='sieve')
pyplot.legend()
pyplot.show()
