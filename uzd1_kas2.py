"""
1.
Parašykite generatorių, kuris kaskartą inicijuotas su funkcija next grąžintų sekantį porinį skaičių.
Pirmas sk. 2, toliau 4 ir taip be pabaigos.
"""
from time import sleep

def kas_du():
    count = 1
    while count:
        yield count*2
        count +=1


counter = kas_du()
print(next(counter))
print(next(counter))
print(next(counter))

def poriniai():
    number = 2
    while True:
        yield number
        number += 2

por = poriniai()
while True:
    print(next(por))
    sleep(0.1)
# print(next(por))
# print(next(por))
# print(next(por))

g = (num*2 for num in range(100))
print(type(g))
print(list(g))

