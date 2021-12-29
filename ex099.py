from time import sleep


def maior(* núm):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in núm:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'--> Foram analisados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(5, 7, 9, 11, 13)
maior(2, 4, 0)
maior(1, 3)
maior(6)
maior()
