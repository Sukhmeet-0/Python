#swap two variables

a=5
b=7

c=a
a=b
b=c
c=None

a=a+b
b=a-b
a=a-b



print(a)
print(b)

a,b=b,a
print(a)
print(b)