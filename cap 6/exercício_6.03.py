"""
Glossário: Um dicionário Python pode ser usado para modelar um
dicionário de verdade. No entanto, para evitar confusão, vamos chamá-lo de
glossário.
• Pense em cinco palavras relacionadas à programação que você conheceu
nos capítulos anteriores. Use essas palavras como chaves em seu glossário e
armazene seus significados como valores.
• Mostre cada palavra e seu significado em uma saída formatada de modo
elegante. Você pode exibir a palavra seguida de dois-pontos e depois o seu
significado, ou apresentar a palavra em uma linha e então exibir seu
significado indentado em uma segunda linha. Utilize o caractere de quebra
de linha (\n) para inserir uma linha em branco entre cada par palavrasignificado em sua saída.
"""
glossary = {
    'booleano' : 'Booleano é um tipo de dado lógico que pode assumir apenas dois valores: verdadeiro (true) ou falso (false).',
    'identação' : 'na programação é o processo de alinhar o início de uma linha de código a uma determinada posição para melhorar a legibilidade e organização do código.',
    'algoritmo' : 'Um algoritmo é um conjunto de regras ordenadas e finitas que especificam como resolver um problema ou realizar uma tarefa.',
    'string' : 'Uma string é uma sequência de caracteres.',
    'tuplas' : 'Tuplas são um tipo de estrutura de dados em programação que armazena uma coleção ordenada e imutável de elementos.'
}
print('está aqui o significado da palavra Booleano: ' + glossary['booleano'].title() + '\n')
print('está aqui o significado da palavra Identação: ' + glossary['identação'].title() + '\n')
print('está aqui o significado da palavra Algoritmo: ' + glossary['algoritmo'].title() + '\n')
print('está aqui o significado da palavra String: ' + glossary['string'].title() + '\n')
print('está aqui o significado da palavra Tuplas: ' + glossary['tuplas'].title())