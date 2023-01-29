'''
Mais convidados: Você acabou de encontrar uma mesa de jantar maior,
portanto agora tem mais espaço disponível. Pense em mais três convidados
para o jantar.
• Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
uma instrução print no final de seu programa informando às pessoas que
você encontrou uma mesa de jantar maior.
• Utilize insert() para adicionar um novo convidado no início de sua lista.
• Utilize insert() para adicionar um novo convidado no meio de sua lista.
• Utilize append() para adicionar um novo convidado no final de sua lista.
• Exiba um novo conjunto de mensagens de convite, uma para cada pessoa
que está em sua lista
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