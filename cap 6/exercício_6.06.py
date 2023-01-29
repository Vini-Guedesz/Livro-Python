"""
Enquete: Utilize o código em favorite_languages.py (página 150).
• Crie uma lista de pessoas que devam participar da enquete sobre linguagem
favorita. Inclua alguns nomes que já estejam no dicionário e outros que não
estão.
• Percorra a lista de pessoas que devem participar da enquete. Se elas já
tiverem respondido à enquete, mostre uma mensagem agradecendo-lhes por
responder. Se ainda não participaram da enquete, apresente uma mensagem
convidando-as a responder.
"""
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
list_new_peoples = ['sarah', 'guto', 'matheus', 'rafa', 'jen']

for name in favorite_languages.keys():
    if name in list_new_peoples:
        print(name.title() + ', muito obrigado por participar da pesquisa.')
    else:
        print(name.title() + ', você está disponível para participar da nossa pesquisa?')