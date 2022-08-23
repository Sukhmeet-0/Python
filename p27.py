# anonymous function
#f=lambda a:a*a
from functools import reduce


f=lambda a,b : a*b
print(f(5,6))



#filter map reduce

# def is_even(n):
#     return n%2==0




nums=[1,23,3,24,2,52,52,5235,252,2,3,23,1,13,33,113,31]
# evens=list(filter(is_even,nums))

evens=list(filter(lambda n:n%2==0,nums))
print(evens)

doubles=list(map(lambda n:n*2,evens))
print(doubles)

from functools import reduce
def add_all(a,b):
    return a+b
sum=reduce(lambda a,b:a+b,doubles)
print(sum)