list = open("words.txt").readlines()
new_list = []
for i in list:
    new_list.append(i.replace("\n", ""))
    
print(new_list)

