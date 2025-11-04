def square(x, N):
    """
    Proszę napisać program, który wyznacza wartość pierwiastka kwadratowego
    z liczby naturalnej x z dokładnością do N miejsc dziesiętnych po przecinku.
    Program powinien działać poprawnie dla

    x < 108
    N < 100

    Args: x float, N integer
    In: Number
    Out: Approximation of square root of n
    """
    if x >= 108:
        return "Error: x >= 108"
    if N >= 100:
        return "Error: N >= 100"

    tab = []
    root = x ** 0.5
    approximation_num = round(root * (10 ** N))
    while approximation_num > 0:
        tab.append(approximation_num % 10)
        approximation_num //= 10
    return tab
x = int(input())
N = int(input())
number = (square(x, N))
number.reverse()
print(number)
print(f"{number[0]}. {''.join(map(str, number[1:]))}")