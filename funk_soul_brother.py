#!/usr/bin/python
import math

# zerowanie danych
y=0
#tabela danych
baza = [[1,2,1],[8,8,7],[3,1,8]]
wejscie = [8,7,2]
nazwa = ["katar","angina","grypa"]
#definicje funkcji
maxior = lambda a,b: a if (a > b) else b
minimal = lambda a,b: a if (a < b) else b
# wynik = map(minimal(baza,wejscie), len(wejscie))


#testy i czesc imperatywna


# print maxior (2, 4)


for j in range(len(baza)):
    for i in range(len(wejscie)):
        x = minimal(wejscie[i],baza[j][i])
        y = maxior(y,x)   
    print nazwa[j]
    print y 
    print "\n"
    y=0
