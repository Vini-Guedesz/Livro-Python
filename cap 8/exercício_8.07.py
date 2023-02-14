"""
Álbum: Escreva uma função chamada make_album() que construa um
dicionário descrevendo um álbum musical. A função deve aceitar o nome de um
artista e o título de um álbum e deve devolver um dicionário contendo essas
duas informações. Use a função para criar três dicionários que representem
álbuns diferentes. Apresente cada valor devolvido para mostrar que os
dicionários estão armazenando as informações do álbum corretamente.
Acrescente um parâmetro opcional em make_album() que permita armazenar
o número de faixas em um álbum. Se a linha que fizer a chamada incluir um
valor para o número de faixas, acrescente esse valor ao dicionário do álbum.
Faça pelo menos uma nova chamada da função incluindo o número de faixas
em um álbum
"""
def make_album(singer, title_album, num_of_trakes='não informado'):
    album = {
        'nome do cantor(a)' : singer,
        'titulo do álbum' : title_album,
        'número de faixas' : num_of_trakes,
    }
    return(album)

print(make_album('billie', 'happy than ever', 16))
print(make_album('baco exu do blues', 'exu'))
print(make_album('djonga', 'nu'))