import timeit
import sys
sys.setrecursionlimit(5000)

fib_cache = {0: 0, 1: 1}

def fib(n):
    if n in fib_cache:
        return fib_cache[n]

    fib_cache[n] = fib(n-1) + fib(n-2)
    return fib_cache[n]

if __name__ == "__main__":
    n = input("Enter the term you would like to find the result of: ")
    n = int(n)
    result = fib(n)
    print(f"{result} is term {n}")

    elapsed_time = timeit.timeit(lambda :fib(n), number=1000)

    print("Elapsed time:", elapsed_time)