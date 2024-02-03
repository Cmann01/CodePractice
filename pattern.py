t = 2
n = 5  # You need to define the value of 'n'

for i in range(1, n+1):
    if i == 1 or i == n:
        print("*" * n)
    else:
        l = "*" + " " * (n-t) + "*"
        print(l)
