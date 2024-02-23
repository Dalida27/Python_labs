import re 

with open('row.txt', 'r') as file:
    data = file.read()

# Exercise 8
mylist = []
corrects = data.split()
for i in corrects:
    matches = re.findall(r'[A-Z][a-z]*', i)
    if matches:
        mylist.append(matches)

print(mylist)
