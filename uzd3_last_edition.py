
"""
3.
Įsivaizduokite, kad reikia nulaužti 4 skaitmenų pin kodą.
Parašykite generatorių, kuris tikrins po viena kombinaciją, pradedant 0000,
ir sustos, kai pin kodas bus teisingas.
Pradėkite programą nuo (pvz.) PIN = '0549' ir rašykite toliau.
Pabaigus funkciją, praiteruokite sukurtą generatorių su for ciklu,
kad spausdintų skaičiukus iš eilės ir atspausdinus paskutinį,
parašytų 'PIN is XXXX(jųsų pinas)'.
Atkreipkite dėmesį, kad kodas gali prasidėti nuliu.
Sugalvokite, kaip apeiti šią problemą :).

"""


def pin_breaker():
    num = 0
    while num < 10000:
        yield f"{num:04}"
        num += 1

PIN = '9999'

breaker = pin_breaker()

while True:
    spejimas = next(breaker)
    print(spejimas)
    if spejimas == PIN:
        print(f"Kodas {spejimas} nulaužtas")
        break
