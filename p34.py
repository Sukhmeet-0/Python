# class A:
#     def feature1(self):
#         print("Feature 1 working")
#     def feature2(self):
#         print("Feature 2 working")


# # class B(A):
# #     def feature3(self):
# #         print("Feature 3 working")
# #     def feature4(self):
# #         print("Feature 4 working")
# class B():
#     def feature3(self):
#         print("Feature 3 working")
#     def feature4(self):
#         print("Feature 4 working")
# class C(A,B):
#     def feature5(self):
#         print("Feature 5 working")

# # a=A()
# # a.feature1()
# # a.feature2()

# # b=B()
# c=C()
# c.feature1()
# c.feature2()
# c.feature3()
# c.feature4()
# c.feature5()




class A:
    def __init__(self):
        print("A")
    # def feature1(self):
    #     print("Feature 1 working")
    # def feature2(self):
    #     print("Feature 2 working")


# class B(A):
class B():
    def __init__(self):
        # super().__init__()
        print("B")
    # def feature3(self):
    #     print("Feature 3 working")
    # def feature4(self):
    #     print("Feature 4 working")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("C")
c=C()