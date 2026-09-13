from datetime import datetime 
n=int(input())
z=int(input())
x=int(input())
v=int(input())
s=int(input())
current = datetime.now()
target= datetime(2026, n, z, x, v, s)
print(current)
print(target)

bus_no=input("enter bus number") 
for char in bus_no:
    if char == bus_no[0]=="N" and char == bus_no[1]=="1":
        print("bus is going north ",end="")

        


