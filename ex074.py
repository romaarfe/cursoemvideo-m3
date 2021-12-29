from random import randint
aleatorio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os números gerados aleatoriamente foram: ', end='')
for n in aleatorio:
    print(f'{n} ', end='')
print(f'\nO maior número sorteado foi: {max(aleatorio)}')
print(f'O menor número sorteado foi: {min(aleatorio)}')
