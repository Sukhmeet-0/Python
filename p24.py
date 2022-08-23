#global

# a=10
# def add():
#     # global a
    
#     a=9
#     # x=globals()['a']
#     print(a)
#     # print(x)


# add()
# print(a)

#passing list in functions

even=0;odd=0

lst=[1,2,3,4,5,5,6,6]
# def add(l):
for i in lst:
    if(i%2==0):
        even+=1
    else:
        odd+=1
# add(lst)
print("Even: {} Odd: {}".format(even,odd))


def countt(l):
    even=0;odd=0
    for i in l:
        if(i%2==0):
            even+=1
        else:
            odd+=1
    print("Even : {}  Odd : {}".format(even,odd))

countt(lst)
