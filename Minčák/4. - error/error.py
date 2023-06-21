def factorial(x):
    if x < 0:
        raise ValueError("Argument je záporný")
    if x > 10:
        raise ValueError("Príliš vysoká hodnota")
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial(5))
