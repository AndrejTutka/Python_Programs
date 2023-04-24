import random

x=0
tips = []
while x < 1000000:
    tip=set()
    while len(tip) <6:
        tip.add(random.randint(1,49))
    
    x+=1
    tips.append(tip)
draw = set()
while len(draw) <6:
        draw.add(random.randint(1,49))
y=0
place1=set()
place2=set()
place3=set()
place4=set()
place5=set()
place6=set()
place7=set()
    

while y < 1000000:
    set3 = draw & tips[y]
    
    y+=1
    if len(set3)==6:
        place1.add(y)
    if len(set3)==5:
        place2.add(y)
    if len(set3)==4:
        place3.add(y)
    if len(set3)==3:
        place4.add(y)
    if len(set3)==2:
        place5.add(y)
    if len(set3)==1:
        place6.add(y)
    if len(set3)==0:
        place7.add(y)
        
print(f'WINNER={place1},2nd place{place2},3rd place={place3},4th place={place4},5th place={place5},6th place={place6},LOSER={place7}')


        

