"""
 Dieses Pythonscript zeigt die Nutzung von Dictionaries
 in der I18n eines Menüs

@created: 02.11.2022
@author: U.Triltsch
"""

en_en = {"file":"File", "new":"New","open":"Open", "save":"Save",
         "save as":"Save as", "print preview":"Print Preview", "print": "Print",
         "close":"Close", "exit":"Exit"}

en_fr =  {"file":"Fichier", "new":"Nouveau","open":"Ouvrir", "save":"Enregistrer",
          "save as":"Enregistrer sous", "print preview": "Apercu avant impressioner",
          "print":"Imprimer", "close":"Fermer", "exit":"Quitter"}

en_de =  {"file":"Datei", "new":"Neu","open":"Öffnen", "save":"Speichern",
          "save as":"Speichern unter", "print preview":"Druckansicht",
          "print":"Drucken", "close":"Schließen", "exit":"Verlassen"}

en_it = {"file":"File", "new":"Nuovo","open":"Apri", "save":"Salva",
          "save as":"Salva come", "print preview":"Anteprima di stampa",
          "print":"Stampa", "close":"Chiudi", "exit":"Esci"}


menu = {"en": en_en, "fr": en_fr, "de": en_de, "it": en_it}

language = input("In welcher Sprache soll das Menu ausgegeben werden [en, fr, de, it]")

current_dic = menu[language]

for key in current_dic:
    print(current_dic[key])
