"""
3.
Įsivaizduokite, kad reikia nulaužti 4 skaitmenų pin kodą.
Parašykite generatorių, kuris tikrins po viena kombinaciją, pradedant 0000, ir sustos,
kai pin kodas bus teisingas.
Pradėkite programą nuo (pvz.) PIN = '0549' ir rašykite toliau.
Pabaigus funkciją, praiteruokite sukurtą generatorių su for ciklu,
kad spausdintų skaičiukus iš eilės ir atspausdinus paskutinį, parašytų
'PIN is XXXX(jųsų pin'as)'. ' \
Atkreipkite dėmesį, kad kodas gali prasidėti nuliu. Sugalvokite, kaip apeiti šią problemą :).

"""

# pin = "0549"
#
# def kodas():
#     skaicius=0
#     while True:
#         if skaicius != int(pin):
#             yield skaicius
#             skaicius += 1
#         else:
#             print(skaicius)
#             break
#
#
#
# sk = kodas()
# sarasas=list(sk)
# print(sarasas)
# print(next(sk))
# print(next(sk))
# print(next(sk))

print("===================================================================")

pin = "0549"


def kodas():
    sk = ''
    skaicius = 0
    while sk != pin:

        if len(str(skaicius)) < 4:
            sk = ("0" * (4 - len(str(skaicius)))) + str(skaicius)
            yield sk

        else:
            sk = str(skaicius)
            yield sk
        skaicius += 1
    # print(sk)


kod = kodas()

while True:
    try:
        print(next(kod))
    except StopIteration:
        break

sarasas=list(kod)
print(sarasas)
print(next(kod))
print(next(kod))
print(next(kod))
