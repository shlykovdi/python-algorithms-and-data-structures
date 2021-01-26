import numba
import time


@numba.njit(parallel=True)
def search_numbers(search_range: int, check_range: int) -> int:
    counter = 0

    for a in numba.prange(2, search_range):
        for b in numba.prange(2, check_range):
            if a % b:
                break
        else:
            counter += 1

    return counter


def timeit(search_range: int, check_range: int, number: int = 1000) -> float:
    time_sum = 0.0
    for _ in range(number):
        start = time.time()
        search_numbers(search_range, check_range)
        time_sum += time.time() - start

    return time_sum / number


def search_range_factory() -> range:
    return range(0, 100001, 5000)


# first compile and cache
search_numbers(0, 0)


def test() -> []:
    time_results = []

    for n in search_range_factory():
        print(f'n = {n}: ', end='')
        time_result = timeit(n, 10, number=10000)
        time_results.append(time_result)
        print(f'{time_result:.12f} seconds')

    return (list(search_range_factory()), time_results)


if __name__ == '__main__':
    test()

# n = 0: 0.000007765913 seconds
# n = 5000: 0.000012991667 seconds
# n = 10000: 0.000019959235 seconds
# n = 15000: 0.000024386644 seconds
# n = 20000: 0.000031934762 seconds
# n = 25000: 0.000035781479 seconds
# n = 30000: 0.000040862012 seconds
# n = 35000: 0.000047829580 seconds
# n = 40000: 0.000052764964 seconds
# n = 45000: 0.000060893822 seconds
# n = 50000: 0.000066409874 seconds
# n = 55000: 0.000070764613 seconds
# n = 60000: 0.000077078915 seconds
# n = 65000: 0.000083030462 seconds
# n = 70000: 0.000088836789 seconds
# n = 75000: 0.000096530175 seconds
# n = 80000: 0.000101465535 seconds
# n = 85000: 0.000106038022 seconds
# n = 90000: 0.000112134671 seconds
# n = 95000: 0.000128319812 seconds
# n = 100000: 0.000124908638 seconds
