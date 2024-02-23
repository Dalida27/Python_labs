import re
with open('row.txt', 'r') as file:
 data = file.read()


#exercise 5
mylist=[]
corrects = data.split()
for i in corrects:
   match = re.search(r'a.*b$', i)
   if match:
      mylist.append(match.group())

print(mylist)