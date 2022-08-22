from numpy import *
a=array([1,2,3,4,5])
b=array([6,7,8,9,10])


c=a+b

print(c)
print(sin(c))
print(cos(c))
print(log(c))
print(sqrt(c))
print(sum(c))
print(min(c))
print(max(c))
# d=c.view()
# d=c
d=c.copy()
print(d)
print(id(c))
print(id(d))