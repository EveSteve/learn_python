# Aufgabe 1: Schreibe einen Algortihmus, der die Fakultät einer Zahl errechnet (z.B. 5!). Gehe dazu zuerst von einer festen Zahl aus.

# ausgangszahl = 5
#
# ergebnis = 1
# # TODO, Tipp: for-Schleife mit Range
#
# print("Die Fakultät von", ausgangszahl, "lautet: ", ergebnis)


# Aufgabe 1.1: Lasse nun die Zahl, deren Fakultät berechnet werden soll, durch den Benutzer eingeben.



# Aufgabe 1.2: Schreibe den Code nun so um, dass die Berechnung der Fakultät in einer Funktion stattfindet.



# Aufgabe 2: Schreibe einen Algorithmus, der prüft, ob eine Zahl eine Primzahl ist.
# siehe auch: http://schuljahr.inf-schule.de/2019-20/programmierung/funktional/projekte/primzahlen/primzahltest

# ALGORITHMUS istPrimzahl:
#   Übergabe: n    # natürliche Zahl
#   prim = True
#   k = 2
#   SOLANGE k < n:
#       WENN n % k == 0:
#           prim = False
#       k = k+1
#   Rückgabe: prim

# Aufgabe 2.1: Lasse nun die Zahl, die darauf geprüft werden soll, ob sie eine Primzahl ist, durch den Benutzer eingeben.


# Aufgabe 2.2: Schreibe den Code nun so um, dass die Prüfung in einer Funktion stattfindet.


# Aufgabe 3: Übersetze diesen Pseudocode in eine Python-Funktion, die die Gesamtkosten eines Produkts bestimmt


# PROCESS BerechneKosten
#     INPUT preis, anzahl
#     SET kosten = preis * anzahl
#     RETURN kosten
# END

# TODO def ....

# name = input("Name des Produkts: ")
# preis = input("Preis des Produkts: ")
# anzahl = input("Anzahl des Produkts: ")

# print("Die Gesamtkosten von", anzahl, "Stück", name, "à", preis, "Euro sind: ", TODO)


# Aufgabe 4: Übersetze diesen Pseudocode in eine Python-Funktion, welches eine Liste von Zahlen nimmt, und
# die Summe aller Zahlen ausgibt.

# PROCESS FindTotal
#     INPUT listOfNumbers
#     SET sum = 0
#     FOR EACH number IN listOfNumbers
#     SET sum = sum + number
#     END FOR
#     PRINT sum
# END


# Aufgabe 5: Übersetze diesen Pseudocode in ein Python-Programm, welches den Nutzer je nach Tageszeit
# auf andere Art und Weise begrüßt. Der Code zum Auslesen der aktuellen Stunde ist unten bereits angegeben

# PROCESS TimedGreeting
#     GET userTime
#     IF userTime > 6:00 + < 12:00
#     PRINT "Guten Morgen!"
#     ELSE IF userTime > 12:00 + < 18:00
#     PRINT "Guten Tag!"
#     ELSE
#     PRINT "Guten Abend!"
# END

# import datetime
#
# aktuelle_stunde = datetime.datetime.now().hour
# print(aktuelle_stunde)
