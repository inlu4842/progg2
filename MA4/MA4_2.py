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
    


def main():
     
     n_values = list(range(20, 30))
     #p_values = list(range(30, 40))
     timings_py = []
     timings_numba = []
     #timings_cpp = []
     
     for n in n_values:
          start_time = time.perf_counter()
          fib_numba(n)
          end_time = time.perf_counter()
          timings_numba.append(end_time - start_time)  
          
          start_time = time.perf_counter()
          fib_py(n)
          end_time = time.perf_counter()
          timings_py.append(end_time - start_time)        
          
          #f = Person(n)
          #start_time = time.perf_counter()
          #f.fibc()
          #end_time = time.perf_counter()
          #timings_cpp.append(end_time - start_time)

     #for p in p_values:
          #start_time = time.perf_counter()
          #fib_py(p)
          #end_time = time.perf_counter()
          #timings_py.append(end_time - start_time)

     plt.figure(figsize=(10, 6))
     plt.plot(n_values, timings_py, label='Python Fibonacci')
     plt.plot(n_values, timings_numba, label='Numba Fibonacci')
     #plt.plot(n_values, timings_cpp, label='C++ Fibonacci')
     plt.xlabel('n')
     plt.ylabel('Time (seconds)')
     plt.legend()
     plt.savefig('fib_timings_with_2030.png')

     #f = Person(5)
     #print(f.get())
     #f.set(8)
     #print(f.get()) #Now f = Person(8)

     #python_fib8 = fib_py(8)
     #print(f'Fib(8) using Python: {python_fib8}')
     #numba_fib8 = fib_numba(8)
     #print(f'Fib(8) using Numba: {numba_fib8}')
     #print(f'Fib(8) using C++: {f.fibc()}')




if __name__ == '__main__':
	main()
    
