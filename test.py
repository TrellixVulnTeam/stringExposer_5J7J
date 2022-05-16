
word_file = open("words.txt", "r")

for aline in word_file:
    values = aline
    print(values)

word_file.close()