'''
Berechnung der Fakultät einer Zahl
Autor: U. Triltsch

Letzte Änderung: 21.10.2021

'''

def fak(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fak(n - 1)
'''
zahl = int(input("Bitte geben Sie die Zahl ein, deren Fakultät berechnet werden soll!\n"))
erg = fak(zahl)
print(erg)
'''

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

zahl = int(input("Bitte geben Sie die Zahl ein!\n"))
erg = fib(zahl)
print(erg)









def fib(n):
    if n == 0:
      return 0
    elif n == 1:
      return 1
    else:
      return fib(n-1) + fib(n-2)

# berechnet die Zahl an der i-ten Stelle des Dreiecks in Abhängigkeit der übergebene Zeile
def pascal_rekursiv(zeile, zahl_i):
    if zahl_i == 0 or zahl_i == zeile:
        return 1
    else:
      return pascal_rekursiv(zeile - 1, zahl_i - 1) + pascal_rekursiv(zeile - 1, zahl_i)

def pascals_triangle(n):
    """ Recursive function to calculate Pascals Triangle """
    if n == 1:
        print (1)
        return [[1]] # Base case termination condition
    else:
        result = pascals_triangle(n-1) # Recursive call
        # Calculate current row using info from previous row
        current_row = [1]
        previous_row = result[-1] # Take from end of result
        for i in range(len(previous_row)-1):
            current_row.append(previous_row[i] + previous_row[i+1])
        current_row += [1]
        result.append(current_row)
        return result


# n = int(input("Wie viele Zeilen soll das Dreieck haben?"))
#
# triangle = pascals_triangle(n)
# for row in triangle:
#    print(row)
#
# #print (pascal_rekursiv(3, 2), end = " ")
#
#
# #Iteration über die Zeilen
# for i in range(n):
#     #Iteration über die Spalten (immer i)
#     for zahl in range(i + 1):
#        # if zahl == 0 or zahl == i:
#        #     print(1, end=" ")
#        # else:
#         print (pascal_rekursiv(i, zahl), end = " ")
#     print("")
#
# #ergebnis = fib(n)
# #print("Ergebnis: ", ergebnis)

