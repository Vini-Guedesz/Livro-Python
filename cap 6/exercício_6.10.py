"""
Números favoritos: Modifique o seu programa do Exercício 6.2 para que cada
pessoa possa ter mais de um número favorito. Em seguida, apresente o nome de
cada pessoa, juntamente com seus números favoritos.
"""
num_favs = {
    'ricardo' : [5, 8, 3],
    'cezar' : [7, 9],
    'igor' : [9, 13],
    'arthur' : [3, 15, 7],
    'vini' : [7, 5]
}
for name, num in num_favs.items():
    print(name + ' tem como números favoritos: ' + str(num))