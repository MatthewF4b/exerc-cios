def validar(frase):
    return frase != ''

arq = open('dados.txt', 'w', encoding='utf-8')

#w abre e apaga
#a adiciona
#r lê

while True:
    frase = input('Digite algo: ')
    if frase.lower() == 'sair':
        break
    
    if validar(frase) == False:
        print('Frase errada')
        continue
    

    arq.write(frase + '\n')

arq.close()