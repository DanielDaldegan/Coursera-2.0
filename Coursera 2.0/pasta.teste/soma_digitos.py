num=int(input("Digite um número: "))
i=1
soma=0
while i<100000:
	ult=num%10
	soma = soma+ult
	num=num//10
	i=i+1
	if num==0 and num//10==0:
		print(soma)
		quit()