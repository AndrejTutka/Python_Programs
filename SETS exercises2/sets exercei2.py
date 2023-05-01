# define a translation table to remove punctuation symbols
translator = str.maketrans('', '', '.,;:!?\'"()[]{}')

# open the file and read its contents
with open("C:\Users\tutka\Downloads\filename.txt", 'r',encoding = 'utf-8') as f:
    text = f.read()

# remove punctuation symbols and convert to lowercase
text = text.translate(translator).lower()

# split the text into words using spaces as separators
words = text.split()

# convert the list of words to a set to count unique words
unique_words = set(words)

# print the count of unique words
print(len(unique_words))