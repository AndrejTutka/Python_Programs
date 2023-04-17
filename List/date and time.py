# import datetime
# 
# right_now = datetime.datetime.now()
# print(right_now)
# 
# 
# # something to take a few milliseconds (or more - depends on your computer)
# for i in range(100):
#     for j in range(50):
#         print(j)
# 
# now2 = datetime.datetime.now()
# print(now2 - right_now)


import datetime

right_now = datetime.datetime.now()
print(right_now)

weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

print(f'Day: {right_now.day}')
print(f'Month: {right_now.month}')
print(f'Year: {right_now.year}')
print(f'Hour: {right_now.hour}')
print(f'Minute: {right_now.minute}')
print(f'Second: {right_now.second}')
print(f'Microsecond: {right_now.microsecond}')
print(f'Weekdays: {right_now.weekday()}')




