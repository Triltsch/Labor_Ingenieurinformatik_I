"""
Dieses Beispiel zeigt eine einfache (aber auch ineffiziente) Variante
des Bubble Sort Algorithmus

Author:         U. Triltsch
Created:        25.10.2022 21:41
Last modified:  25.10.2022 21:41
"""

meine_liste = [12, 5, 99, 19, 26, 104, 3, 21, 7]

for i in range(len(meine_liste), 0, -1):
    for j in range(len(meine_liste) - 1):
        if meine_liste[j] > meine_liste[j + 1]:
            meine_liste[j], meine_liste[j + 1] = meine_liste[j + 1], meine_liste[j]

print(meine_liste)
