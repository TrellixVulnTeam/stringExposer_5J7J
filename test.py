#Looping through windows api calls. And identifying the category of windows api as per malapi.io
malapiList = ["Enumeration", "Injection"]
for malapicategory in malapiList:
    
    
    #https://www.pythonpool.com/python-remove-newline-from-list/
    #Importing the text into a list. We also have to remove the \n from each line
    myList = open("malapi"+malapicategory+".txt").readlines()
    new_list = []
    for i in myList: #removing the \n and placing into new list. 
        new_list.append(i.replace("\n", ""))
    print(new_list)

