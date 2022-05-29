times = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Flamengo', 'Bragantino', 'Corinthians',
         'Internacional', 'Fluminense', 'Athetico-PR', 'Cuiába', 'Ceará-SC', 'Atletico_GO',
         'São Paulo', 'Juventude', 'América-MG', 'Santos', 'Bahia', 'Gremio', 'Sport-Recife',
         'Chapecoence')

print('-'*40)
print('==== CAMPEONATO BRASILEIRO - 2021 =====')
print('-'*40)
print(f'A lista de times: {times}')
print('-'*40)
print(f'Os primeiros 5 colocados são: {times[:5]}')
print('-'*40)
print(f'Os últimos 4 colocados são: {times[-4:]}')
print('-'*40)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('-'*40)
print(f'O Chapecoence está na {times.index("Chapecoence") + 1}ª posição')
