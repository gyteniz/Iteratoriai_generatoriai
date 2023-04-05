"""
2.
Parašykite generatorių , kuris kas kartą generuotų po vieną Fibonačio sekos skaičių.
(Seka prasideda šiais skaičiais: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233.
Kiekvienas šios sekos skaičius lygus dviejų prieš jį einančių skaičių sumai, daugiau google:)

"""
import itertools


def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        suma = a + b
        a = b
        b = suma


sk = fibonacci()
print(next(sk))
print(next(sk))
print(next(sk))
print(next(sk))
print(next(sk))
print(next(sk))
print(next(sk))
print(next(sk))
print(next(sk))
print(next(sk))
print(next(sk))
print(next(sk))

print("=============================================================================")

def fibonacci_iki(imtis):
    skaicius1, skaicius2 = 0, 1
    while skaicius1 <= imtis:
        try:
            yield skaicius1
            skaicius1, skaicius2 = skaicius2, skaicius1 + skaicius2
        except StopIteration:
            print("Seka baigta")


numb = fibonacci_iki(10000)
sarasas = list(numb)
print(sarasas)

print("=============================================================================")

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

print("=============================================================================")