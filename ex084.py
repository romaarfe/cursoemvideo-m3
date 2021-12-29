pessoas = list()
dado = list()
pesado = leve = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        pesado = leve = dado[1]
    else:
        if dado[1] > pesado:
            pesado = dado[1]
        if dado[1] < leve:
            leve = dado[1]

    pessoas.append(dado[:])
    dado.clear()

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'A) Foram cadastradas {len(pessoas)} pessoas.')
print(f'B) O maior peso foi de {pesado}Kg. De ', end='')
for p in pessoas:
    if p[1] == pesado:
        print(f'{p[0]}...', end='')
print()
print(f'C) O menor peso foi de {leve}Kg. De ', end='')
for p in pessoas:
    if p[1] == leve:
        print(f'{p[0]}... ', end='')
print()
