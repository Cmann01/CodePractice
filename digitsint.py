def countDigit(n):
    digit=0
    while n !=0:
        n//=10
        digit+=1
    return digit

n=78673
print("Nuber of digits :%d "%(countDigit(n)))
