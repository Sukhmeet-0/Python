from operator import truediv


class Student:
    def __init__(self,m1,m2) :
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2=other.m2
        return Student(m1,m2)
    def __gt__(self,other):
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if(r1>r2):
            return True
        else:
            return False
    def __str__(self):
        return self.m1, self.m2

a=Student(58,48)
b=Student(48,39)

c=a+b
print(c.m1)


if(a>b):
    print("a wins")
else:
    print("b wins")

print(a.__str__())