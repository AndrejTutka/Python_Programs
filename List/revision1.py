# Part 1

list1 = [41793, -7577, -18085, 22921, 13645, 9792, 27742, 15964, 49455, -7865, 37238, 35051, 47486, 18995, 18030, 45945, 19515, 29421, -18057, 33355, -15191, 14675, 2915, -14049, -7616, 8894, -9152, 38426, -7935, 11112, 3318, 39747, 25026, 46716, -4718, -13033, -15122, 47496, 32791, 37014, 45336, 315, 45984, 30642, 42260, 30682, 20634, 13455, -11898, 5426]

# Display:
#  the 1st element
print(f'the first element of the list is {list1[0]}')
#  the last element
print(f'the last element of the list is {list1[-1]}')
#  swap the second and next-to-last element

(list1[1],list1[-2]) = (list1[-2],list1[1])


print(f'the list with second and next-to-last swaped is {list1[:]}')

#  get the count of numbers in the list
print(f'there are {len(list1)} numbers')

#  get the sum of all numbers in the list
print(f'sum of all umbers is {sum(list1)}')
#  get the greatest element
print(f'greatest element is {max(list1)}')

#  get the smallest element
print(f'smallest element is {min(list1)}')
#  get the position of the greatest element
print(f'pos. of the greatest element is {list1.index(max(list1))}')
#  get the position of the smallest element
print(f'pos. of the smallest element is {list1.index(min(list1))}')

#  get the element of the lowest ABSOLUTE value

# list2 = [abs(i) for i in list1]
# 
# # print(str(list2))
# print(min(list2))
print(f'lowest absolute value is {min(list1, key=abs)}')


#  get the number of positive values
counter=0
for i in list1:
    if i >=0:
        counter+=1
        
print(f'number of positive values is {counter}')

#  sort the numbers
list1.sort()

#  erase the first 2 numbers from the list
list1 = list1[2:]

#  add 77777777 at the end of the list
list1.append(77777777)

#  add 55555555 at the beginning of the list
list1.insert(0, 55555555)
print(list1)
#  add 33333333 to the middle of the list

#  merge the list1 with this list: [23, 45, 56, 78]

#  create and independent copy of the list1

#  make the list1 empty

