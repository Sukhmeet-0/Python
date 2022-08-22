#data types

print("Hello")

num=2.5
print(type(num))
num=5
print(type(num))
num=6+9j
print(type(num))

a=5.6
b=int(a)
print(b)
print(type(b))
k=float(b)
print(k)
c=complex(b,k)
print(c)

print(a<b)
bool=a<b
print(bool)

a=int(True)
print(a)
a="a"
print(type(a))
lst=list(range(0,10))
print(lst)
print(type(lst))

d={'name':'Samsung','model':'a50','alternate':'oneplus'}
print(d)
print(d.keys())
print(d.values())
