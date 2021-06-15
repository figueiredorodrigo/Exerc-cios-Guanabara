while True:
    n = int(input('Deseja ver a tabuada de qual número? Número negativo para interromper: '))
    print(f'---'*15)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE! ')