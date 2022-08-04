import io
import pandas as pd
from msticpy.transform import IoCExtract


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
            print("[+] Possible "+malapicategory+" action by malware. Windows API call found on this line: "+lines[lineNumber])
            f.close()
            



#https://www.pythonpool.com/python-remove-newline-from-list/
#Importing the text into a list. We also have to remove the \n from each line
#myList = open("words.txt").readlines()
#new_list = []
#for i in myList: #removing the \n and placing into new list. 
#    new_list.append(i.replace("\n", ""))
#for item in new_list: 
#    findline(item) 

print("Searching for Windows API calls in strings file....\n")

#Looping through windows api calls. And identifying the category of windows api as per malapi.io
malapiList = ["Enumeration", "Injection", "Evasion", "Spying", "Internet", "Anti_Debugging", "Ransomware", "Helper"]
for malapicategory in malapiList:
    
    
#https://www.pythonpool.com/python-remove-newline-from-list/
#Importing the text into a list. We also have to remove the \n from each line
    myList = open("malapi"+malapicategory+".txt").readlines()
    new_list = []
    for i in myList: #removing the \n and placing into new list. 
        new_list.append(i.replace("\n", ""))
    for item in new_list:
        findline(item)
            
print("\nNow Extracing any Potential IoCs .... \n")

#Converting the txt file into a csv
df = pd.read_csv('strings.txt')
header_list = ['Strings']
df.to_csv("strings.csv", header=header_list, index=0)

#Extracting and returning any IOCs. Done using msticpy and inbuilt regex. 
df2 = pd.read_csv('strings.csv')
ioc_extractor = IoCExtract()
ioc_df = ioc_extractor.extract(data = df2, columns = ['Strings'])
print(ioc_df)

ioc_df.to_csv("iocList.csv")
