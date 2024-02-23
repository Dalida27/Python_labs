import re

def snake_to_camel(match):
    return match.group(0)[1:].capitalize()

with open('row.txt', 'r') as file:
    data = file.read()
    corrects = data.split()

    for i in corrects:
        if '_' in i:
            modify = re.sub(r'_([a-z])', snake_to_camel, i)
            print(modify)
