#Opdracht 1 If statement
#Declareren van user variables
scoreToets = eval(input('Enter score: '))

#Checken van voorwaarden (moet voldoen aan een minimum van 15 punten.
if scoreToets > 15:
    print('Gefeliciteerd!\nMet een score van {} ben je geslaagd!'.format(scoreToets))

#Wanneer het tweede print statement onder de i zou worden geplaatsts (zonder ident), dan wordt de tekst hoe dan ook afgedrukt. Deze behoort dan niet tot het if statement.

a = 3 % 6

print(a)