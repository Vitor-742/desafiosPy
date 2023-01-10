estado = input('''
    Qual estado deseja saber a porcentagem de faturamento?
    1 - SP 
    2 - RJ 
    3 - MG 
    4 - ES 
    5 - Outros
    ''')

aux = {
    '1': 6783643,
    '2': 3667866,
    '3': 2922988,
    '4': 2716548,
    '5': 1984953
}

print(round(aux[estado] / 18075998 * 100, 2), '%')
