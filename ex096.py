def area(a, b):
    ar = a * b
    print(f'A área desse terreno é: {ar} m2')


print('Controle de Terrenos')
print('--' * 20)
area(a=float(input('Largura [m]: ')), b=float(input('Comprimento [m]: ')))

