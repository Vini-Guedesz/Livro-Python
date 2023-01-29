"""
Glossário 2: Agora que você já sabe como percorrer um dicionário com
um laço, limpe o código do Exercício 6.3, substituindo sua
sequência de instruções print por um laço que percorra as chaves e os valores
do dicionário. Quando tiver certeza de que seu laço funciona, acrescente mais
cinco termos de Python ao seu glossário. Ao executar seu programa novamente,
essas palavras e significados novos deverão ser automaticamente incluídos na
saída.
"""
glossary = {
    'booleano' : 'Booleano é um tipo de dado lógico que pode assumir apenas dois valores: verdadeiro (true) ou falso (false).',
    'identação' : 'na programação é o processo de alinhar o início de uma linha de código a uma determinada posição para melhorar a legibilidade e organização do código.',
    'algoritmo' : 'Um algoritmo é um conjunto de regras ordenadas e finitas que especificam como resolver um problema ou realizar uma tarefa.',
    'string' : 'Uma string é uma sequência de caracteres.',
    'tuplas' : 'Tuplas são um tipo de estrutura de dados em programação que armazena uma coleção ordenada e imutável de elementos.',
    'float' : '"Float" é uma abreviação de "floating point", que é um tipo de dado numérico utilizado em programação para representar números reais.',
    'int' : '"int" é uma abreviação de "integer", que é um tipo de dado numérico utilizado em programação para representar números inteiros, ou seja, números sem casas decimais.',
    'key' : 'Chave de dicionário: em linguagens de programação que suportam dicionários, uma chave é um valor usado para acessar um item específico no dicionário.',
    'value' : 'Valor de dicionário: em linguagens de programação que suportam dicionários, um valor é o item armazenado no dicionário que é associado a uma chave específica.',
    'dicionário' : 'Um dicionário é uma estrutura de dados que permite armazenar e recuperar informações usando chaves.',
}
for key, value in glossary.items():
    print('siginificado da palavra '+ key + ': ' + value)