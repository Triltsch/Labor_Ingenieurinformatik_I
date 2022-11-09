"""
Dieses Beispiel zeigt an einem einfachen
Rechner die Anwendung von Exceptions

Author:         U. Triltsch
Created:        08.11.2022 21:23
Last modified:  09.11.2022 16:35
"""


class FormulaError(Exception):
    """
    Eine einfache Exception anlegen. Die Aufgabe fordert dazu auf, dieser
    den Namen FormularError zu geben.
    """
    pass


def parse_input(input_str):
    """
    Diese Funktion verarbeitet den eingegebenen String
    :param input_str: eine Eingabe in der Form Zahl Operator Zahl (z.B. 3 + 3)
    :return: Die drei einzelnen Elemente als zahl_1 (float) operator (str) zahl_2 (float)
    """
    input_list = input_str.split()
    if len(input_list) != 3:
        raise FormulaError("Input does not consist of three elements")
    zahl1, operator, zahl2 = input_list
    try:
        zahl1 = float(zahl1)
        zahl2 = float(zahl2)
    except ValueError as val_err:
        raise FormulaError(val_err) from val_err
    return zahl1, operator, zahl2


def calculate(num_1, operator, num_2):
    """
    Eine eifache Implementierng der Berechnung
    :param num_1: Die erste Zahl
    :param operator: der Operator ('+', '-', '*' oder '/')
    :param num_2: Die zweite Zahl
    :return: das Ergebnis der Berechnung als float
    """
    if operator == "+":
        return num_1 + num_2
    if operator == "-":
        return num_1 - num_2
    if operator == "*":
        return num_1 * num_2
    if operator == "/":
        return num_1 / num_2
    raise FormulaError(f"{0} is not a valid operator".format(operator))


if __name__ == "__main__":
    while True:
        user_input = input(">>> ")
        if user_input == "quit":
            break
        try:
            n1, op, n2 = parse_input(user_input)
            result = calculate(n1, op, n2)
            print(result)
        except FormulaError as form_err:
            print(form_err)
