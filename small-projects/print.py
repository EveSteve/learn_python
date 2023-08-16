nummer = 134
print(' '.join(['Der Eifelturm ist', str(nummer), 'Jahre alt.']))

print('; '.join(['Banane','Kirsche','Erbeere']))

print(1, 'Python Tricks', 'Dan Bader', sep=',')

print('Zeile 1\nZeile 2\nZeile 3')

file = open("demofile.txt", "a")
file.write("Diese Zeile wird in einer Datei ausgegeben!")
file.close()

# Aufgabe 1
# Funktionsweise des Print-Statements erneut durchgehen
# number = input("Bitte geben Sie eine Zahl für die Multiplikationstabelle ein: ")
# for count in range(1, 11):
#     print(count, " * ", number, " = ", int(count) * int(number))

# Aufgabe 2
# Schreibe ein Programm, welches folgende Wörter vom Nutzer annimmt und folgenden Output macht:
# Input1: Vorname1, Input2: Vorname2, Input3: Speise1, Speise2
# Output: "<Vorname1> isst gerne <Speise1>, aber <Vorname2> isst gerne <Speise2>."


# Aufgabe 3 (replace)
# Du hast einen Text in der Variable text. Ersetze nun in diesem Text alle Stellen, wo das Wort 'Pfannkuchen' vorkommt, dieses mit Eierkuchen. Gibt den neuen Text aus.
text = 'Dieses tolle Pfannkuchen-Grundrezept ist absolut gelingsicher. ' \
       'Und das Ergebnis: Himmlisch! Über den einfachen Pfannkuchenteig freut sich deswegen ' \
       'auch die ganze Familie. Egal, ob zum Brunch oder als Mittagessen: Das Pfannkuchen-Rezept passt immer!' \
       'Und wie macht man Pfannkuchen? Ganz simpel! Der klassische Teig besteht aus den Zutaten Mehl, Milch und Eiern. ' \
       'Er lässt sich wunderbar variieren und verfeinern. Grundsätzlich schmecket das Ganze süß sowie herzhaft. ' \
       'Der Unterschied liegt nur im Topping sowie natürlich in der Zucker- oder Salzmenge. Wenn ihr ein paar einfache Tipps befolgt, ' \
       'wecken die schnellen Pfannkuchen garantiert schöne Kindheitserinnerungen 😉 . Denn wer ist früher nicht gerne in der Küche gestanden ' \
       'und hat Mama zugesehen, wie der Pfannkuchenteig Löffel für Löffel in die Pfanne gegeben wurde? Klar, dass ihr das Rezepte ' \
       'natürlich auch in „Backen macht glücklich – Das Familienbackbuch“ findet.'

# Aufgabe 4 (find)
# Teste, ob ein vom Nutzer eingelesenes Wort in folgendem Text vorkommt. Gebe 'Ja', oder 'Nein' aus, je nachdem, ob das Wort vorkommt.
suchtext = 'Für diesen Zitronen-Mandel-Kuchen ohne Mehl reicht die Beschreibung „saftig“ eigentlich überhaupt nicht aus. ' \
           'Der glutenfreie Kuchen mit gemahlenen Mandeln ist wirklich extrem saftig und im Inneren noch leicht feucht. Genau so, wie ich Rührkuchen liebe! ' \
           'Dabei handelt es sich beim Mandel-Zitronenkuchen im Grunde genommen eigentlich eher um einen Biskuit. Basis ist nämlich eine sehr schaumige Eiermasse. ' \
           'Sie wird ähnlich wie beim Wiener Biskuit zusätzlich mit flüssiger Butter verfeinert. Was den Mandelkuchen ohne Mehl in punkto Konsistenz einfach absolut ' \
           'umwerfend macht. Übrigens auch das perfekte Rezept für alle, die von glutenfreien Kuchen bisher eher enttäuscht waren. Zum Beispiel, weil diese oft eher ' \
           'trocken sind. Hier ist das Gegenteil der Fall: Der Mandelkuchen ohne Mehl wird euch wie auch mein glutenfreier Apfelkuchen ganz bestimmt schmecken! ' \
           'Ich habe mich für diese Kreation von zwei älteren Rezepten inspirieren lassen: dem mallorquinischen Mandelkuchen sowie dem Low Carb Apfelkuchen.'