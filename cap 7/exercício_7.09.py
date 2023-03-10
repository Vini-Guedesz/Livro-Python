"""
Sem pastrami: Usando a lista sandwich_orders do Exercício 7.8, garanta
que o sanduíche de 'pastrami' apareça na lista pelo menos três vezes.
Acrescente um código próximo ao início de seu programa para exibir uma
mensagem informando que a lanchonete está sem pastrami e, então, use um
laço while para remover todas as ocorrências de 'pastrami' e
sandwich_orders. Garanta que nenhum sanduíche de pastrami acabe em
finished_sandwiches.
"""
sandwich_orders = ['extra bacon', 'mexicano', 'apimentado', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []
print('desculpe, não temos mais sanduiches de pastrami')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('estamos preparando seu sanduiche ' + sandwich + '.')
    finished_sandwiches.append(sandwich)
    
print('sanduiches prontos:'  + str(finished_sandwiches))