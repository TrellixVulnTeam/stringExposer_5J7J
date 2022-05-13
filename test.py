#https://www.geeksforgeeks.org/how-to-obtain-the-line-number-in-which-given-word-is-present-using-python/

# READ FILE
df = open("strings.txt")
 
# read file
read = df.read()
 
# return cursor to
# the beginning
# of the file.
df.seek(0)
read

# create empty list
arr = []
 
# count number of
# lines in the file
line = 1
for word in read:
    if word == '\n':
        line += 1
#print("Number of lines in file is: ", line)
 
for i in range(line):
    # readline() method,
    # reads one line at
    # a time
    arr.append(df.readline())

def findline(word):
    for i in range(len(arr)):
        if word in arr[i]:
            #print(i+1)
            lineNumber = i
            #https://stackoverflow.com/questions/2081836/how-to-read-specific-lines-from-a-file-by-line-number
            f=open('strings.txt')
            lines=f.readlines()
            print(lines[lineNumber])
            

#Now we want to print those line numbers of i+1

#myList = ["cat", "week"]
#for item in myList:
#    findline(item)


word_file = open("words.txt", "r")

for aline in word_file:
    values = aline
    findline(values)

#word_file.close()