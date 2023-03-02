def fat(n):
    fat=1
    while n>1:
        fat=fat*n
        n-=1
    return fat

n=int(input("Digite o valor de n: "))
k=int(input("Digite o valor de k: "))
fatN=fat(n)
print(fatN)
fatK=fat(k)
print(fatK)
fatNK=fat(n-k)
print(fatNK)
result=fatN/(fatK*fatNK)
print(result)










#print("O valor de %d elevado a %d eh %d" %(n, k, pot)) # mais elaborado