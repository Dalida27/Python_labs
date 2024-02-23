import re 

with open('row.txt', 'r') as file:
    data = file.read()

# Exercise 9

corrects = data.split()
for i in corrects:
    modify = re.sub(r'[A-Z][a-b]*', ' ', i)
    print(modify)