"""
Dieses Beispiel zeigt eine bessere Variante
des Bubble Sort Algorithmus

Author:         U. Triltsch
Created:        25.10.2022 21:41
Last modified:  25.10.2022 21:41
"""

meine_liste = [12, 5, 99, 19, 26, 104, 3, 21, 7]
nichtfertig = True
zaehler = 0

while nichtfertig:
    nichtfertig = False
    for j in range(len(meine_liste) - zaehler - 1):
        if meine_liste[j] > meine_liste[j + 1]:
            meine_liste[j], meine_liste[j + 1] = meine_liste[j + 1], meine_liste[j]
            nichtfertig = True
    zaehler += 1

print(meine_liste)
print("Anzahl Iterationen: ", zaehler)
