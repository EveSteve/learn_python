
# Aufgabe 1
# Es gibt eine Liste mit den Zahlen von 1 bis 5. Drucke für jede Zahl die Quadratzahl aus
nummern = [1, 2, 3, 4, 5]

for i in nummern:
    # TODO:
    # quadrat = ...


# Aufgabe 2
# Die Zahlen von 1 bis 10 sollen gedruckt werden. Für jede Zahl die Information, ob es eine gerade, oder ungerade Zahl ist.

for i in range(1, 11):
    if i % 2 == 0:
        # TODO
    else:
        # TODO

# Aufgabe 3
# Zähle die Menge an Zahlen in der Liste mithilfe eines for-Loops

numbers = [12,3,56,67,89,90]


# man kann auch len(numbers) benutzen, um diese Zahl zu erhalten

# Aufgabe 4
# Lasse die Schleife laufen, solange der Zähler kleiner 3 ist

zaehler = 1
# while TODO:
    print(zaehler)
    zaehler = zaehler + 1

# Aufgabe 5
# Finde heraus, wie oft eine Zahl durch 3 geteilt werden kann, bevor sie kleiner oder gleich 10 ist

zaehler = 0
nummer = 180
while nummer > 10:
    # Teile die Zahl durch 3
    # TODO
    # Erhöhe den Zähler
    # TODO
print('Anzahl Teilungen: ', zaehler)

# Aufgabe 6
# Der Benutzer soll eine Zahl eingeben. Ist diese nicht zwischen 100 und 500, wird der Benutzer erneut aufgefordert, eine Zahl einzugeben.
# Ist die Zahl zwischen 100 und 500, wird die korrekte Zahl ausgegeben und das Programm ist vorbei.

nummer = int(input('Gib eine Zahl zwischen 100 und 500 ein: '))
# while TODO
    print('Falsche Nummer, gib eine korrekte Nummer ein!')
    nummer = int(input('Gib eine Zahl zwischen 100 und 500 ein: '))
else:
    print("Eingegebene Zahl ist korrekt: ", nummer)