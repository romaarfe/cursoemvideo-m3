valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break
valores.sort(reverse=True)
print(f'A) Foram digitados {len(valores)} elementos.')
print(f'B) A lista de valores em ordem descrescente é: {valores}')
for c, v in enumerate(valores):
    if v == 5:
        print(f'C) O número 5 foi encontrado na {c+1}ª posição.')
if 5 not in valores:
    print('C) O número 5 não foi digitado, logo não se encontra na lista.')
