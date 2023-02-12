"""
Camisetas grandes: Modifique a função make_shirt() de modo que as
camisetas sejam grandes por default, com uma mensagem Eu amo Python. Crie
uma camiseta grande e outra média com a mensagem default, e uma camiseta
de qualquer tamanho com uma mensagem diferente.
"""
def make_shirt(size='grande', text_print='eu amo pyhton'):
    print('camisa de tamanho '  + size + ' com a estampa ' + '"' + text_print + '"')

make_shirt()
make_shirt('média')
make_shirt(text_print='eu gosto de linux')