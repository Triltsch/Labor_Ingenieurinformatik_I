"""
Dieses Pythonscript zeigt die Nutzung von Dictionaries

@created: 02.11.2022
@author: U.Triltsch
"""

if __name__ == '__main__':

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
'''
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


    key = input("Welches Tier?")
    if key in tiere:
      print(tiere[key])

      tiere[key] = 34

      print(tiere)




'''
