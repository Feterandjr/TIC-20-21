'''Me va a pedir el numero de un mes y
me va a devolver la abreviatura del mes'''
def mes():
    abreviaMes="EneFebMarAbrMayJunJulAgoSepOctNovDic"
    numMes=input("Introduce mes:")
    pos=(numMes-1)*3
    print"El mes es",abreviaMes[pos:pos+3]

mes()    
