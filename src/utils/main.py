from functools import wraps
import time


def stop_watch(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        start = time.time()
        result = func(*args, **kargs)
        elapsed_time = time.time() - start
        print(f"{func.__name__} took {elapsed_time} seconds")
        return result

    return wrapper


def load_file(file_path):
    input_data = []
    with open(file_path) as f:
        for line in f:
            input_data.append(line.rstrip('\n'))
    return input_data
