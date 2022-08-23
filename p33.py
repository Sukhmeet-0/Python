class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()
    def show(self):
        print(self.name, self.rollno)


    class Laptop:
        def __init__(self):
            self.brande='HP'
            self.cpu='i9'
            self.ram=32

s1=Student('Navin',2)
s1.show()
print(s1.lap.brande)