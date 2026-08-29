def fibonacci(x):
    if x <= 1:
        return 1

    return fibonacci(x-2) + fibonacci(x-1)

print(fibonacci(4))