"""
Rios: Crie um dicionário que contenha três rios importantes e o país que
cada rio corta. Um par chave-valor poderia ser 'nilo': 'egito'.
• Use um laço para exibir uma frase sobre cada rio, por exemplo, O Nilo corre
pelo Egito.
• Use um laço para exibir o nome de cada rio incluído no dicionário.
• Use um laço para exibir o nome de cada país incluído no dicionário.
"""
rivers = {
    'amazonas' : 'brasil',
    'nilo' : 'egito',
    'mississipi' : 'estados unidos',
    'volga' : 'russia',
    'reno' : 'alemanha',
}

for river, contry in rivers.items():
    print('o rio ' + river + ' corre pelo(a) ' + contry.title())
    print(river)
    print(contry)