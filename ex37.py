def faixa_etaria(idade):
    if idade <= 0:
        return "Idade inválida"
    elif idade < 12:
        return 'Criança'
    elif idade < 17:
        return 'Adolescente'
    else:
        return 'Adulto'
    
while True:
    idade = input('Digite a idade ou SAIR: ')
    if idade.lower() == 'sair':
        break
    print(faixa_etaria(int(idade)))

print('Até mais...')