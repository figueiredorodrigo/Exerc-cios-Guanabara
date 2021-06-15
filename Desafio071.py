'''
CAIXA ELETRONICO
VALOR SACADO
CEDULAS DE CADA VALOR QUE SERÃO ENTREGUE
'''

print('=' * 10)
print(f'BANCO JAPA')
print('=' * 10)
valor = int(input('Que valor você deseja sacar? '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 20)
print('Volte sempre ao BANCO JAPA! Tenha um bom dia!')
