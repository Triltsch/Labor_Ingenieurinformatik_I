
def meine_Funktion():
    raise NotImplementedError("Lazy Programmer exeption ;-)")

def meine_Funktion2():
    raise MeinError("Test meiner eigenen Ausnahme!")

class MeinError(Exception):
    pass

if __name__ == '__main__':


    while True:
        try:
            n = input("Bitte geben Sie eine ganze Zahl ein: ")
            n = int(n)
            break
        except ValueError as ex:
            print("Keine Ganzzahl! Bitte erneut eingeben ...")
            print(ex)
    print("Sehr gut! Ihre Zahl lautet: ",  n)

    try:
        meine_Funktion2()
    except MeinError as err:
        print (err)



