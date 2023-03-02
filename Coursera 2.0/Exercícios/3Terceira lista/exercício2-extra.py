num=int(input("Digite um número inteiro: "))
ant=num%10
prox=(num//10)%10
result=False
if ant==prox and num>0:
    result=True
else:
    while ant!=prox and ant!=0 and prox!=0:
        num=num//10
        ant=prox
        prox=(num//10)%10
        if ant==prox:
            result=True
        else:
            result=False
if result:
    print("sim")
else:
    print("não")
