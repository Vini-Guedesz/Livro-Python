"""
Cidades: Crie um dicionário chamado cities. Use os nomes de três
cidades como chaves em seu dicionário. Crie um dicionário com informações
sobre cada cidade e inclua o país em que a cidade está localizada, a
população aproximada e um fato sobre essa cidade. As chaves do dicionário
de cada cidade devem ser algo como country, population e fact. Apresente o
nome de cada cidade e todas as informações que você armazenou sobre ela.
"""
cities = {
    
    'são luís' : {
        'contry' : 'brasil',
        'population' : 1109000,
        'fact' : 'é uma das duas cipitais brasileiras que estão localizadas em ilhas'  
    },
    
    'são paulo' : {
        'contry' : 'brasil',
        'population' : 12180000,
        'fact' : 'é uma das maiores metrópoles do mundo'
    },
    
    'rio de janeiro' : {
        'contry' : 'brasil',
        'population' : 6748000,
        'fact' : 'foi projetada para ser a primeira capital do brasil'
    }
}

for city, info in cities.items():
    print(city + ':' + str(info))