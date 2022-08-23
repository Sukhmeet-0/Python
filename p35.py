class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")


class Laptop:
    def code(self,ide):
        ide.execute();


ide=PyCharm()
lap=Laptop()
lap.code(ide)