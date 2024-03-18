import multiprocessing
import time


def factorize(*numbers):
    factors = []
    for num in numbers:
        num_factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                num_factors.append(i)
        factors.append(num_factors)
    return factors


"""----------------------------------"""


def find_factors(num):
    num_factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            num_factors.append(i)
    return num_factors


# test 3.2
def multi_process_factorize(*numbers):
    with multiprocessing.Pool() as pool:
        factors = pool.map(find_factors, numbers)
    return factors


if __name__ == "__main__":
    start_time = time.time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    print(f'1 thread: - {time.time() - start_time} seconds')
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]

    start_time = time.time()
    a, b, c, d = multi_process_factorize(128, 255, 99999, 10651060)
    print(f'Thread pool: - {time.time() - start_time} seconds')

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]
