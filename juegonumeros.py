'''Dime un numero al azar del 1 al 10 y lo adivino'''
def adivino ():
    numero = input("Dime un numero del 1 al 10: ")
    guess = input("Que numero crees que es?")
    while guess!=numero:
        if guess>numero:
            print("Demasiado Alto")
        if guess<numero:
            print("Demasiado bajo")
        guess = input("Sigue Intentando:")
    print("Correcto")
adivino()
