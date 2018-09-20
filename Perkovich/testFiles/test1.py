from fractions import Fraction

fahrenheit = eval(input('Enter degrees in Fahrenheit: '))

celsius = Fraction(5, 9) * (fahrenheit - 32)

print('Temperature in degree celsius is equivalent to: {}'.format(celsius))
