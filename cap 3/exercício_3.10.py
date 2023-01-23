'''
Todas as funções: Pensa em algo que você poderia armazenar em uma
lista. Por exemplo, você poderia criar uma lista de montanhas, rios, países,
cidades, idiomas ou qualquer outro item que quiser. Escreva um programa que
crie uma lista contendo esses itens e então utilize cada função apresentada
neste capítulo pelo menos uma vez.
'''
convidados_casamento = ['andy', 'louis', 'suzy', 'harry']
convidados_casamento.insert(2, 'marcos')
del convidados_casamento[0]
convidados_casamento.pop(-1)
convidados_reverse = sorted(convidados_casamento)
convidados_ordem = sorted(convidados_casamento, reverse=True)
print('ao total são '+ str(len(convidados_casamento)) + ' convidados!!!')
print('essa é a lista de convidados em ordem alfabetica: '+ convidados_ordem[0].title() + ', ' + convidados_ordem[1].title() +', '+ convidados_ordem[2].title())
print('essa é a lista de convidados em ordem alfabetica: '+ convidados_reverse[0].title() + ', ' + convidados_reverse[1].title() +', '+ convidados_reverse[2].title())