#Definieren van lijst
flowers = ['rose', 'bougainvillea', 'yucca', 'marigold', 'daylilly', 'lilly of the valley']

#Expressie checkend of het woord 'potato' in lijst voorkomt
potatoInList = 'potato' in flowers

#Definites van sublijsten
thorny = flowers[0:3]
poison = flowers[5:6]
dangerous = thorny + poison

#Afdrukken van sublijsten op scherm
print(thorny)
print(poison)
print(dangerous)
