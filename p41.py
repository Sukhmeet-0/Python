
try:
    a=5
    b=0
    print(a/b)
except Exception as e:
    print(e)
    print("Cant divide number by 0")
finally:
    print("Bye")