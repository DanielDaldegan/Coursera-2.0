usuario=int(input("Digite um número:"))
teste=((usuario%5)+(usuario%3))
if teste==0:
    print("FizzBuzz")
else:
    print(usuario)