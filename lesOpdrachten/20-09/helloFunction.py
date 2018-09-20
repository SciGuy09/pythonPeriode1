def hello(naam):
    print("Welcome, " + naam.strip() + ", to the world of python!")

invoerNaam = input('Geef je naam in: ')
hello(invoerNaam)

def rng(getallenLijst):
    'Bla'
    resultaat = max(getallenLijst) - min(getallenLijst)
    return resultaat

getallenLijst = [6, -8, 5]
print(rng(getallenLijst))

help(rng)