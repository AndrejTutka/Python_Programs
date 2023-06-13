import random
import string
# table = [
#     ['D','N','E','S'],
#     ['J','E','U','T'],
#     ['O','R','O','K'],
#     ['P','I','A','T'],
#     ['Y','Q','X','T']
#     ]
text = 'DNES JE UTOROK PIATY'

for symbol in '.:;?':
    text = text.replace(symbol, '')
text = text.replace(' ', '')
text = text.upper()

table = []
width = 4


if len(text) % width !=0:
    diff = width - len(text)% width
    for i in range(diff):
        text+= random.choice(string.ascii_uppercase)
        
print(text)
for start_line in range(0, len(text),width):
    line=list(text[start_line:start_line + width])
    table.append(line)
    
print(table)
    
    












# for j in range(len(table[0])):             
#     for i in range(len(table)):
#         print(table[i][j],end ='')

    
    
