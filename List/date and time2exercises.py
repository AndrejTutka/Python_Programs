import datetime

year = input('what year is it: ')

right_now = datetime.datetime.now()
print(right_now)

start_of_spring = datetime.datetime.strptime(f'00:00:01 11/03/{year}', '%H:%M:%S %d/%m/%Y')
if start_of_spring > right_now:
    print(f'The start of spring break is going to happen in {start_of_spring - right_now}')
else:
    print(f'The start of spring break was {right_now - start_of_spring} ago')

start_of_summer  = datetime.datetime.strptime(f'00:00:01 01/07/{year}', '%H:%M:%S %d/%m/%Y')
if start_of_summer > right_now:
    print(f'The start of summer holidays is going to happen in {start_of_summer - right_now}')
else:
    print(f'The start of summer holidays was {right_now - start_of_summer} ago')
    
start_of_christmass = datetime.datetime.strptime(f'00:00:01 23/12/{year}', '%H:%M:%S %d/%m/%Y')
if start_of_christmass > right_now:
    print(f'The start of christmass holidays is going to happen in {start_of_christmass - right_now}')
else:
    print(f'The start of christamass holidays was {right_now - start_of_christmass} ago')