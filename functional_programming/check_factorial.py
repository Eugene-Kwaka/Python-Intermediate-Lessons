def find_factorial_looping(n):
    if n < 0:
        return 0
    else:
        factorial = 1
        for i in range(1, n+1):
            factorial = factorial * i
    return factorial

print(find_factorial_looping(5)) 