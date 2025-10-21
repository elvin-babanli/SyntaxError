a = int(input("Please add range: "))

list  =[]
x,y = 0,1
for i in range(0,a):
    list.append(x)
    x,y=y,x+y
    
print(list)