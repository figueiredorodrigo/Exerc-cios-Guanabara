#calculo preço e forma de pgmnto

pgmnt = int(input('Qual será a forma de pagamento?\n [1] - A vista dinheiro/cheque\n [2] - Á vista no cartão\n [3] - 2x no cartão\n [4] - 3x ou mais '))

prc = float(input('Qual é o preço do produto? '))

if pgmnt == 1:
    print(f'À vista no dinheiro/cheque, você terá 10% de desconto, então o valor do produto será R$ {prc - (prc*0.1)} ')
elif pgmnt == 2:
    print(f'À vista no cartão, o desconto é de 5%, ou seja, o preço será de R${prc - (prc*0.5)}')
elif pgmnt == 3:
    print('Sem descontos')
elif pgmnt == 4:
    print(f'20% de juros, o preço será R${prc + (prc*0.2)} ')
else:
    print('Você digitou um número que não corresponde a uma forma de pagamento')