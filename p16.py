#for each loop

nums=[125,332,42,14,52,2,1]

for n in nums:
    if(n%5==0):
        print(n)
        break
else:
    print("Not found")