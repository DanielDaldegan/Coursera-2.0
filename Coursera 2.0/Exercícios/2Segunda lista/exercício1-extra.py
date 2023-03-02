import math
x1=int(input("Digite x1:"))
y1=int(input("Digite y1:"))
x2=int(input("Digite x2:"))
y2=int(input("Digite y2:"))
d=math.sqrt(((x1-x2)**2)+((y1-y2)**2))
if d>=10:
    print("longe")
else:
    print("perto")