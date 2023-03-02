num=int(input("Digite o valor de n: "))
if num==0:
    print("1")
else:
    soma=num
    while num!=1:
        num-=1
        soma=soma*num
    print(soma)