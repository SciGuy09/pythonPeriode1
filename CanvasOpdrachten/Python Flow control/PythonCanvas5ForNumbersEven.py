#Opdracht 5 For, If & Numbers
#Declaratie van getallenlijst:
getallenLijst = [1, 33, -34, -83, 8, 98]

#Opzetten 'for' loop:
for getal in getallenLijst:
    #Checken of het getal even is:
    if getal % 2 == 0:
        #Afdrukken even getal
        print(getal)