'''
Reduzindo a lista de convidados: Você acabou de descobrir que sua nova
mesa de jantar não chegará a tempo para o jantar e tem espaço para somente
dois convidados.
• Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que
mostre uma mensagem informando que você pode convidar apenas duas
pessoas para o jantar.
• Utilize pop() para remover os convidados de sua lista, um de cada vez, até
que apenas dois nomes permaneçam em sua lista. Sempre que remover um
nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela
saiba que você sente muito por não poder convidá-la para o jantar.
• Apresente uma mensagem para cada uma das duas pessoas que continuam
na lista, permitindo que elas saibam que ainda estão convidadas.
• Utilize del para remover os dois últimos nomes de sua lista, de modo que você
tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem
uma lista vazia no final de seu programa.
'''
guests = ['michael jackson', 'stan lee', 'andy samberg']

print(guests[0].title()+ ', você está convidado(a) para um jantar!!!')
print(guests[1].title()+ ', você está convidado(a) para um jantar!!!')
print(guests[2].title()+ ', você está convidado(a) para um jantar!!!')

print("foi encontrado uma mesa maior, irá haver mais convidados!!")

guests.insert(0, 'Whinderson')
guests.insert(2, 'filime dechamps')
guests.append('guanabara')

print(guests[0].title()+ ', você está convidado(a) para um jantar!!!')
print(guests[1].title()+ ', você está convidado(a) para um jantar!!!')
print(guests[2].title()+ ', você está convidado(a) para um jantar!!!')
print(guests[3].title()+ ', você está convidado(a) para um jantar!!!')
print(guests[4].title()+ ', você está convidado(a) para um jantar!!!')
print(guests[5].title()+ ', você está convidado(a) para um jantar!!!')

print('infelizmente as mesas não chegaram a tempo. Só podemos ter 2 convidados.')

print(guests[0]+ ', infelizmente você não poderá ser convidado para o jantar, sinto muito!')
guests.pop(0)

print(guests[0]+ ', infelizmente você não poderá ser convidado para o jantar, sinto muito!')
guests.pop(0)

print(guests[0]+ ', infelizmente você não poderá ser convidado para o jantar, sinto muito!')
guests.pop(0)

print(guests[0]+ ', infelizmente você não poderá ser convidado para o jantar, sinto muito!')
guests.pop(0)

print(guests[0].title()+ ', você permanece convidado(a) para um jantar!!!')
print(guests[1].title()+ ', você permanece convidado(a) para um jantar!!!')

del guests[0]
del guests[0]
print(guests)