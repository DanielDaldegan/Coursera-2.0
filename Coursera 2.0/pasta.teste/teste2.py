import math

def calc_delta(a,b,c):
    delta=(b**2)-(4*a*c)
    return delta

def raizes(a,b,delta):
    if delta == 0:
        result = b/(2*a)
        print("a raiz desta equação é",result)
            
    else:
        if delta < 0:
            print("esta equação não possui raízes reais")
        else:
            resultPos = (b + (math.sqrt(delta)))/(2*a)
            resultNeg = (b - (math.sqrt(delta)))/(2*a)
            if resultPos>=resultNeg:
                print("as raízes da equação são",resultNeg,"e",resultPos)
            else:
                print("as raízes da equação são",resultPos,"e",resultNeg)

print("vamos resolver uma equação de segundo grau:")
a=int(input("favor inserir o valor da variável A:"))
if a == 0:
    a=int(input("A=0 indica uma equação de primeiro grau. Favor inserir um valor diferente:"))
b=int(input("favor inserir o valor da variável B:"))
c=int(input("favor inserir o valor da variável C:"))
delta=calc_delta(a,b,c)
raizes(a,b,delta)
