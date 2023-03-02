num=int(input("Digite um número: "))
i=1
soma=0
while i<100000:
	ult=num%10
	soma = soma+ult
	num=num//10
	i=i+1
print(soma)