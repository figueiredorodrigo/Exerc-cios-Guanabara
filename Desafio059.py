from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('OPERAÇÕES '
          '\n \033[1;34;40m[1]\033[m \033[1;34;40m- ADIÇÃO           \033[m '
          '\n \033[1;34;40m[2]\033[m \033[1;34;40m- MULTIPLICAÇÃO    \033[m '
          '\n \033[1;34;40m[3]\033[m \033[1;34;40m- MAIOR            \033[m '
          '\n \033[1;34;40m[4]\033[m \033[1;34;40m- NOVOS NÚMEROS    \033[m '
          '\n \033[1;34;40m[5]\033[m \033[1;34;40m- SAIR DO PROGRAMA \033[m ')
    opcao = int(input('Qual operação vc deseja fazer? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')
    elif opcao == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} é {produto}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida... Tente novamente...')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa. Volte sempre!')


