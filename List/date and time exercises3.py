import datetime

year = input('what year is it: ')
month = input('what month is it: ')
day = input('what day is it: ')
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
right_now = datetime.datetime.now()
print(right_now)

date = datetime.datetime.strptime(f'{day}/{month}/{year}', '%d/%m/%Y')
if date> right_now:
    print(f'your date will happen in {date - right_now}')
else:
    print(f'your date heppened {right_now - date} ago')
    
date2 = datetime.datetime.strptime(f'{year}-{month}-{day}', '%Y-%m-%d')
    
print(f'Weekday: {weekdays[date2.weekday()]}')

date3 = datetime.datetime.strptime(f'{year}-01-01', '%Y-%m-%d')

print(f'your date will happen in {right_now - date3}')