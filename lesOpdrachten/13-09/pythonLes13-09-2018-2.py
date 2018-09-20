#Import math module
import math

#Definieren variabelen
a = math.sqrt(pow(3, 2) + pow(4, 2))
b = a > 5
c = math.pi * math.pow(10, 2)

#Definieren van x coordinaten op basis van de gebruikersinput
xCoor = 5
#Definieren van y coordianten op basis van de gebruikersinput.
yCoor = 5

CircleRadius = 7

#Expressie
d = math.sqrt(math.pow(xCoor, 2) + math.pow(yCoor, 2))

#Afdrukken waarden
print(a)
print(b)
print(c)

if (d <= 7):
    print('Dart is within the radius of the board')
else:
    print('Out of range')
