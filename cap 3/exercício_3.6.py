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
convidados = ['michael jackson', 'stan lee', 'andy samberg']

print(convidados[0].title()+ ', você está convidado(a) para um jantar!!!')
print(convidados[1].title()+ ', você está convidado(a) para um jantar!!!')
print(convidados[2].title()+ ', você está convidado(a) para um jantar!!!')

print("foi encontrado uma mesa maior, irá haver mais convidados!!")

convidados.insert(0, 'Whinderson')
convidados.insert(2, 'filime dechamps')
convidados.append('guanabara')

print(convidados[0].title()+ ', você está convidado(a) para um jantar!!!')
print(convidados[1].title()+ ', você está convidado(a) para um jantar!!!')
print(convidados[2].title()+ ', você está convidado(a) para um jantar!!!')
print(convidados[3].title()+ ', você está convidado(a) para um jantar!!!')
print(convidados[4].title()+ ', você está convidado(a) para um jantar!!!')
print(convidados[5].title()+ ', você está convidado(a) para um jantar!!!')