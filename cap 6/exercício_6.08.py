"""
Animais de estimação: Crie vários dicionários, em que o nome de cada
dicionário seja o nome de um animal de estimação. Em cada dicionário, inclua
o tipo do animal e o nome do dono. Armazene esses dicionários em uma lista
chamada pets. Em seguida, percorra sua lista com um laço e, à medida que
fizer isso, apresente tudo que você sabe sobre cada animal de estimação
"""
colt = {
    'breed' : 'cachorro',
    'owner' : 'victor',
    'vacinado' : True
}
rengar = {
    'breed' : 'gato',
    'owner' : 'vinicius',
    'vacinado' : True
}
atena = {
    'breed' : 'cachorro',
    'owner' : 'walter',
    'vacinado' : False
}
list_pets = [colt, rengar, atena]
for pet in list_pets:
    print(pet)