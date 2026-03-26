nota = float(input('Nota: '))
freq = float(input('Freq: '))

'''if nota >= 7 and freq >= 75:
    print('Aprovado')
elif nota >= 5 and freq >= 75:
    print ('AF')
else:
    print('DP')'''

if freq < 75:
    print('Reprovado por falta')
elif nota >= 7:
    print('Aprovado')
elif nota >= 5:
    print('AF')
else:
    print('dp')