

def word_frenquencies(my_list: list) -> dict:
    result = {}
    for word in my_list:
        if word in result:
            result[word] +=1
        else:
            result[word] = 1
            
    return result

text = input('enter a text:  ')

unwanted = []
for symbol in text:
    if not symbol.isalpha() and symbol != ' ':
        unwanted.append(symbol)

for symbol in unwanted:
     text = text.replace(symbol, '')

text = text.split()
print(word_frenquencies(text))


