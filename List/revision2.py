list2 = [
          [-35051, -20634, -29421, -18085, -7616],
          [-15964, -32791, -7935, -13033, -3318],
          [-33355, -15122, -49455, -25026, -30682],
          [-14049, -15191, -18057, -42260, -9792],
          [-45336, -11112, -315, -2915, -37014],
          [-18995, -13645, -22921, -5426, -13455],
          [-7577, -47496, -41793, -11898, -14675],
          [-45945, -37238, -4718, -38426, -45984],
          [-47486, -27742, -39747, -8894, -19515],
          [-46716, -30642, -18030, -9152, -7865]
        ]

# get length of the list2 - what does it express?
print(len(list2))
# get the count of numbers in the 3rd sublist
print(len(list2[2]))
# show the last number in the 2nd sublist
print(list2[1][-1])
# swap the first and the last value in the last sublist
list2[-1][0],list2[-1][-1] = list2[-1][-1],list2[-1][0]
print(list2[-1])
# swap the 1st and the 2nd sublist
list2[0],list2[1] = list2[1],list2[0]
print(list2)
# show the smallest value for each sublist
for i in list2:
    print(min(i))

# * Create a piece of code, which transposes the list2 - i.e., rows become columns, and columns become rows
#   Example: a = [[1,2,3], [4,5,6]] --> [[1,4], [2,5], [3,6]]

list3 =[]
# x=0

for i in range(len(list2[0])):
    list3.append([])
    
for sub in list2:
    for i in range(len(sub)):
        list3[i].append(sub[i])
        
# print(list3)
# while x < len(list2):
#     
#     list3.insert(x,list2[x][0])
# 
#     x+=1



   

print(list3)
# list3.insert(1,list2[1][0])
# list3.insert(2,list2[2][0])
# list3.insert(2,list2[2][0])
