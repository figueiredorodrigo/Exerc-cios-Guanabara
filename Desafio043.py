#cálculo imc

peso = float(input('Quantos kg você pesa? '))
alt = float(input('Qual é a sua altura em metros? '))
imc = peso/(alt ** 2)
print(f'O IMC dessa pessoa é de {imc}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS! Você está na faixa de peso NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA! CUIDADO!')
