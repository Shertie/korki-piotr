"""
Obcięcie” liczby naturalnej polega na usunięciu z niej M początkowych i N końcowych
cyfr, gdzie M, N >= 0. Proszę napisać funkcję, która dla danej liczby naturalnej K zwraca największą liczbę
pierwszą o różnych cyfrach jaką można uzyskać z obcięcia liczby K albo 0 gdy taka liczba nie istnieje. Na
przykład dla liczby 1202742516 spośród obciętych liczb pierwszych: 2,5,7,251,2027 liczbą spełniającą warunek
jest liczba 251.
"""
def has_unique_digits(n):
    digits = str(n)
    return len(digits) == len(set(digits))



def is_prime(n):
    n = int(n)
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n == 3:
        return True
    if n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

# 2315

def slicing(K):
    if not K or not K.isdigit():
        return 0

    maximum_prime = 0
    for m in range(len(K) + 1):          # w = range(5) => w[0] = 0
        for n in range(len(K) + 1 - m):
            actual_prime = K[m:len(K) - n]
            if actual_prime and is_prime(actual_prime):
                num = int(actual_prime)
                if has_unique_digits(num):
                    maximum_prime = max(maximum_prime, int(actual_prime))
    return maximum_prime


K = input("Wprowadź liczbę: ")
print(slicing(K))