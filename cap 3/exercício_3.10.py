'''
Todas as funções: Pensa em algo que você poderia armazenar em uma
lista. Por exemplo, você poderia criar uma lista de montanhas, rios, países,
cidades, idiomas ou qualquer outro item que quiser. Escreva um programa que
crie uma lista contendo esses itens e então utilize cada função apresentada
neste capítulo pelo menos uma vez.
'''
wedding_guests = ['andy', 'louis', 'suzy', 'harry']
wedding_guests.insert(2, 'marcos')
del wedding_guests[0]
wedding_guests.pop(-1)
reverse_guests = sorted(wedding_guests, reverse=True)
sorted_guests = sorted(wedding_guests)
print('ao total são '+ str(len(wedding_guests)) + ' convidados!!!')
print('essa é a lista de convidados em ordem alfabetica: '+ sorted_guests[0].title() + ', ' + sorted_guests[1].title() +', '+ sorted_guests[2].title())
print('essa é a lista de convidados em ordem reversa: '+ reverse_guests[0].title() + ', ' + reverse_guests[1].title() +', '+ reverse_guests[2].title())