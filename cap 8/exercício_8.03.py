"""
Camiseta: Escreva uma função chamada make_shirt() que aceite um
tamanho e o texto de uma mensagem que deverá ser estampada na camiseta.
A função deve exibir uma frase que mostre o tamanho da camiseta e a
mensagem estampada.
Chame a função uma vez usando argumentos posicionais para criar uma
camiseta. Chame a função uma segunda vez usando argumentos nomeados.
"""
def make_shirt(size, text_print):
    print('camisa de tamanho '  + size + ' com a estampa ' + '"' + text_print + '"')

make_shirt(text_print='deus não joga dados', size='gg')
make_shirt('gg', "deus não joga dados")