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

def findline(values):
    #print(values)
    for i in range(len(arr)):        
        if values in arr[i]:
            #print(values)
            #print(i+1)
            lineNumber = i
            #https://stackoverflow.com/questions/2081836/how-to-read-specific-lines-from-a-file-by-line-number
            f=open('strings.txt')
            lines=f.readlines()
            print(lines[lineNumber])
            f.close()
            



#https://www.pythonpool.com/python-remove-newline-from-list/
#Importing the text into a list. We also have to remove the \n from each line
#myList = open("words.txt").readlines()
#new_list = []
#for i in myList: #removing the \n and placing into new list. 
#    new_list.append(i.replace("\n", ""))
#for item in new_list: 
#    findline(item) 



#Looping through windows api calls. And identifying the category of windows api as per malapi.io
malapiList = ["Enumeration", "Injection"]
for malapicategory in malapiList:
    
    
#https://www.pythonpool.com/python-remove-newline-from-list/
#Importing the text into a list. We also have to remove the \n from each line
    myList = open("malapi"+malapicategory+".txt").readlines()
    new_list = []
    for i in myList: #removing the \n and placing into new list. 
        new_list.append(i.replace("\n", ""))
    for item in new_list:
        findline(item)
            
