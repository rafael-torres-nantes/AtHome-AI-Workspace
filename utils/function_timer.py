import time
from functools import wraps

def time_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Tempo para {func.__name__}: {end_time - start_time:.2f} segundos")
        return result
    return wrapper