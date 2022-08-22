from numpy import *
a=array([
    [1,2,3,2],
    [4,5,6,6]
])
# print(a)
m=matrix(a)
print(m)
print()
print()
l=matrix('1,2,3;4,5,6')
print(l)
print()
print(diagonal(m))



a=matrix('1,2;3,4')
b=matrix('1,2;3,4')
c=a*b
print(c)



# print(a.ndim)
# print(a.shape)
# print(a.size)
# b=a.flatten()
# print(b)
# c=b.reshape(3,4)
# print(c)
# d=b.reshape(2,2,3)
# print(d)
