from data import data3

max = 0
min = data3[0]['valor']
soma = 0
cont = 0

for dia in data3:
    if dia['valor'] > max:
        max = dia['valor']
    if dia['valor'] < min and dia['valor'] != 0:
        min = dia['valor']
    soma += dia['valor']

for dia in data3:
    if dia['valor'] > soma / 30:
        cont += 1

print(f'menor faturamento: {min}')
print(f'maior faturamento: {max}')
print(f'dias com faturamento acima da média: {cont}')