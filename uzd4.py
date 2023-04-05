"""
4.
Parašykite generatoriaus funkciją, kuri atidarytų nurodytą tekstinį failą,
ir grąžintų po vieną eilutę (tiesiog yield'inti ' reikės ne skaičių o kitą duomenų tipą.).
Reikės prisiminti darbą su failais :)

"""


def grazinti_eilute(failas):
    with open(failas, 'r+') as failas:
        for line in failas:
            yield line[:-1]


x = grazinti_eilute("tekstas.txt")
for i in x:
    print(i)