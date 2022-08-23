# factorial

def factorial(n):
    x=1
    for i in range(1,n+1):
        x=x*i
    print(x)
        
factorial(4)



def fact(n):

    if(n==0):
        return 1
    return n*fact(n-1)

r=fact(5)

print(r)