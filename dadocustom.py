'''Elegir un numero al azar entre dos numeros de
tu elección'''
def dado():
    num=input("Desde k numero?")
    num_b=input("Hasta k numero?")
    import random
    dado=random.randint(num,num_b)
    print dado
dado()
