'''
Comprehension de cubos: Use uma list comprehension para gerar uma lista
dos dez primeiros cubos.
'''
cubo = [valor**3 for valor in range(1,11)]
for valor in cubo:
    print(valor)