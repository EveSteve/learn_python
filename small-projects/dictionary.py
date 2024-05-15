# Aufgabe 1: Schreibe eine Funktion, die prüft, ob ein Key bereits in einem Dictionary vorhanden ist, und falls ja, TRUE zurückgibt.
 
def key_exists(dict, key):
    exists = False
 
    # TODO
 
    return exists
 
 
dict = {"Banane":"gelb", "Kirsche":"rot", "Apfel": "rot", "Traube": "grün"}
 
search_key = input("Welcher Key soll geprüft werden: ")
print("Der Key", search_key, "ist im Dictionary vorhanden: ", key_exists(dict, search_key))
 
 
# Aufgabe 2: Schreibe ein Programm, welches mit einer for-Schleife über ein Dictionary iteriert und dessen inhalt Zeile für Zeile ausgibt (Tipp: Benutze d.items())
# Gebe den Inhalt in der Form <key> -> <value> aus.
 
dict2 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
 
 
# Aufgabe 3: Tausche den Inhalt eines Keys aus. Mache aus dem Key "city" den Key "location".
dict3 = {
    "name": "Kelly",
    "age":25,
    "salary": 8000,
    "city": "New York"
}
