#program który oblicza odległość do horyzontu z podpunktami


import math

#wysokosc klawiatury 1.2
#Wysokosc osoby 1.65 m
#Wysokość wzroku ok 1.55 m

h = [1.2, 1.55, 20] #m 
#element 0 to wysokosc klawiatury
#element 1 to wysokosc wzroku
#element 2 to wysokosc 20m

a = 3.57 * math.sqrt(h[0])
b = 3.57 * math.sqrt(h[1])
c = 3.57 * math.sqrt(h[2])

print ('Odległość do horyzontu z wysokosci klawiatury wynosi', round(a, 2), 'km')
print ('Odległość do horyzontu z wysokosci  wzroku', round(b, 2), 'km')
print ('Odległość do horyzontu z wysokosci 20m-budynku wynosi', round(c, 2), 'km')
