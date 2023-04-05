
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

pin = "0644"
def pin_breaker():
    a = 0
    while True:
        yield str(a).zfill(4)
        a+=1


kodas = pin_breaker()

while True:
    kod = next(kodas)
    print(kod)
    if kod == pin:
        print(f"Pin kodas {kod} nulauztas.")
        break
