# Schreiben einer ToDo-Liste. Ein Task soll die Form:
# {
#  'name': 'Einkaufen',
#  'erledigt': False,
#  'priorität': 'Mittel'
# }
# haben



# Funktion zum Anzeigen der ToDo-Liste
def anzeigen(todo_list):
    print("Liste anzeigen ist noch nicht implementiert.")

# Funktion zum Hinzufügen einer Aufgabe zur ToDo-Liste
def hinzufügen(todo_list, task):
    print("Task hinzufügen ist noch nicht implementiert.")

# Funktion zum Entfernen einer Aufgabe aus der ToDo-Liste
def entfernen(todo_list, task):
    print("Task entfernen ist noch nicht implementiert.")

# Funktion zum Markieren einer Aufgabe als erledigt
def erledigt_markieren(todo_list, task):
    print("Erledigte markieren ist noch nicht implementiert.")

# Funktion zum Anzeigen nur erledigter Aufgaben
def anzeigen_erledigt(todo_list):
    print("Erledigte anzeigen ist noch nicht implementiert.")

def anzeigen_unerledigt(todo_list):
    print("Unerledigte anzeigen ist noch nicht implementiert.")



todo_list = []
while True:
    print("\nWas möchtest du tun?")
    print("1. ToDo-Liste anzeigen")
    print("2. Aufgabe hinzufügen")
    print("3. Aufgabe entfernen")
    print("4. Aufgabe als erledigt markieren")
    print("5. Nur erledigte Aufgaben anzeigen")
    print("6. Nur unerledigte Aufgaben anzeigen")
    print("7. Beenden")
    choice = input("Auswahl: ")

    if choice == '1':
        anzeigen(todo_list)
    elif choice == '2':
        task = input("Neue Aufgabe hinzufügen: ")
        hinzufügen(todo_list, task)
    elif choice == '3':
        task = input("Aufgabe entfernen: ")
        entfernen(todo_list, task)
    elif choice == '4':
        task = input("Aufgabe als erledigt markieren: ")
        erledigt_markieren(todo_list, task)
    elif choice == '5':
        anzeigen_erledigt(todo_list)
    elif choice == '6':
        anzeigen_unerledigt(todo_list)
    elif choice == '7':
        print("Auf Wiedersehen!")
        break
    else:
        print("Ungültige Eingabe. Bitte wähle eine Option von 1 bis 6.")