def contador():
    palabra=raw_input("Que palabra quieres saber cuantas letras tiene?")
    numero=0
    for cont in range(0,40):
        if (palabra[cont]=='a'or palabra[cont]=='b' or palabra[cont]=='c'
            or palabra[cont]=='d' or palabra[cont]=='e' or palabra[cont]=='f'
            or palabra[cont]=='g' or palabra[cont]=='h' or palabra[cont]=='i'
            or palabra[cont]=='j' or palabra[cont]=='k' or palabra[cont]=='l'
            or palabra[cont]=='m' or palabra[cont]=='n' or palabra[cont]=='o'
            or palabra[cont]=='p' or palabra[cont]=='q' or palabra[cont]=='r'
            or palabra[cont]=='s' or palabra[cont]=='t' or palabra[cont]=='u'
            or palabra[cont]=='v' or palabra[cont]=='w' or palabra[cont]=='x'
            or palabra[cont]=='y' or palabra[cont]=='z'):
            numero=numero+1
            print numero
        else:
            print palabra[cont]

contador()
