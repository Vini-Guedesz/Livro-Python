'''
Fatias: Usando um dos programas que você escreveu neste capítulo,
acrescente várias linhas no final do programa que façam o seguinte: • Exiba a
mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia para
exibir os três primeiros itens da lista desse programa.
• Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir
três itens do meio da lista.
• Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para
exibir os três últimos itens da lista.
'''
cube = [value**3 for value in range(1,11)]
print('Os três primeiros itens da lista são:' + str(cube[0:3]))
print('Os itens medianos da lista são:' + str(cube[int(len(cube)/2-1):int(len(cube)/2+1)]))
print('Os três primeiros itens da lista são:' + str(cube[-3:]))