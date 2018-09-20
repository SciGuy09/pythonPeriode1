#Definieren van variabelen: '-' en '+'
s1 = '-'
s2 = '+'

#Expressies met de reeds gedefinieerde variabelen
a = s1 + s2
b = a
c = s2 + (s1 * 2)
d = (s2 + (s1 * 2)) * 2
e = (s2 + (s1 * 2)) * 10 + s2
f = ((s2 + s1) + (s2 * 3) + (s1 * 2) + s2) * 3 + (s2 + s1) + (s2 * 3) + (s1 * 2)

#Afdrukken van waarden op scherm
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)