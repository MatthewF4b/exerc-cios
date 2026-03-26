opc = int(input('Cadastrar\n2-Alterar\n3-Excluir\n4-Sair'))

match opc:
    case 1:
        print('Cadastro realizado')
    case 2:
        print('Alteração realizada')
    case 3:
        print('Exclusão realizada')
    case 4:
        print('Você optou por sair')
    case _ :
        print('Opção inválida')