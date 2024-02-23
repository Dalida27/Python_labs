import re
with open('row.txt', 'r') as file:
 data = file.read()



#exercise 3
mylist=[]
corrects = data.split()
for i in corrects:
    match = re.search(r'\b[a-z]+_[a-z]+\b', i)
    if match:
      mylist.append(match.group())

print(mylist)