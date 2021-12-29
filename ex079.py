valores = list()
while True:
    v = int(input('Digite um valor: '))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado. Este não será adicionado!')
    continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if continuar in 'N':
        break
valores.sort()
print(f'Os valores únicos digitados em ordem crescente são: {valores}')
