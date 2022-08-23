#fibonacci series

def fib(n):
    a=0
    b=1
    if(n==0):
        print(a)
    elif(n==1):
        print(b)
    elif(n<0):
        print("Invalid number !!")
    else:
        print(a,end=" ")
        print(b,end=" ")
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c,end=" ")


fib(5)