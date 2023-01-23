'''
Removendo caracteres em branco de nomes: Armazene o nome de uma
pessoa e inclua alguns caracteres em branco no início e no final do nome.
Lembre-se de usar cada combinação de caracteres, "\t" e "\n", pelo menos
uma vez.
'''
nome = "\tVinicius\nGuedes"
print(nome)

nome = nome.rstrip()
print(nome)

nome = nome.lstrip()
print(nome)

nome = nome.strip()
print(nome)