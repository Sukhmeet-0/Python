# decorators

def div(a,b):
    print(a/b)

# div(4,2)

def smartDiv(func):
    def inner(a,b):
        if(a<b):
            a,b=b,a
        return func(a,b)
    return inner
div1=smartDiv(div)
# div(2,4)
div1(2,4)
