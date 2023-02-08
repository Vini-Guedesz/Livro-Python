"""
ingressos para o cinema: Um cinema cobra preços diferentes para os
ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos
de 3 anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o
ingresso custará 10 dólares; se tiver mais de 12 anos, o ingresso custará 15
dólares. Escreva um laço em que você pergunte a idade aos usuários e, então,
informe-lhes o preço do ingresso do cinema.
"""
message = '\ndigite "quit" para sair.'
message += '\ndigite sua idade:'
active = True
while active:
    age = input(message)
    if age != "quit":
        if int(age) < 3:
            print('seu ingresso é grátis')
        elif int(age) >= 3 and int(age) <= 12:
            print('seu ingresso é custa 10 dólares')
        elif int(age) > 12:
            print('seu ingresso é custa 15 dólares')
    else:
        active = False