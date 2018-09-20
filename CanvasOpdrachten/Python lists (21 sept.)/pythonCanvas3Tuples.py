#Opdracht 3 tuples

#definieren lijst tuples
tuple = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')

#Definieren van variabel met het type lijst
lijst = []

#Ljist uitbreiden met hoeveelheid aan A's
lijst.append(tuple.count('A'))
#Ljist uitbreiden met hoeveelheid aan B's
lijst.append(tuple.count('B'))
#Ljist uitbreiden met hoeveelheid aan C's
lijst.append(tuple.count('C'))
#Afdrukken lijst met aantallen van de verschillende A's, B's en C's in de lijst
print(lijst)