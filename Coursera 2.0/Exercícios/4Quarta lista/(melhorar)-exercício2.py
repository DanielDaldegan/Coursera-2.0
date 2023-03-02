def maior_primo(num):
    import math
    while num>0:
        if (num%2==0) or (num%3==0) or (num%5==0) or (num%math.sqrt(num)==0):
            num-=1
        else:
            return num
