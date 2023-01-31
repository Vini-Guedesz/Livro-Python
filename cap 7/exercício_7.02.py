"""
Lugares em um restaurante: Escreva um programa que pergunte ao usuário
quantas pessoas estão em seu grupo para jantar. Se a resposta for maior que
oito, exiba uma mensagem dizendo que eles deverão esperar uma mesa. Caso
contrário, informe que sua mesa está pronta.
"""
peoples = input('deseja uma mesa para quantas pessoas?')
if int(peoples) > 8:
    print('espere enquanto preparamos sua mesa.')
else:
    print('sua mesa está pronta.')