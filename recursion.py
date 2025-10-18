'''def feb(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:

           return feb(n-1)+feb(n-2)
n=6
print(feb(n))
'''
n=6
for i in range(0,n+1):
    if n==0:
        n=1
    else:
        n=n*(i)
print(n)
