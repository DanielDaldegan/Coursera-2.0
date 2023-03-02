import math

n1=int(input("Digite um número:"))

par=0
impar=0

if n1%2==0 or n1=='S':
    par=par+1
    n1=int(input("Digite um número ou S para sair:"))
if n1%2!=0 or n1=='S':
    impar=impar+1
    n1=int(input("Digite um número ou S para sair:"))
print("há",par,"números pares e",impar,"números impares")



