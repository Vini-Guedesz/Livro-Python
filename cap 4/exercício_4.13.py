'''
Buffet: Um restaurante do tipo buffet oferece apenas cinco tipos básicos
de comida. Pense em cinco pratos simples e armazene-os em uma tupla.
• Use um laço for para exibir cada prato oferecido pelo restaurante.
• Tente modificar um dos itens e cerifique-se de que Python rejeita a mudança.
• O restaurante muda seu cardápio, substituindo dois dos itens com pratos
diferentes. Acrescente um bloco de código que reescreva a tupla e, em
seguida, use um laço for para exibir cada um dos itens do cardápio
revisado.
'''
pratos = ('pizza', 'pastel', 'feijoada', 'strogonoff', 'hamburguer')
for prato in pratos:
    print(prato)
    
#pratos[0] = 'arroz'

pratos = ('pizza', 'pastel', 'feijoada', 'arroz', 'sopa')
for prato in pratos:
    print(prato)