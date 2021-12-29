tupla = (int(input('Digite um número: ')),
         int(input('Digite um número: ')),
         int(input('Digite um número: ')),
         int(input('Digite um número: ')))
print(tupla)
print(f'O número 9 aparece {tupla.count(9)} vez(es).')
if 3 in tupla:
    print(f'O número 3 aparece pela primeira vez na {tupla.index(3)+1}ª posição.')
else:
    print('O número 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
