"""
Grandes mágicos: Comece com uma cópia de seu programa do
Exercício 8.9. Escreva uma função chamada make_great() que modifique a
lista de mágicos acrescentando a expressão o Grande ao nome de cada
mágico. Chame show_magicians() para ver se a lista foi realmente modificada.
"""
def show_magicians(magicians):
    for magician in magicians:
        print(magician)
        
def make_great(great_list):
    magician_great = []
    while great_list:
        magician = great_list.pop()
        magician_great.append('o grande ' + magician)
    print(magician_great)

profissionals = ['patolino', 'pateta', 'mikey']
show_magicians(profissionals)
make_great(profissionals)
show_magicians(profissionals)
