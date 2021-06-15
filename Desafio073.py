tabela = ('Vasco', 'Coritiba', 'Flu', 'CAM', 'Fla', 'Corinthians', 'Botafogo', 'Sport', 'Grêmio', 'São Paulo', 'Goiás', 'Inter', 'Palmeiras', 'Braga', 'Bahia', 'Ceará', 'CAP', 'ATL GO', 'Santos', 'Fortaleza')

SãoPaulo = tabela.index('São Paulo') +1

print(f'\nOs primeiros 5 colocados são: {tabela[:5]}'
      f'\nOs ultimos 4 colocados são: {tabela[-4:]}'
      f'\nTimes em ordem alfabética: {sorted(tabela)}'
      f'\nO São Paulo está na {SãoPaulo}ª posição')