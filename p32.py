class Student:
    school="Telusko"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    def average(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1
    def set_m1(self,value):
        self.m1=value
    @classmethod
    def getSchool(cls):
        return cls.school
    @staticmethod
    def info():
        print("This is student class.. in abc molecule")


s1=Student(35,56,79)
s2=Student(65,23,56)

print(s1.average())
print(s2.average())
print(s1.info())
s2.info()