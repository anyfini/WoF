### WoF - Worrier of Florin / Finlor
### A text-based adventure game
spiel_ort = "Florin"
spiel_name = "Worrier of " + spiel_ort



import random
import sys


# Kartendecks
Strategiekarten = ["Heiltrank", "Liebestrank", "Verwirrung", "Bekehrung", "Blinder Zorn", "Panische Angst", "Paranoia", "Giftregen", "Steinwurf", "Alte Rüstung", "Strohmann", "Schleifeisen", "Rauchbombe (Dieb)", "Axtwurf (Babar)", "Überzeugungszwang (Mönch)", "Knappe (Ritter)", "Ausgiebiges Frühstück (Abenteurer)"]
Waffenkarten_tier1 = ["Rostige Klinge", "Nagelholz", "Steinschleuder", "Holzschild", "Holzspeer"]
Monsterkarten_tier1 = ["Sturer Stier", "Wellenreitende Wasserschildkröte", "Bärtiger Bär", "Würdiger Wolf", "Harmloser Hai", "Wüttender Widder", "Wildes Wildschwein", "Schlängelnede Schlange", "Eilige Echse", "Horde Halblinge"]



class Krieger:
    def __init__ (self, name, angriff, leben, gewandtheit, reiten, charisma, inventar = [], gesehene_monster = [], besiegte_monster = []):
        self.name = name
        self.angriff = angriff
        self.leben = leben
        self.gewandtheit = gewandtheit
        self.reiten = reiten
        self.charisma = charisma
        self.inventar = inventar
        self.gesehene_monster = gesehene_monster
        self.besiegte_monster = besiegte_monster
    def __str__(self):
        return "Information zum Spieler: " + self.name + ", Angriff = " + str(self.angriff) + " , Leben = " + str(self.leben) + " , Gewandtheit = " + str(self.gewandtheit) + " , Reiten = " + str(self.reiten) + " , Charisma " + str(self.charisma)
    def show_inventar(self):
        print("Inventar von " + self.name + ":")
        for i in self.inventar:
            j = self.inventar.index(i)
            print(str(j+1) + ". " + i)

        


### Spielvorbereitung
# Spieler
def player_initial():
    # Anzahl Spieler
    global anzahl_spieler
    anzahl_spieler = int(input("Wie viele Spieler? "))
    # Name Spieler
    global spieler_name
    spieler_name = []
    for i in range(anzahl_spieler):
        spieler_name.append(input("Name Spieler " + str(i+1) + ": "))


## Stats Vergabe
def stats_initial(name):
    charisma = 0
    # Angriff und Leben
    würfel1 = random.randint(1,6)
    würfel2 = random.randint(1,6)
    print(input("Drücke Enter um für den Angriffs-und Lebenswert zu würfeln."))
    print("Würfel 1 = " + str(würfel1))
    print(input("Drücke Enter um mit dem zweiten Würfel zu würfeln."))
    print("Würfel 2 = " + str(würfel2))
    angriff = würfel1 + würfel2
    print("Angriff: " + str(angriff))
    leben = 12 - angriff
    print("Leben: " + str(leben))
    if würfel1 == würfel2:
        charisma += 1
    # Gewandtheit und Reiten
    würfel1 = random.randint(1,6)
    würfel2 = random.randint(1,6)
    print(input("Drücke Enter um für den Gewandtheits-und Reitwert zu würfeln."))
    print("Würfel 1 = " + str(würfel1))
    print(input("Drücke Enter um mit dem zweiten Würfel zu würfeln."))
    print("Würfel 2 = " + str(würfel2))
    gewandtheit = würfel1 + würfel2
    print("Gewandtheit: " + str(gewandtheit))
    reiten = 12 - gewandtheit
    print("Reiten: " + str(reiten))
    if würfel1 == würfel2:
        charisma += 1
    # Charisma
    print(input("Drücke Enter um zu schauen ob du Charisma erhälst"))
    print("Wenn du glück hattest und einen Pasch gewürfelt hast, erhälst du einen Punkt Charisma.")
    if charisma == 0:
        print("Du hast leider keinen Pasch gewürfelt und erhälst keinen Punkt Charisma.")
        print("Charisma: " + str(charisma))
    else:
        print("Du hattest Glück und beginnst das Spiel mit Charisma.")
        print("Charisma: " + str(charisma))
    # Krieger erstellen
    return Krieger(name, angriff, leben, gewandtheit, reiten, charisma)



### Spielrunde
def schatzkarte_ziehen(spieler):
    würfel1 = random.randint(1,6)
    if würfel1 == 6:
        # eine zufällige Karte aus dem Waffenkarten Deck ziehen
        würfel2 = random.randint(1,5)
        print("Du hast eine Waffenkarte gezogen: " + Waffenkarten_tier1[würfel2])
        spieler.inventar.append(Waffenkarten_tier1[würfel2])
    else:
        # eine zufällige Karte aus dem Strategiekarten Deck ziehen
        würfel2 = random.randint(0,15)
        print("Du hast eine Strategiekarte gezogen: " + Strategiekarten[würfel2])
        spieler.inventar.append(Strategiekarten[würfel2])


def monsterkarte_ziehen(spieler):
    # eine zufällige Karte aus dem Monsterkarten Deck ziehen
    würfel1 = random.randint(0,9)
    print("Du hast eine Monsterkarte gezogen: " + Monsterkarten_tier1[würfel1])
    spieler.gesehene_monster.append(Monsterkarten_tier1[würfel1])
    

def kampf(spieler):
    # Kampf
    print(input("Du gerätst in ein Kampf, ein Monster ! " + spieler.gesehene_monster[-1]))
    # nutze dein inventar
    spieler.show_inventar()
    # nenne alle Schatzkarten die du verwenden möchtest
    print("Nenne die Nummern der Schatzkarten die du verwenden möchtest.")
    print("Wenn du dir sicher bist drücke Enter. Wiederhole dies bis du keine Schatzkarte mehr einsetzen möchtest.")
    print("Dann drücke einfach Enter.")
    schatzkarten = []
    while True:
        eingabe = input()
        if eingabe == "":
            break
        else:
            schatzkarten.append(spieler.inventar[int(eingabe)-1])
    print("Du hast folgende Schatzkarten ausgewählt:")
    for i in schatzkarten:
        print(i)
    # lösche die Schatzkarten aus dem Inventar
    for i in schatzkarten:
        spieler.inventar.remove(i)




if __name__ == "__main__":
    # remove old logs
    with open("logs.txt", "w") as f:
        f.write("")
    # Spielvorbereitung
    spieler = []
    print("Willkommen bei WoF - " + spiel_name + "!")
    print("Ein textbasiertes Abenteuerspiel")
    player_initial()
    # Schreibe Spieler Stats in Datei
    with open("logs.txt", "a") as f:
        f.write(f'### Spiel von {spieler_name} ###\n')
        f.write("\n")
        f.write(f'## Start ##\n')
    print("Willkommen in " + spiel_ort + " edle Krieger!")
    print("Befor ihr euch in den Wettstreit um den Thron begebt, müsst ihr euch noch ein wenig vorbereiten.")
    print("Seit ihr bereit für eure Eigenschaften?")
    print("Dann lasst uns beginnen!")
    print(input("Drücke Enter um zu beginnen."))
    for i in range(anzahl_spieler):
        print("Spieler " + str(i+1) + ": " + spieler_name[i])
        print("Es ist dein Zug sich auf das Abenteuer vorzuereiten.")
        spieler.append(stats_initial(spieler_name[i]))
        print(spieler[i].__str__())
        print("Du bist bereit für das Abenteuer!")
        print(input("--------------------"))
        # Schreibe Spieler Stats in Datei
        with open("logs.txt", "a") as f:
            f.write(spieler[i].__str__() + "\n")

    ## Spielrunde

    # jeder Spieler ist einmal am Zug
    runde = 0
    while True:
        runde += 1
        for i in range(anzahl_spieler):
            ## Schatzkarte ziehen
            print(spieler[i].name + ", es ist dein Zug.")
            print("Ziehe eine Schatzkarte!")
            print(input("Drücke Enter um zu ziehen."))
            schatzkarte_ziehen(spieler[i])
            # Willst du dein Inventar sehen?
            inventar_sehen = input("Willst du dein Inventar sehen? (j/n) ")
            if inventar_sehen == "j":
                spieler[i].show_inventar()
            print(input("---"))
            
            ## Monsterkarte ziehen
            print("Ziehe eine Monsterkarte!")
            print(input("Drücke Enter um zu ziehen."))
            monsterkarte_ziehen(spieler[i])
            # Kampf
            kampf(spieler[i])


            print(input("--------------------\n\n"))