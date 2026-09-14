from datetime import datetime 
n=int(input("enter the month"))
z=int(input("enter the day"))
x=int(input("enter the hour(24hour format)"))
v=int(input("enter the minute"))
current = datetime.now()
target= datetime(2026, n, z, x, v,)
remaining_time= target - current
bus_no = input("Enter bus number: ")
code = bus_no[:2]
routes = {
    "N1": "JAMMU",
    "N2": "DELHI",
    "N3": "CHANDIGARH",
    "N4": "SHIMLA",
    "E1": "GUWAHATI",
    "E2": "KOLKATA",
    "E3": "PATNA",
    "S1": "HYDERABAD",
    "S2": "BANGALORE",
    "S3": "CHENNAI",
    "W1": "MUMBAI",
    "W2": "AHMEDABAD",
    "W3": "SURAT",
    "W4": "JAIPUR"
}
if code in routes:
    print("Bus is going to", routes[code])
    print("Remaining time:", remaining_time)
else:
    print("Bus is cancelled")
