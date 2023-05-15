### WoF - Worrier of Florin / Finlor
### A text-based adventure game
spiel_ort = "Florin"
spiel_name = "Worrier of " + spiel_ort



import random
import sys
import karten_decks


# Kartendecks
Strategiekarten = ["Heiltrank", "Liebestrank", "Verwirrung", "Bekehrung", "Blinder Zorn", "Panische Angst", "Paranoia", "Giftregen", "Steinwurf", "Alte Rüstung", "Strohmann", "Schleifeisen", "Rauchbombe (Dieb)", "Axtwurf (Babar)", "Überzeugungszwang (Mönch)", "Knappe (Ritter)", "Ausgiebiges Frühstück (Abenteurer)"]
Waffenkarten_tier1 = ["Rostige Klinge", "Nagelholz", "Steinschleuder", "Holzschild", "Holzspeer"]
Monsterkarten_tier1 = ["Sturer Stier", "Wellenreitende Wasserschildkröte", "Bärtiger Bär", "Würdiger Wolf", "Harmloser Hai", "Wüttender Widder", "Wildes Wildschwein", "Schlängelnede Schlange", "Eilige Echse", "Horde Halblinge"]
# karten_decks.py importieren
strat_dict = karten_decks.strategie_karten
waffen_dict = karten_decks.waffen_karten_tier1
monster_dict = karten_decks.monster_karten_tier1




class Krieger:
    def __init__ (self, name, angriff, leben, gewandtheit, reiten, charisma, rüstung, inventar = [], gesehene_monster = [], besiegte_monster = []):
        self.name = name
        self.angriff = angriff
        self.leben = leben
        self.gewandtheit = gewandtheit
        self.reiten = reiten
        self.charisma = charisma
        self.rüstung = rüstung
        self.inventar = inventar
        self.gesehene_monster = gesehene_monster
        self.besiegte_monster = besiegte_monster
    def __str__(self):
        return "Information zum Spieler: " + self.name + ", Angriff = " + str(self.angriff) + " , Leben = " + str(self.leben) + " , Gewandtheit = " + str(self.gewandtheit) + " , Reiten = " + str(self.reiten) + " , Charisma " + str(self.charisma) + " , Rüstung = " + str(self.rüstung)
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
    rüstung = 0 # bei default immer 0
    return Krieger(name, angriff, leben, gewandtheit, reiten, charisma, rüstung, inventar = [], gesehene_monster = [], besiegte_monster = [])



### Spielrunde
def schatzkarte_ziehen(spieler):
    würfel1 = random.randint(1,6)
    print(spieler.name)
    if würfel1 == 6:
        # eine zufällige Karte aus dem Waffenkarten Deck ziehen
        würfel2 = random.randint(0,4)
        print("Du hast eine Waffenkarte gezogen: " + Waffenkarten_tier1[würfel2])
        spieler.inventar.append(Waffenkarten_tier1[würfel2])
    else:
        # eine zufällige Karte aus dem Strategiekarten Deck ziehen
        würfel2 = random.randint(0,15)
        print("Du hast eine Strategiekarte gezogen: " + Strategiekarten[würfel2])
        spieler.inventar.append(Strategiekarten[würfel2])

def item_karte_info(item):
    # die Werte der Karte auslesen durch das Dictionary
    if item in strat_dict:
        # print(strat_dict[item])
        # gebe den Name der Karte aus
        print("Name: " + strat_dict[item]["name"] + ", Typ: " + strat_dict[item]["typ"] + ", Klasse: " + str(strat_dict[item]["klasse"]) + ", Effekt: " + str(strat_dict[item]["effekt"]))
    elif item in waffen_dict:
        # print(waffen_dict[item])
        print("Name: " + waffen_dict[item]["name"] + ", Typ: " + waffen_dict[item]["typ"] + ", Klasse: " + str(waffen_dict[item]["klasse"]) + ", Effekt: " + str(waffen_dict[item]["effekt"]) + ", Platz: " + str(waffen_dict[item]["platz"]) + ", Angriffsstats: " + str(waffen_dict[item]["stats"]))


def monster_karte_info(monster):
    # die Werte der Karte auslesen durch das Dictionary
    if monster_dict[monster]["reiten"]["reiten"] == True:
        print("Name: " + monster_dict[monster]["name"] + ", Tier: " + str(monster_dict[monster]["tier"]) + ", Leben: " + str(monster_dict[monster]["leben"]) + ", Gewandtheit: " + str(monster_dict[monster]["gewandtheit"]) + ", Angriffsstats: " + str(monster_dict[monster]["angriff"]) + "\n Belohnung wenn du das Monster besiegt hast: " + str(monster_dict[monster]["belohnung"]) + " Schatzkarten. \n Du kannst das Monster reiten: " + str(monster_dict[monster]["reiten"]["reiten"]) + ", wenn du den Reitwert oder mehr hast!")
    else:
        print("Name: " + monster_dict[monster]["name"] + ", Tier: " + str(monster_dict[monster]["tier"]) + ", Leben: " + str(monster_dict[monster]["leben"]) + ", Gewandtheit: " + str(monster_dict[monster]["gewandtheit"]) + ", Angriffsstats: " + str(monster_dict[monster]["angriff"]) + "\n Belohnung wenn du das Monster besiegt hast: " + str(monster_dict[monster]["belohnung"]) + " Schatzkarten.")


def monsterkarte_ziehen(spieler):
    # eine zufällige Karte aus dem Monsterkarten Deck ziehen
    würfel1 = random.randint(0,9)
    print("Du hast eine Monsterkarte gezogen: " + Monsterkarten_tier1[würfel1])
    spieler.gesehene_monster.append(Monsterkarten_tier1[würfel1])
    

def kampf(spieler):
    # Kampf
    print(input("Du gerätst in ein Kampf, ein Monster ! " + spieler.gesehene_monster[-1]))
    # nutze dein inventar
    print(monster_karte_info(spieler.gesehene_monster[-1]))
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
    # hast du das Monster besiegt?
    if input("Hat der Spieler das Monster besiegt? (j/n) ") == "j":
        spieler.besiegte_monster.append(spieler.gesehene_monster[-1])
        print("Du hast das Monster besiegt! Weiter so!.")
        anzahl_zu_ziehende_karten = monster_dict[spieler.gesehene_monster[-1]]["belohnung"]
        for i in range(anzahl_zu_ziehende_karten):
            schatzkarte_ziehen(spieler)



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
    print("Bevor ihr euch in den Wettstreit um den Thron begebt, müsst ihr euch noch ein wenig vorbereiten.")
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
                for item in spieler[i].inventar:
                    item_karte_info(item)

            print(input("---"))
            
            ## Monsterkarte ziehen
            print("Ziehe eine Monsterkarte!")
            print(input("Drücke Enter um zu ziehen."))
            monsterkarte_ziehen(spieler[i])
            # Kampf
            kampf(spieler[i])


            print(input("--------------------\n\n"))