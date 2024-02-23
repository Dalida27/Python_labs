import re
with open('row.txt', 'r') as file:
 data = file.read()
 
#exercise 2
mylist = []
corrects = data.split()
for i in corrects:
    match = re.search(r'a[b]{2,3}', i)
    if match:
      mylist.append(match.group())

print(mylist)
