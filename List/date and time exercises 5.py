import datetime

year = input('what year is it: ')

date = datetime.datetime.strptime(f'{year}-01-01', '%Y-%m-%d')


for i in range(365):
    difference = datetime.timedelta(days = 1)        
    date= date+difference
    if date.weekday() in [5,6]:
        print(f'weekend: {date}')

   
