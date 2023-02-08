"""
Ingredientes para uma pizza: Escreva um laço que peça ao usuário para
fornecer uma série de ingredientes para uma pizza até que o valor 'quit' seja
fornecido. À medida que cada ingrediente é especificado, apresente uma
mensagem informando que você acrescentará esse ingrediente à pizza.
"""
ingredients_pizza = []
ingredient = ''
message = '\ndigite "quit" para finalizar.'
message += '\nqual ingrediente você quer em sua pizza?'
active = True
while active:
    ingredient = input(message)
    if ingredient != 'quit':
        ingredients_pizza.append(ingredient)
        print(ingredient + ' foi adicionado ao seu pedido')
        print('lista de igredientes: ' + str(ingredients_pizza))
    else:
        active = False