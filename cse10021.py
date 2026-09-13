from datetime import datetime 
n=int(input("enter the month"))
z=int(input("enter the day"))
x=int(input("enter the hour(24hour format)"))
v=int(input("enter the minute"))
current = datetime.now()
target= datetime(2026, n, z, x, v,)
remaining_time= target - current
bus_no=input("enter bus number") 
code=bus_no[:2]
if code == "N2":
    print("bus is going to DELHI",remaining_time)
elif code == "N1":
    print('bus is going to JAMMU', remaining_time)
elif code == "N3":
    print('bus is going to chandigarh',remaining_time)
elif code == "N4":
    print('bus is going to shimla', remaining_time)
elif code == "E1":
    print('bus is going to GHUWAHATI', remaining_time)
elif code == 'E2':
    print('bus is going to kolkata', remaining_time)
elif code == 'E3':
    print('bus is going to patna', remaining_time)
elif code== 'S1':
    print('bus is going to hydreabad', remaining_time)
elif code== 'S2':
    print('bus is going to bangalore', remaining_time)
elif code =='S3':
    print('bus is going to chennai', remaining_time)
elif code =='W1':
    print('bus is going to mumbai', remaining_time)
elif code =='W2':
    print('bus is going to ahemdabad', remaining_time)
elif code =='W3':
    print('bus is going to surat', remaining_time)
elif code =='W4':
    print('bus is going to jaipur', remaining_time)
else:
    print("bus is cancelled")
    