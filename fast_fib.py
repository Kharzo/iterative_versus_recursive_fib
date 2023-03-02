import timeit

def fib(n):
    memo = {0: 0, 1: 1}
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

if __name__== '__main__':
    n = input("Enter the term you would like to find the result of: ")
    n = int(n)
    result = fib(n)
    print(f"{result} is term {n}")

    elapsed_time = timeit.timeit(lambda :fib(n), number=1000)

    print("Elapsed time:", elapsed_time)