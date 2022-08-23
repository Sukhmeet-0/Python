class Computer:
    def __init__(self):
        self.name="Navin"
        self.age=21

    def update(self):
        self.age=30

    def compare(self,other):
        if(self.age==other.age):
            return True
        else:
            return False


c1=Computer()
# c1.update()
c2=Computer()
c2.name='Sukhmeet'

print(c1.name)
print(c2.name)
print(c1.age)
print(c2.age)

if c1.compare(c2):
    print("They are same")
else:
    print("Not same")