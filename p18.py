from array import *

# vals=array('i',[5,3,6,3,2,1])
# print(vals)
# print(vals.buffer_info())
# print(vals.typecode)
# vals.reverse()
# # print(vals)


# newArr=array(vals.typecode,(a*a for a in vals))

# for i in newArr:
#     if(i==25):
#         print(i,end=" ")

# print()




# insertion in array

a=array('i',[])
n=int(input("Enter the size of an array: "))
for i in range(n):
    x=int(input("Enter the value to be inserted: "))
    a.append(x)
# print(a) 



#search
b=int(input("Enter the value to search: "))
for i in a:
    if(i==b):
        print("Value found at index ",i-1)
        break
else:
    print("Value not found")