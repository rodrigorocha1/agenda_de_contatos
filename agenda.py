AGENDA = {}

AGENDA['Rodrigo'] = {
    'telefone': '99999999',
    'email': 'email@email.com',
    'endereco': 'AV1'
}

AGENDA['Maria'] = {
    'telefone': '99999999',
    'email': 'email@email.com',
    'endereco': 'AV1'
}


def mostrar_contatos():
    for contato in AGENDA:
        buscar_contato(contato)


def buscar_contato(contato):
    print('Nome:', contato)
    print('TELEFONE:', AGENDA[contato]['telefone'])
    print('EMAIL:', AGENDA[contato]['email'])
    print('ENDEREÇO:', AGENDA[contato]['endereco'])
    print('##')


def incluir_editado_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco
    }


def excluir_contato(contato):
    AGENDA.pop(contato)


def imprimir_menu():
    print('1 - Mostrar contatos')
    print('2 - Buscar')
    print('3 - Incluir')
    print('4 - Editar')
    print('5 - Excluir')
    print('0 - Fechar')


while True:
    imprimir_menu()
    op = ('Escolha uma opção')
    if op == '1':
        mostrar_contatos()
    elif op == '2':
        contato = input('Digite o nome do contato: ')
        buscar_contato(contato)
    elif op == '3' or op == '4':
        contato = input('Digite o nome do contato: ')
        telefone = input('Digite o nome do telefone: ')
        email = input('Digite o nome do email: ')
        endereco = input('Digite o nome do endereco: ')
        incluir_editado_contato(contato, telefone, email, endereco)
    elif op == '5':
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)
    elif op == '0':
        print('fechando programa')
        exit()
    else:
        print('Op Inválida')
