lst = [159.99, 160.00, 205.95, 128.83, 175.49]

lst.append(160.00)
print(lst)

b = lst.count(160.00)
c = min(lst)
d = lst.index(c)
e = lst.remove(c)
f = lst.sort()

print(lst)
print(b)
print(c)
print(d)
print(e)
print(f)

# Bij uitvoerfuncties geen variabelen declareren. Dit bespaard namelijk een hoop geheugen, en maakt zo de code een stuk sneller.
