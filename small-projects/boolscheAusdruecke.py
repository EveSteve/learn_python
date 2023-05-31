# Aufgabe 1
# Prüfe, ob folgende Ausdrücke TRUE oder FALSE ergeben

print(3 > 4) # TODO True oder False?

print("Hallo Welt" > "Hallo") # TODO True oder False?

print(4 != 5) # TODO True oder False?

print("Hallo" == "Hallo Welt") # TODO True oder False?

print("Hallo Welt" > "Hallo" and 3 > 4) # TODO True oder False?

print("Hallo Welt" > "Hallo" or 3 > 4) # TODO True oder False?

print(not "Hallo Welt" >= "Hallo Welt") # TODO True oder False?

print(not not 5 == 5) # TODO True oder False?

print(not 3 >= 4 and not 4 >= 5) # TODO True oder False?

# Aufgabe 2
# Was kommt hier heraus?

a = 6
b = 10
print( a == 10 or b == 10 ) # TODO True oder False?
print( not ( not a == 10 or not b == 10) ) # TODO True oder False?

# Aufgabe 3
# Was muss an den markierten Stellen eingetragen werden?

x = 10
if x TODO 0:
    print("Wert ist größer als 0.")
elif x TODO 0:
    print("Wert ist kleiner als 0.")
else:
    print("Wert ist 0.")


# Aufgabe 4
# Das folgende Programm benutzt zwei geschachtelte if Verzweigungen. Schreibe das Programm um, so dass es mit einer einzelnen Verzweigung auskommt

zahl = int(input("Gib eine Zahl ein: "))
if zahl % 2 == 0:
    if zahl % 3 == 0:
        print("Die eingegebene Zahl ist durch drei und zwei teilbar.")
    else:
        print("Die eingegebene Zahl ist nicht durch drei und zwei teilbar.")
else:
    print("Die eingegebene Zahl ist nicht durch drei und zwei teilbar.")

