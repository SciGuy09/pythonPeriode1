#Opdracht 1 getal - stringconversie

#Definieren van variabelen
cijferIOOR = 6.5
cijferPROG = 7.5
cijferCSN = 7

#Expressies omvattende het berekenen van het gemiddelde cijfer
gemiddeldeCijfer = (cijferIOOR + cijferPROG + cijferCSN) / 3
#Expressie omvattende de berekening van de totale beloning
totaleBeloning = (cijferIOOR * 30) + (cijferPROG * 30) + (cijferCSN * 30)

#Afdrukken van gemiddelde cijfer en de totale beloning
print('Mijn cijfers (gemiddeld een {}) leveren een bedrag van {} euro op!'.format(gemiddeldeCijfer, totaleBeloning))