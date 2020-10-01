'''Escribe un programa que genere una contrasena'''
def contrasena():
    nombre=raw_input("Introduce tu nombre:")
    apellido=raw_input("Introduce tu apellido:")
    print nombre,apellido,"eres el impostor?"
    print "las tres letras iniciales", 3*nombre+2*apellido


contrasena()
