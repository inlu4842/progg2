from numba import njit
import matplotlib.pyplot as plt
import numpy as np
from person import Person
import time

def fib_py(n):
# Python Fibonacci without Numba
    if n <= 1:
        return n
    else:
        return fib_py(n - 1) + fib_py(n - 2)
    
# Numba-optimized Fibonacci
@njit
def fib_numba(n):
    if n <= 1:
        return n
    else:
        return fib_numba(n - 1) + fib_numba(n - 2)
    
def time_fib_py(n):
    start_time = time.perf_counter()
    fib_py(n)
    end_time = time.perf_counter()
    return end_time - start_time

def time_fib_numba(n):
    start_time = time.perf_counter()
    fib_numba(n)
    end_time = time.perf_counter()
    return end_time - start_time

def time_fib_cpp(n):
    f = Person(n)
    start_time = time.perf_counter()
    f.fib()
    end_time = time.perf_counter()
    return end_time - start_time

n_values = list(range(30, 46))
timings_py = [time_fib_py(n) for n in n_values]
timings_numba = [time_fib_numba(n) for n in n_values]
timings_cpp = [time_fib_cpp(n) for n in n_values]

plt.figure(figsize=(10, 6))
plt.plot(n_values, timings_py, label='Python Fibonacci')
plt.plot(n_values, timings_numba, label='Numba Fibonacci')
plt.plot(n_values, timings_cpp, label='C++ Fibonacci')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.legend()
plt.savefig('fib_timings.png')
    

def main():
     f = Person(5)
     print(f.get())
     f.set(8)
     print(f.get())

     python_fib8 = fib_py(8)
     print(f'Fib(8) using Python: {python_fib8}')

     numba_fib8 = fib_numba(8)
     print(f'Fib(8) using Numba: {numba_fib8}')

     print(f'Fib(8) using C++: {f.fib(8)}')

     #result = f.fib()
     #print(result)


if __name__ == '__main__':
	main()
    
