def factorization(n):
    divisors = []
    i = 2
    while n > 1:
        if n % i == 0:
            divisors.append(i)
            n = n // i
        else:
            i += 1
    return divisors

def countingnums(n):
    suma = 0
    while n > 0:
        suma = suma + n % 10
        n //= 10
    return suma

def bool_is_smith(n):
    sum_left = countingnums(n)
    tab = factorization(n)
    sum_right = 0
    for i in tab:
        sum_right += countingnums(i)
    return sum_left == sum_right

print(bool_is_smith(85))
