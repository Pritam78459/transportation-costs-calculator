name = input('Enter name of the customer =')
vname = input('Enter name of the vehicle =')
distance = 6000
if  distance < 100:
    print(f'22 per kilometer applicable')
    ndistance = distance*22
    print(f'Total value without GST is = {ndistance}')
    GST = ndistance*0.12
    print(f'GST value is ={GST}')
    NET = ndistance + GST
    print(f'Total value including GST is {NET}')
elif 100 < distance <= 250:
    print(f'18 per kilometer applicable')
    ndistance = distance * 18
    print(f'Total value without GST is = {ndistance}')
    GST = ndistance * 0.12
    print(f'GST value is ={GST}')
    NET = ndistance + GST
    print(f'Total value including GST is {NET}')
elif 250 < distance <= 500:
    print(f'15 per kilometer applicable')
    ndistance = distance * 15
    print(f'Total value without GST is = {ndistance}')
    GST = ndistance * 0.12
    print(f'GST value is ={GST}')
    NET = ndistance + GST
    print(f'Total value including GST is {NET}')
elif 500 < distance <= 1000:
    print(f'13 per kilometer applicable')
    ndistance = distance * 13
    print(f'Total value without GST is = {ndistance}')
    GST = ndistance * 0.12
    print(f'GST value is ={GST}')
    NET = ndistance + GST
    print(f'Total value including GST is {NET}')
elif distance > 1000:
    print(f'11 per kilometer applicable')
    ndistance = distance * 11
    print(f'Total value without GST is = {ndistance}')
    GST = ndistance * 0.12
    print(f'GST value is ={GST}')
    NET = ndistance + GST
    print(f'Total value including GST is {NET}')