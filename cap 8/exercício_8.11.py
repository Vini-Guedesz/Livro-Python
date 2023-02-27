"""
Mágicos inalterados: Comece com o trabalho feito no Exercício 8.10.
Chame a função make_great() com uma cópia da lista de nomes de mágicos.
Como a lista original não será alterada, devolva a nova lista e armazene-a em
uma lista separada. Chame show_magicians() com cada lista para mostrar que
você tem uma lista de nomes originais e uma lista com a expressão o Grande
adicionada ao nome de cada mágico.
"""
def show_magicians(magicians):
    for magician in magicians:
        print(magician)
        
def make_great(great_list):
    magician_great = []
    while great_list:
        magician = great_list.pop()
        magician_great.append('o grande ' + magician)
    return(magician_great)

profissionals = ['patolino', 'pateta', 'mikey']
great_profissionals = make_great(profissionals[:])
show_magicians(great_profissionals)
show_magicians(profissionals)