import random

class JokeOMat:
    def __init__(self):
        self.black_humor_jokes = [
            "Warum hat der Hai keine Freunde? Er ist ein Einzelgänger.",
            "Warum kann die Blondine keine Autotür öffnen? Weil sie den Schlüssel verloren hat.",
            "Die ersten Worte meines Sohnes?“ – Wo warst du die letzten 20 Jahre?",
            "Polen ist das einzige Land, wo der Bumerang nicht zurückkommt.",
            "Was wiegst du eigentlich? Nur die ersten drei Zahlen!",
        ]
        self.flat_jokes = [
            "Warum hat der Mathematikbuch geweint? Es hatte zu viele Probleme.",
            "Warum nehmen Geister nie Lügen wahr? Weil sie durch die Wahrheit hindurchsehen können.",
            "Was ist groß, braun und schreibt ganz undeutlich? - Ein Kritzlibär",
            "„Weißt Du warum die Pflanzen in unserem Garten vertrocknet sind? - ne da stehe ich auf dem Schlauch",
            "Was bekommt man, wenn man eine Bibel bei EBay versteigert? - 10 Gebote"
        ]
        self.puns = [
            "Warum arbeiten Geister nie? Weil sie keine Existenz haben.",
            "Warum hat der Kühlschrank die Party verlassen? Weil er gemerkt hat, dass er kein Bier mehr hatte.",
        ]
        self.animal_jokes = [
            "Warum ließ das Eichhörnchen seinen Job fallen? Weil es zu eich-nahmig war.",
            "Warum sind Elefanten so groß, grau und runzelig? Weil, wenn sie pink wären, sie Kühlschränke wären.",
        ]
        self.mother_jokes = [
            "Deine Mutter arbeitet im Möbelhaus als unterste Schublade.",
            "Wenn der Geier ausstirbt ist deine Mutter der hässlichste Vogel.",
            "Deine Mutter arbeitet als Geruch auf dem Fischkutter.",
            "Um deine Mutter zu überfahren braucht man mehrere Tankfüllungen.",
            "Deine Mutter war schon als kleiner Junge hässlich.",
            "Deine Mutter ist so fett! Wenn sie mit High Heels das Haus verlässt, kommt sie mit Flip-Flops nach Hause.",
            "Deine Mutter ist so hässlich, dass dein Vater sie mit zur Arbeit nimmt, damit er ihr keinen Abschiedskuss geben muss.",
            "Deine Mutter ist so dumm, dass sie einen Telefonjoker nutzt, um zu fragen welche Farbe das Weiße Haus in Washington hat.",
            "Deine Mutter ist so behaart, dass wenn sie mit dem Hund spazieren geht zuerst gestreichelt wird.",
        ]

    def get_random_joke(self, joke_category):
        if joke_category == "schwarzer humor":
            return random.choice(self.black_humor_jokes)
        elif joke_category == "flachwitze":
            return random.choice(self.flat_jokes)
        elif joke_category == "wortspiele":
            return random.choice(self.puns)
        elif joke_category == "tierwitze":
            return random.choice(self.animal_jokes)
        elif joke_category == "mutterwitze":
            return random.choice(self.mother_jokes)
        else:
            return "Ungültige Witzkategorie."

    def show_information(self):
        return """
Impressum:
Joke-O-Mat Betreiber
Straße: Musterstraße 1
Ort: 12345 Musterstadt
Kontakt: info@jokeomat.de
"""

jokeomat = JokeOMat()

print("Willkommen beim Joke-O-Mat!")
while True:
    print('----------')
    print("Wähle eine Kategorie: schwarzer Humor, Flachwitze, Wortspiele, Tierwitze, Mutterwitze oder 'Informationen' für Impressum")
    chosen_category = input("Welche Kategorie möchtest du hören?").lower()  # Änderung: Klammern hinzugefügt

    if chosen_category == 'informationen':
        print(jokeomat.show_information())
    else:
        print(jokeomat.get_random_joke(chosen_category))
