'''
Comprehension de cubos: Use uma list comprehension para gerar uma lista
dos dez primeiros cubos.
'''
cube = [value**3 for value in range(1,11)]
for value in cube:
    print(value)