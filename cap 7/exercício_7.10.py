"""
Férias dos sonhos: Escreva um programa que faça uma enquete sobre as
férias dos sonhos dos usuários. Escreva um prompt semelhante a este: Se
pudesse visitar um lugar do mundo, para onde você iria? Inclua um bloco de
código que apresente os resultados da enquete.
"""
dream_vacation = {}
active = True
while active:
    name = input('qual é seu nome? ')
    local = input('Se pudesse visitar um lugar do mundo, para onde você iria? ')
    dream_vacation[name] = local
    deactivate = input('gostaria de sair do programa?(sim/não) ')
    if deactivate == 'sim':
        active = False

for name,local in dream_vacation.items():
    print(name + ' gostaria de ir para ' + local)