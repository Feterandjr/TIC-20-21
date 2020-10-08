'''Haz una contraseña con tres letras
de tu nombre y 3 de tu apellido'''
def contrasena():
    import random
    name=raw_input("Ur name?")
    apellido=raw_input("Ur surname?")
    print "Ur password is: "+name[0:3]+apellido[0:3]
contrasena()
