#importeren van library die betrekking heeft op de volgende aritmetica
import math

#Definieren van x coordinaten op basis van de gebruikersinput
xCoor = eval(input('Enter x coor: '))
#Definieren van y coordianten op basis van de gebruikersinput.
yCoor = eval(input('Enter y coor: '))
CircleRadius = 10

#Expressie
hypotenusa = math.sqrt(math.pow(xCoor, 2) + math.pow(yCoor, 2))

if (hypotenusa <= 10):
    print('Dart is within the radius of the board')
else:
    print('Out of range')

# (0, 0) => in range
# (10, 10) => out of range
# (6, 6) => within range
