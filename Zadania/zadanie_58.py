"""
Liczbę nazywamy iloczynowo-pierwszą jeżeli iloczyn jej cyfr w systemie o podstawie b jest
liczbą pierwszą. Na przykład: 13 jest liczbą iloczynowo-pierwszą w systemie dziesiętnym, bo 1 ∗ 3 = 3 16 jest
liczbą iloczynowo-pierwszą w systemie trójkowym, bo 16 = 121(3), 1 ∗ 2 ∗ 1 = 2 W liczbie naturalnej możemy
dokonywać rotacji jej cyfr, np. 1428, 4281, 2814, 8142 albo 209, 092, 920.

Proszę napisać funkcję, która dla danej liczby naturalnej N,
zwróci najmniejszą podstawę systemu (z zakresu 2-16) w którym przynajmniej
jedna z rotowanych liczb jest iloczynowo-pierwsza albo wartość None gdy taka podstawa nie istnieje.
"""

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

def dec_to_X(x, base):
   tab = []
   while x > 0:
        tab.append(x % base)
        x //= base
   return tab[::-1] if tab else [0]

def rotations(tab):
    # for i in range(len(tab)):
    #     tab[i:] + tab[:i]
    return [tab[i:] + tab[:i] for i in range(len(tab))]

# w = [3, 2, 1, 4, 7, 9]
# print([w[i:] + w[:i] for i in range(len(w))])

number = int(input("Wprowadź liczbę: "))
for base in range(2, 17):
    new_num = dec_to_X(number, base)
    for i in rotations(new_num):
        multi = 1
        for r in i:
          multi *= r
        if is_prime(multi):
            print(base)
            exit()
print(None)
