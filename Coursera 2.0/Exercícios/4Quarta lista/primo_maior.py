import math
num=int(input("Digite um número: "))
#10
i=num
j=0
while i<=num:
    if (num%i==0):
        result=num
        i+=1
        j+=1
    else:
        i-=1

        

"""
num=int(input("Digite um número inteiro: "))
i=2
j=0
while i<=num:
    if num%i==0:
        result=True
        j+=1
    else:
        result=False
    i+=1
if result and j<=1:
    print("primo")
else:
    print("não primo")"""