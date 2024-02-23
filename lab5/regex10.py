import re

def camel_to_snake(match):
    return '_' + match.group(0).lower()

with open('row.txt', 'r') as file:
    data = file.read()
    corrects = data.split()

    for i in corrects:
        modify = re.sub(r'(?<!^)([A-Z])', camel_to_snake, i)
        print(modify.lower())
