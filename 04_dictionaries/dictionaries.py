# Dieses Pythonscript zeigt die Nutzung von Dictionaries

if __name__ == '__main__':
    '''
    #tiere = {"Hund":5, "Fuchs":4, "Reh":6, "Dachs":2, "Wildschwein":4}
    tiere = {}
    print(type(tiere))
    print (tiere)

    tiere["Hund"] = 5
    tiere["Fuchs"] = 4
    tiere["Reh"] = 6
    tiere["Dachs"] = 2
    tiere["Wildschwein"] = 4

    print(tiere)

    print(tiere["Dachs"])


    #Zugriff auf nicht vorhandenen key
    key = "Luchs"
    if key in tiere:
        print(tiere[key])
    else:
        print(key + " ist nicht als key im Dictionary 'tiere' vorhanden!")



    #Löschen einzelner key:value-Paare
    print(tiere)
    del tiere["Reh"]
    print(tiere)
    key = "Luchs"
    if key in tiere:
        del tiere[key]

    #Wiederherstellen von Reh
    tiere["Reh"] = 6

    print(tiere)
    removed_value = tiere.pop('Reh')
    print(tiere)
    print("Der Wert des entfernten keys:" + str(removed_value))
    removed_value = tiere.pop('Luchs', 'Key wurde nicht gefunden')
    print("Der Wert des entfernten keys:" + str(removed_value))

'''


    #####################################################################################
    # Ein neues Anwendungsbeispiel:Übersetzungen
    #####################################################################################

    #ein Englisch-Deutsch-Wörterbuch
    en_de = {"red":"rot", "green":"grün", "blue":"blau", "yellow":"gelb"}

    #und genau umgekehrt:
    de_en = {"rot":"red", "grün":"green", "blau":"blue", "gelb":"yellow"}

    print(en_de["blue"])
    print(de_en["gelb"])


    #noch ein Deutsch-Französisch-Wörterbuch:
    de_fr = {"rot":"rouge", "grün":"vert", "blau":"bleu", "gelb":"jaune"}
    #ein verschachtelter Zugriff
    print("The French word for red is:" + de_fr[en_de["red"]])



    #wir können auch Dictionaries aus Dictionaries erzeugen:
    dictionaries = {"de_en":de_en, "en_de":en_de, "de_fr":de_fr}

    print(dictionaries["de_fr"]["blau"])


    ####
    # Ein anderes Beispiel für Dictionary im Dictionary (nested)
    # hier sind die keys Zahlen
    digits = {1:{'Word':'one', 'Roman':'I'},
              2:{'Word':'two', 'Roman':'II'},
              3:{'Word':'three', 'Roman':'III'},
              4:{'Word':'four', 'Roman':'IV'},
              5:{'Word':'five', 'Roman':'V'}}

    print(digits[1]['Word'])
    print(digits[4]['Roman'])



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
