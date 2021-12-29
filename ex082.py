valores = list()
pares = list()
impares = list()
while True:
    v = int(input('Digite um valor: '))
    valores.append(v)
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Os valores digitados são: {valores}')
print(f'A lista com os valores pares é: {pares}')
print(f'A lista com os valores ímpares é: {impares}')
