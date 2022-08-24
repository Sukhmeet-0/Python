from threading import Thread


from threading import *
from time import *
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t=Hello()
tt=Hi()

t.start()
sleep(0.2)
tt.start()

t.join()
tt.join()

print("Bye")
