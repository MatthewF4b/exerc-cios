soma = 0
cont = 0

while True:
    n = int(input('Digite n: '))
    if n == 0:
        break
    soma += n
    cont += 1

if cont > 0:
    print(f'A média é: {soma/cont}')
else:
    print('Não há média a ser calculada')