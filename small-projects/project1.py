# zahl = 5
# zeichenkette = '5'
# kommazahl = 1.333
# wahrheitswert = False
# liste = [1,2,'3',4,5]
# print(liste)
# print(type(liste))
#
# i = 0
#
# while i < 5:
#     print(i)
#     i += 1


nummer = int(input('Gib eine Zahl zwischen 100 und 500 ein: '))
while nummer < 100 or nummer > 500:
    print('Falsche Nummer, gib eine korrekte Nummer ein!')
    nummer = int(input('Gib eine Zahl zwischen 100 und 500 ein: '))
else:
    print("Eingegebene Zahl ist korrekt: ", nummer)