import time


def search_numbers(search_range: int, check_range: int) -> int:
    numbers = set(value for value in range(2, search_range))

    for b in range(2, check_range):
        for a in range(2, search_range):
            if a % b and a in numbers:
                numbers.remove(a)

    return len(numbers)


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

# n = 0: 0.000007259846 seconds
# n = 5000: 0.002308003902 seconds
# n = 10000: 0.004855539799 seconds
# n = 15000: 0.007439360619 seconds
# n = 20000: 0.009442532063 seconds
# n = 25000: 0.011394913197 seconds
# n = 30000: 0.013710184097 seconds
# n = 35000: 0.016366589069 seconds
# n = 40000: 0.018819758892 seconds
# n = 45000: 0.020997118950 seconds
# n = 50000: 0.023377728462 seconds
# n = 55000: 0.025932493210 seconds
# n = 60000: 0.028922767639 seconds
# n = 65000: 0.032718651295 seconds
# n = 70000: 0.035962924957 seconds
# n = 75000: 0.038699162006 seconds
# n = 80000: 0.037741117477 seconds
# n = 85000: 0.040266869068 seconds
# n = 90000: 0.042850687504 seconds
# n = 95000: 0.044810328484 seconds
# n = 100000: 0.047031235695 seconds
