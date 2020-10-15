'''Dime un numero al azar del 1 al 10 y lo adivino'''
import random

def adivino ():
    maxn = input("Con cual dificultad quieres jugar de 10 a 1000000: ")
    numero=random.randint(1,maxn)
    guess = input("Que numero crees que es?")
    while guess!=numero:
        if guess>numero:
            print("Demasiado Alto")
        if guess<numero:
            print("Demasiado bajo")
        guess = input("Sigue Intentando:")
    print("Correcto")
adivino()
