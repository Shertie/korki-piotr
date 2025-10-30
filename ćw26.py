"""
Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego.

In : integer n
Find out if n is product of 2 fibonacci numbers.
Out: bool
"""

def fib(n):
    tab = [0, 1]
    for i in range(2, n+1):
        tab.append(tab[i-1] + tab[i-2])
    return tab

n = int(input("Podaj liczbę: "))
tab = fib(n)
is_ok = False
for i in tab:
    for j in range(i, len(tab)):
        if tab[i] * tab[j] == n:
            is_ok = True
            print("TAK!")
if not is_ok:
    print("NIE!")

