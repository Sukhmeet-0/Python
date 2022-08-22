# def update(x):

#     print(id(x))

#     x=8
#     print(id(x))
#     print(x)
# a=10
# print(id(a))
# update(a)

def add(a, *b): #5 will go to a and rest all numbers will go to b as tuples becuase of asterik sign
    c=a+sum(b)
    print(c)

add(5,5,7,5,8)

def person(name,age=18):
    print(name , age)

person('sukhmeet',21)
person(age=21,name='sukhmeet')



def person(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i, j)

person('navin',age=21,city='Mumbai')