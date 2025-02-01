s = 50 
f = 100

print("The values: ", end="")
for i in range(s, f+1):
    #print(i)
    if(i % 3 == 0 and i % 5 != 0 ):
        print(i,end=" ")