"""
Ein neues Anwendungsbeispiel: Übersetzungen

@created: 02.11.2022
@author: U.Triltsch
"""

# ein Englisch-Deutsch-Wörterbuch
en_de = {"red": "rot", "green": "grün", "blue": "blau", "yellow": "gelb"}

# und genau umgekehrt:
de_en = {"rot": "red", "grün": "green", "blau": "blue", "gelb": "yellow"}

print(en_de["blue"])
print(de_en["gelb"])

# noch ein Deutsch-Französisch-Wörterbuch:
de_fr = {"rot": "rouge", "grün": "vert", "blau": "bleu", "gelb": "jaune"}
# ein verschachtelter Zugriff
print("The French word for red is:" + de_fr[en_de["red"]])

# wir können auch Dictionaries aus Dictionaries erzeugen:
dictionaries = {"de_en": de_en, "en_de": en_de, "de_fr": de_fr}

print(dictionaries["de_fr"]["blau"])
