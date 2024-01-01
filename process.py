import multiprocessing
import time

def factorize_worker(args):
    number, result_queue = args
    factors = [i for i in range(1, number + 1) if number % i == 0]
    result_queue.put((number, factors))

def factorize(*numbers):
    manager = multiprocessing.Manager()
    result_queue = manager.Queue()
    args_list = [(number, result_queue) for number in numbers]

    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        pool.map(factorize_worker, args_list)

    results = [result_queue.get() for _ in numbers]
    return results

def test_factorize():
    a, b, c, d = factorize(128, 255, 99999, 10651060)

    assert a == (128, [1, 2, 4, 8, 16, 32, 64, 128])
    assert b == (255, [1, 3, 5, 15, 17, 51, 85, 255])
    assert c == (99999, [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999])
    assert d == (10651060, [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060])

if __name__ == "__main__":
    start_time = time.time()
    test_factorize()
    end_time = time.time()

    print("Sync Execution Time:", end_time - start_time)

    start_time_parallel = time.time()
    results_parallel = factorize(128, 255, 99999, 10651060)
    end_time_parallel = time.time()

    print("Parallel Execution Time:", end_time_parallel - start_time_parallel)
