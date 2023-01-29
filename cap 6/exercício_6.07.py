'''
Pessoas: Comece com o programa que você escreveu no Exercício 6.1 .
Crie dois novos dicionários que representem pessoas diferentes e
armazene os três dicionários em uma lista chamada people. Percorra sua lista
de pessoas com um laço. À medida que percorrer a lista, apresente tudo que
você sabe sobre cada pessoa.

'''

user_marcos = {
    'first_name' : 'marcos',    
    'last_name' : 'guedes',
    'age' : 18,
    'city' : 'saint louis'
}
user_igor = {
    'first_name' : 'igor',
    'last_name' : 'santos',
    'age' : 24,
    'city' : 'são paulo'
}
user_fabio = {
    'first_name' : 'ramon',
    'last_name' : 'torres',
    'age' : 14,
    'city' : 'santos'
}
user_gabriel = {
    'first_name' : 'gabriel',
    'last_name' : 'silva',
    'age' : 30,
    'city' : 'imperatriz'
}
list_peoples = [user_marcos, user_igor, user_fabio, user_gabriel]
for peoples in list_peoples:
    print(peoples)