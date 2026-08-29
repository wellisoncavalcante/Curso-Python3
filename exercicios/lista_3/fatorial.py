def fatorial(x):
    if x <= 1:
        return 1

    return x * fatorial(x-1)

print(fatorial(8))