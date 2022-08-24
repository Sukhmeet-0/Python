

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def sum(self,a=None,b=None,c=None):
        if(a!=None and b!=None and c!=None):
            s=a+b+c

        #so on...

        return s
    def show(self):
        print("Student")



class Student2(Student):
    pass
    # def show(self):
    #     print("Student 2")


s1=Student2(56,45)
# print(s1.sum(1,2,3))

s1.show()