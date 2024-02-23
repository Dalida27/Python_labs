import re
with open('row.txt', 'r') as file:
 data = file.read()


#exercise 6
corrects = data.split()
for i in corrects:
  modify = re.sub(r'[ ,.]', ':', i)
  print(modify)