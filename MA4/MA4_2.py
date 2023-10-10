#!/usr/bin/env python3
from numba import njit
import time
import matplotlib.pyplot as plt
import numpy as np
from person import Person

def main():
	f = Person(5)
	print(f.get())
	f.set(8)
	print(f.get())

if __name__ == '__main__':
	main()

def fib_py(n):
# Python Fibonacci without Numba
    if n <= 1:
        return n
    else:
        return fib_py(n - 1) + fib_py(n - 2)
    
# Numba-optimized Fibonacci
#@jit
def fib_numba(n):
    if n <= 1:
        return n
    else:
        return fib_numba(n - 1) + fib_numba(n - 2)