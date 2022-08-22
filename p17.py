# find if a number is prime

num=int(input("Enter a number: "))
for i in range(2,int(num/2)):
    if(num%i==0):
        print("Not Prime number")
        break
else:
    print("Prime Number")

    