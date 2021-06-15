# Somatório de impares, multiplos de 3 entre 1 e 500
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'O somatório dos {cont} números múltiplos de 3, entre 1 e 500 é: {soma}')
