import re
with open('row.txt', 'r') as file:
 data = file.read()


#exercise 4
mylist = []
corrects = data.split()
for i in corrects:
    match = re.search(r'[A-Z][a-z]+', i)
    if match:
     mylist.append(match.group())

print(mylist)