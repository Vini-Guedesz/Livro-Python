"""
Sem usuários: Acrescente um teste if em hello_admin.py para garantir
que a lista de usuários não esteja vazia.
• Se a lista estiver vazia, mostre a mensagem Precisamos encontrar alguns
usuários!
• Remova todos os nomes de usuário de sua lista e certifique-se de que a
mensagem correta seja exibida.
"""
users = []
if users == []:
    print('sem usuarios cadastrados.')
else:
    for user in users:
        if user == 'admin':
            print('bem vindo a tela de comando!!!')
        else:
            print('bem vindo, ' + user.title() + ', obrigado por fazer login!!!')