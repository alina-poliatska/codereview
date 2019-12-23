"""
Вивести максимальне число зі списку
"""

text = ('h','ejk',1,5,8,11,20,3)
list = 0
for element in text:
    if isinstance(element,int):
        list += element
    else:
        continue
print(max(list))