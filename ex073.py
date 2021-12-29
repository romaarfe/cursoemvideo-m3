brasileirao = ('Atlético-MG', 'Flamengo', 'Fortaleza', 'Palmeiras', 'Bragantino', 'Corinthians', 'Internacional',
              'Fluminense', 'Cuiabá', 'Atlético-PR', 'Atlético-GO', 'São Paulo', 'América-MG', 'Ceará SC', 'Santos',
              'Bahia', 'Juventude', 'Sport Recife', 'Grêmio', 'Chapecoense')
print(f'A lista de times na tabela do Brasileirão, são: {brasileirao}.')
print(' » «' * 30)
print(f'Os cinco primeiros colocados são: {brasileirao[0:5]}.')
print(' » «' * 30)
print(f'Os últimos quatro colocados da tabela são: {brasileirao[-4:]}')
print(' » «' * 30)
print(f'Os times em ordem alfabética são: {sorted(brasileirao)}')
print(' » «' * 30)
print(f'Chapecoense está na {brasileirao.index("Chapecoense")+1}ª posiçao da tabela')
