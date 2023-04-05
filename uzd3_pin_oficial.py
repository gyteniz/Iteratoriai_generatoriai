
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


# PIN = '1012'
#
# def pin_breaker():
#     num = 0
#     while num < 10000:
#         guess = f'{num:04}'
#         if guess == PIN:
#             print(f"{guess} That's your PIN!")
#             break
#         yield guess
#         num += 1
#
# gen = pin_breaker()
#
# while True:
#     try:
#         print(next(gen))
#     except StopIteration:
#         break

print("===================================================================================")
pinas = "0547"

counter = (f"{num:04}" for num in range(10000))
pin_list = list(counter)
for pin in pin_list:
    print(pin)
    if pin == pinas:
        print(f"PIN kodas yra: {pin}")
        break
