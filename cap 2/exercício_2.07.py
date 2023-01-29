'''
Removendo caracteres em branco de nomes: Armazene o nome de uma
pessoa e inclua alguns caracteres em branco no início e no final do nome.
Lembre-se de usar cada combinação de caracteres, "\t" e "\n", pelo menos
uma vez.
'''
name = "\tVinicius\nGuedes"
print(name)

name = name.rstrip()
print(name)

name = name.lstrip()
print(name)

name = name.strip()
print(name)