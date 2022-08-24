from abc import ABC,abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        # print("Running")
        pass

class Lap(Computer):
    # def process(self):
    #     print("Running")
    pass
c=Lap()
c.process()