# object oriented programming

class Computer:
    # def config(self):

    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        print("In init")


    def config(self):
        print(self.cpu,self.ram,"1TB")


a=Computer("I5",8)
b=Computer("Ryzen 5",8)

a.config()
b.config()
# Computer.config(a)



