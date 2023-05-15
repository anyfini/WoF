# Alle Karten-Decks

# Strategie-Karten
Strategiekarten = ["Heiltrank", "Liebestrank", "Verwirrung", "Bekehrung", "Blinder Zorn", "Panische Angst", "Paranoia", "Giftregen", "Steinwurf", "Alte Rüstung", "Strohmann", "Schleifeisen", "Rauchbombe (Dieb)", "Axtwurf (Babar)", "Überzeugungszwang (Mönch)", "Knappe (Ritter)", "Ausgiebiges Frühstück (Abenteurer)"]
# zu jedem wert in der liste gibt es eine karte mit dem gleichen namen
strategie_karten = {
    "heiltrank": {
        "name": "Heiltrank",
        "typ": "strategie",
        "klasse": "alle",
        "effekt": "Heilung um 5",
    },
    "Liebestrank": {
        "name": "Liebestrank",
        "typ": "strategie",
        "klasse": "alle",
        "effekt": "Zwinge einen Mitspieler mit niedrigerem Charisma als deines dir bei einem Kampf zu helfen",
    },
    "Verwirrung": {
        "name": "Verwirrung",
        "typ": "strategie",
        "klasse": "alle",
        "effekt": "Ein Spieler greift den Verbündeten mit dem höchsten Angriff im Kampf an",
    },
    "Bekehrung": {
        "name": "Bekehrung",
        "typ": "strategie",
        "klasse": "alle",
        "effekt": "Der Spieler im Kampf mit den niedrigsten Leben ist dein Schild",
    },
    "Blinder Zorn": {
        "name": "Blinder Zorn",
        "typ": "strategie",
        "klasse": "alle",
        "effekt": "Verdopple den Angriff halbiere das Leben von einer Spielfigur für den Kampf",
    },
    "Panische Angst": {
        "name": "Panische Angst",
        "typ": "strategie",
        "klasse": "alle",
        "effekt": "Verdopple das Leben halbiere den Angriff einer Spielfigur für den Kampf",
    },
    "Paranoia": {
        "name": "Paranoia",
        "typ": "strategie",
        "klasse": "alle",
        "effekt": "Senke die Gewandtheit eines Spielers dauerhaft um die Hälfte. Würfle um diese Karte los zu werden eine 5 oder 6 Pro deinem Zug",
    },
    "Giftregen": {
        "name": "Giftregen",
        "typ": "strategie",
        "klasse": "alle",
        "effekt": "Vergifte einen Spieler er nimmt jede Runde einen Schaden, Um diesen Effekt loszuwerden würfle mit 3 Würfeln einen Pasch"
    },
    "Steinwurf": {
        "name": "Steinwurf",
        "typ": "strategie",
        "klasse": "alle",
        "effekt": "Das Monster greift nun zuerst an",
    },
    "Alte Rüstung": {
        "name": "Alte Rüstung",
        "typ": "strategie",
        "klasse": "alle",
        "effekt": "Erhöhe deine Rüstung um 1 für diesen Kampf",
    },
    "Strohmann": {
        "name": "Strohmann",
        "typ": "strategie",
        "klasse": "alle",
        "effekt": "Wenn das Monster eine gerade Zahl für den Angriff würfelt, geht der Angriff einmalig auf den Strohmann",
    },
    "Schleifeisen": {
        "name": "Schleifeisen",
        "typ": "strategie",
        "klasse": "alle",
        "effekt": "Erhöhe deinen Angriff in diesem Kampf um 1",
    },
    "Rauchbombe (Dieb)": {
        "name": "Rauchbombe (Dieb)",
        "typ": "strategie",
        "klasse": "Dieb",
        "effekt": "Erlaubt es dir eine Karte verdeckt zu spielen",
    },
    "Axtwurf (Babar)": {
        "name": "Axtwurf (Babar)",
        "typ": "strategie",
        "klasse": "Babar",
        "effekt": "verursache zusätzlich zu deinem Angriff den Schanden i.H.v. der Augenzahl des einseitigen Würfel",
    },
    "Überzeugungszwang (Mönch)": {
        "name": "Überzeugungszwang (Mönch)",
        "typ": "strategie",
        "klasse": "Mönch",
        "effekt": "Überzeuge jeden Spieler bei 4-6 sich deinem Kampf anzuschließen",
    },
    "Knappe (Ritter)": {
        "name": "Knappe (Ritter)",
        "typ": "strategie",
        "klasse": "Ritter",
        "effekt": "Der Knappe bringt die die Ritterrüstung für diesen Kampf. Setze die Rüstung auf 5",
    },
    "Ausgiebiges Frühstück (Abenteurer)": {
        "name": "Ausgiebiges Frühstück (Abenteurer)",
        "typ": "strategie",
        "klasse": "Abenteurer",
        "effekt": "Ein ausgiebiges Frühstück ist so selten und mehr Wert als alles Gold der Welt. Heile dich vollständig. Dein Zug ist zu Ende",
    },
}


# Waffen-Karten
Waffenkarten_tier1 = ["Rostige Klinge", "Nagelholz", "Steinschleuder", "Holzschild", "Holzspeer"]
# zu jedem wert in der liste gibt es eine karte mit dem gleichen namen
waffen_karten_tier1 = {
    "Rostige Klinge": {
        "name": "Rostige Klinge",
        "typ": "waffe",
        "klasse": "alle",
        "effekt": "Angriff +1",
        "platz": "hand",
        "stats": {
            "angriff": {
                "wert": 1,
                "schlechter_treffer": [1, 2],
                "normaler_treffer": [3, 4, 5],
                "kritischer_treffer": [6],
            },
            "rüstung": 0,
            "leben": 0,
            "gewandtheit": 0,
            "charisma": 0,
        }
    },
    "Nagelholz": {
        "name": "Nagelholz",
        "typ": "waffe",
        "klasse": "alle",
        "effekt": "Angriff +2",
        "platz": "2 hände",
        "stats": {
            "angriff": {
                "wert": 2,
                "schlechter_treffer": [1, 2, 3],
                "normaler_treffer": [4, 5],
                "kritischer_treffer": [6],
            },
            "rüstung": 0,
            "leben": 0,
            "gewandtheit": 0,
            "charisma": 0,
        }
    },
    "Steinschleuder": {
        "name": "Steinschleuder",
        "typ": "waffe",
        "klasse": "alle",
        "effekt": "Angriff + 2, Rüstung -1",
        "platz": "2 hände",
        "stats": {
            "angriff": {
                "wert": 2,
                "schlechter_treffer": [1, 2],
                "normaler_treffer": [3, 4],
                "kritischer_treffer": [5, 6],
            },
            "rüstung": -1,
            "leben": 0,
            "gewandtheit": 0,
            "charisma": 0,
        }
    },
    "Holzschild": {
        "name": "Holzschild",
        "typ": "waffe",
        "klasse": "alle",
        "effekt": "Rüstung +1",
        "platz": "hand",
        "stats": {
            "angriff": 0,
            "rüstung": 1,
            "leben": 0,
            "gewandtheit": 0,
            "charisma": 0,
        }
    },
    "Holzspeer": {
        "name": "Holzspeer",
        "typ": "waffe",
        "klasse": "alle",
        "effekt": "Angriff +1",
        "platz": "hand",
        "stats": {
            "angriff": {
                "wert": 1,
                "schlechter_treffer": [1, 2],
                "normaler_treffer": [3, 4, 5],
                "kritischer_treffer": [6],
            },
            "rüstung": 0,
            "leben": 0,
            "gewandtheit": 0,
            "charisma": 0,
        }
    },
}



# Monster-Karten
Monsterkarten_tier1 = ["Sturer Stier", "Wellenreitende Wasserschildkröte", "Bärtiger Bär", "Würdiger Wolf", "Harmloser Hai", "Wüttender Widder", "Wildes Wildschwein", "Schlängelnede Schlange", "Eilige Echse", "Horde Halblinge"]
# zu jedem wert in der liste gibt es eine karte mit dem gleichen namen
monster_karten_tier1 = {
    "Sturer Stier": {
        "name": "Sturer Stier",
        "typ": "monster",
        "tier": 1,
        "leben": 7,
        "gewandtheit": 8,
        "angriff": {
            "wert": 2,
            "schlechter_treffer": [],
            "normaler_treffer": [1, 2, 3, 4],
            "kritischer_treffer": [],
            "daneben": [5, 6],
        },
        "reiten": {
            "reiten": True,
            "reiten_wert": 5,
            "vorteil": "Rüstung +1",
        },
        "belohnung": 1,
    },
    "Wellenreitende Wasserschildkröte": {
        "name": "Wellenreitende Wasserschildkröte",
        "typ": "monster",
        "tier": 1,
        "leben": 10,
        "gewandtheit": 4,
        "angriff": {
            "wert": 4,
            "schlechter_treffer": [],
            "normaler_treffer": [1, 2],
            "kritischer_treffer": [],
            "daneben": [3, 4, 5, 6],
        },
        "reiten": {
            "reiten": False,
            "reiten_wert": 0,
            "vorteil": "",
        },
        "belohnung": 2,
    },
    "Bärtiger Bär": {
        "name": "Bärtiger Bär",
        "typ": "monster",
        "tier": 1,
        "leben": 8,
        "gewandtheit": 6,
        "angriff": {
            "wert": 6,
            "schlechter_treffer": [],
            "normaler_treffer": [1, 2, 3, 4],
            "kritischer_treffer": [],
            "daneben": [5, 6],
        },
        "reiten": {
            "reiten": True,
            "reiten_wert": 8,
            "vorteil": "Angriff +1",
        },
        "belohnung": 1,
    },
    "Würdiger Wolf": {
        "name": "Würdiger Wolf",
        "typ": "monster",
        "tier": 1,
        "leben": 9,
        "gewandtheit": 4,
        "angriff": {
            "wert": 4,
            "schlechter_treffer": [],
            "normaler_treffer": [1, 2, 3, 4],
            "kritischer_treffer": [],
            "daneben": [5, 6],
        },
        "reiten": {
            "reiten": False,
            "reiten_wert": 0,
            "vorteil": "",
        },
        "belohnung": 1,
    },
    "Harmloser Hai": {
        "name": "Harmloser Hai",
        "typ": "monster",
        "tier": 1,
        "leben": 5,
        "gewandtheit": 10,
        "angriff": {
            "wert": 1,
            "schlechter_treffer": [],
            "normaler_treffer": [1, 2, 3, 4, 5, 6],
            "kritischer_treffer": [],
            "daneben": [],
        },
        "reiten": {
            "reiten": False,
            "reiten_wert": 0,
            "vorteil": "",
        },
        "belohnung": 1,
    },
    "Wüttender Widder": {
        "name": "Wüttender Widder",
        "typ": "monster",
        "tier": 1,
        "leben": 7,
        "gewandtheit": 5,
        "angriff": {
            "wert": 4,
            "schlechter_treffer": [],
            "normaler_treffer": [1, 2, 3, 4, 5],
            "kritischer_treffer": [],
            "daneben": [6],
        },
        "reiten": {
            "reiten": False,
            "reiten_wert": 0,
            "vorteil": "",
        },
        "belohnung": 1,
    },
    "Wildes Wildschwein": {
        "name": "Wildes Wildschwein",
        "typ": "monster",
        "tier": 1,
        "leben": 8,
        "gewandtheit": 10,
        "angriff": {
            "wert": 6,
            "schlechter_treffer": [],
            "normaler_treffer": [6],
            "kritischer_treffer": [],
            "daneben": [1, 2, 3, 4, 5],
        },
        "reiten": {
            "reiten": True,
            "reiten_wert": 8,
            "vorteil": "Gewandtheit + 1",
        },
        "belohnung": 1,
    },
    "Schlängelnede Schlange": {
        "name": "Schlängelnede Schlange",
        "typ": "monster",
        "tier": 1,
        "leben": 5,
        "gewandtheit": 1,
        "angriff": {
            "wert": 2,
            "schlechter_treffer": [],
            "normaler_treffer": [1, 2, 3, 4, 5, 6],
            "kritischer_treffer": [],
            "daneben": [],
        },
        "reiten": {
            "reiten": False,
            "reiten_wert": 0,
            "vorteil": "",
        },
        "belohnung": 1,
    },
    "Eilige Echse": {
        "name": "Eilige Echse",
        "typ": "monster",
        "tier": 1,
        "leben": 7,
        "gewandtheit": 12,
        "angriff": {
            "wert": 2,
            "schlechter_treffer": [],
            "normaler_treffer": [1, 2, 3, 4, 5],
            "kritischer_treffer": [],
            "daneben": [6],
        },
        "reiten": {
            "reiten": True, 
            "reiten_wert": 5,
            "vorteil": "Gewandtheit +1",
        },
        "belohnung": 1,
    },
    "Horde Halblinge": {
        "name": "Horde Halblinge",
        "typ": "monster",
        "tier": 1,
        "leben": 15,
        "gewandtheit": 8,
        "angriff": {
            "wert": 6,
            "schlechter_treffer": [],
            "normaler_treffer": [1, 3, 5],
            "kritischer_treffer": [],
            "daneben": [2, 4, 6],
        },
        "reiten": {
            "reiten": False,
            "reiten_wert": 0,
            "vorteil": "",
        },
        "belohnung": 3,
    },
}
