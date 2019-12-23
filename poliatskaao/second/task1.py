"""
Дано рядок. Перевірити чи починається данний рядок з двох begin, у кожному begin має бути блок end,
команди readln() i writeln() мають лежати в блоці begin end і кожен такий блок має містити
не більш ніж один такий самий блок.
"""


import re

def reg(text):
    return bool(re.match('^(\begin){1}\s((\begin){1}\s(\writeln)(\(\))*\s[a-z](end){1}\s){0,1}[a-z](writeln(\(\)))*\s[a-z](end){1}$',text))


row = input('Enter row: ')
while not reg(row):
    print('NO')
    row = input('Enter row: ')
print('YES')