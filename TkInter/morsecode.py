pele_mele = {}

pele_mele[7] = 123456
pele_mele[-123] = 0
pele_mele[1.2] = True
pele_mele[True] = 'Monday'
pele_mele['whatsoever'] = [1,2,3]


print(pele_mele)

del pele_mele[7]

print(pele_mele)

if 7 in pele_mele:
    print('yes 7 is in dictionarz')
else:
    print('no 7 not in dict.')
    
for i in pele_mele:
    print(i)
    
for key,value in pele_mele.items():
    print(f'{key}----->{value}')