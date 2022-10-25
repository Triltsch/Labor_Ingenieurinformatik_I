# Dieses erste Beispielprojekt soll die grundlegende Arbeit
# mit PyCharm und Debugger demonstrieren.


# Autor: U. Triltsch
# Erstellt am: 04.10.021
# Letzte Aenderung am: 05.10.2021

# Ihre Beschreibung kommt hier hin...
def algorithm(number):

    teilergebnis = number/2.0
    g2 = teilergebnis + 1
    while(teilergebnis != g2):
        n = number/ teilergebnis
        g2 = teilergebnis
        teilergebnis = (teilergebnis + n)/2

    return teilergebnis

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #HIPO- Principle
    #Input
    number = float(input("Please input a number:\n"))
    #Process  --> What is happening here?
    result = algorithm(number)
    #Output
    print("The result of the operation on: ", number, "is: ", result)


