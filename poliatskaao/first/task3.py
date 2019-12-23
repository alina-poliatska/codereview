"""
Вивести загальну кількість букв в усіх словах рядку
"""
text = ('ghb djnfh hj')
words = text.split()
res = 0
for word in words:
        res += len(word)
print(res)