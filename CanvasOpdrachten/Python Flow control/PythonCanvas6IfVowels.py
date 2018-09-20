#Opdracht 6 For, If % Vowels

#Declaratie string:
s = 'Guido van Rossom heeft programmeertaal Python bedacht.'
klinker = 'aeiou'

#Opzetten 'for' loop
for letter in s:
    #Checken of letter klinker is
    if letter in klinker:
        #Afdrukken van resultaat
        print(letter)