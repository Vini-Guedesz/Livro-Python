'''
Mais testes condicionais: Você não precisa limitar o número de testes que
criar em dez. Se quiser testar mais comparações, escreva outros testes e
acrescente-os em conditional_tests.py. Tenha pelo menos um resultado True e um
False para cada um dos casos a seguir:
• testes de igualdade e de não igualdade com strings;
• testes usando a função lower();
• testes numéricos que envolvam igualdade e não igualdade, maior e menor que,
maior ou igual a e menor ou igual a;
• testes usando as palavras reservadas and e or;
• testes para verificar se um item está em uma lista;
• testes para verificar se um item não está em uma lista.
'''
carro = 'bmw'
nome_propietario = 'Vini'
idade_propetario = 18
preco_carro = 190000
km_rodado = 30000
ex_propietarios = ['ruan', 'itallo', 'luis']

print('carro é uma bmw?')
print(carro == 'BMW')

print('carro é um diferente de uma ferrari?')
print(carro != 'ferrari')

print('o nome do é propetário é Vini?')
print(nome_propietario.lower() == 'vini')

print('o propietário é maior de idade?')
print(idade_propetario >= 18)

print('o propietário tem idade difente de 25 anos?')
print(idade_propetario != 25)

print('o propietário tem idade igual à 18?')
print(idade_propetario == 18)

print('o carro custou menos do que 1 milhão?')
print(preco_carro < 1000000)

print('o carro custou mais do que 100 mil?')
print(preco_carro > 100000)

print('este carro já teve como mais de um dono antes do atual ou tem mais de 100 mil km rodado?')
print(len(ex_propietarios)>1 or km_rodado > 100000)

print('itallo e luis são ex propietários?')
print('luis' and 'itallo' in ex_propietarios)

print('marcos é um ex propietário?')
print('marcos' in ex_propietarios)

print('marcos não é um ex propietário?')
print('marcos' not in ex_propietarios)