"""
Álbuns dos usuários: Comece com o seu programa do Exercício 8.7.
Escreva um laço while que permita aos usuários fornecer o nome de um artista e
o título de um álbum. Depois que tiver essas informações, chame make_album()
com as entradas do usuário e apresente o dicionário criado. Lembre-se de incluir
um valor de saída no laço while.
"""
def make_album(singer, title_album, num_of_trakes='não informado'):
    album = {
        'nome do cantor(a)' : singer,
        'titulo do álbum' : title_album,
        'número de faixas' : num_of_trakes,
    }
    return(album)

while True:
    print('coloque as informações sobre o álbum:')
    singers = input('nome do artista: ')
    title = input('titulo do álbum: ')
    number_tracks = input('número de músicas: ')
    dic_album = make_album(singers, title, number_tracks)
    print(dic_album)
    exit = input('deseja sair do programa? sim/não')
    if exit == 'sim':
        break