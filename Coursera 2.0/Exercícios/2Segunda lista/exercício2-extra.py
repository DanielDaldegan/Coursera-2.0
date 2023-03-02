import math
print("vamos resolver uma equação de segundo grau:")
valorA=int(input("favor inserir o valor da variável A:"))
if valorA == 0:
    valorA=int(input("A=0 indica uma equação de primeiro grau. Favor inserir um valor diferente:"))
valorB=int(input("favor inserir o valor da variável B:"))
valorC=int(input("favor inserir o valor da variável C:"))
delta=(valorB**2)-(4*valorA*valorC)
 
if delta == 0:
    result = valorB/(2*valorA)
    print("a raiz desta equação é",result)
        
else:
    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
        resultPos = (valorB + (math.sqrt(delta)))/(2*valorA)
        resultNeg = (valorB - (math.sqrt(delta)))/(2*valorA)
        if resultPos>=resultNeg:
            print("as raízes da equação são",resultNeg,"e",resultPos)
        else:
            print("as raízes da equação são",resultPos,"e",resultNeg)