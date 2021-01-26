import time


def search_numbers(search_range: int, check_range: int) -> int:
    counter = 0

    for a in range(2, search_range):
        for b in range(2, check_range):
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


def test() -> []:
    time_results = []

    for n in search_range_factory():
        print(f'n = {n}: ', end='')
        time_result = timeit(n, 10, number=100)
        time_results.append(time_result)
        print(f'{time_result:.12f} seconds')

    return (list(search_range_factory()), time_results)


if __name__ == '__main__':
    test()

# n = 0: 0.000000000000 seconds
# n = 5000: 0.001088678837 seconds
# n = 10000: 0.002162857056 seconds
# n = 15000: 0.003251543045 seconds
# n = 20000: 0.004325716496 seconds
# n = 25000: 0.005414392948 seconds
# n = 30000: 0.006459541321 seconds
# n = 35000: 0.007570004463 seconds
# n = 40000: 0.008651416302 seconds
# n = 45000: 0.009812688828 seconds
# n = 50000: 0.010603802204 seconds
# n = 55000: 0.011830391884 seconds
# n = 60000: 0.012817461491 seconds
# n = 65000: 0.013695678711 seconds
# n = 70000: 0.014711768627 seconds
# n = 75000: 0.015851271152 seconds
# n = 80000: 0.016867380142 seconds
# n = 85000: 0.018122994900 seconds
# n = 90000: 0.018943140507 seconds
# n = 95000: 0.019988272190 seconds
# n = 100000: 0.021193101406 seconds
