def factorial(x):
    if x < 0:
        raise ValueError("Argument je záporný")
    if x > 10:
        raise ValueError("Príliš vysoká hodnota")
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

print(factorial(60))
