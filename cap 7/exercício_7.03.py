"""
Múltiplos de dez: Peça um número ao usuário e, em seguida, informe se o
número é múltiplo de dez ou não.
"""
num = input('informe um número: ')
if int(num) % 10 == 0:
    print("este número é múltiplo de dez.")
else:
    print("este número não é múltiplo de dez.")