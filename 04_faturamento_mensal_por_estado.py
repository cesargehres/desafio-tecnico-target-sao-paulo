def calcular_porcentagem(valor, valor_total):
    porcentagem = (valor / valor_total) * 100
    return porcentagem


#lista dos estados e respectivos faturamentos arrecadados
faturamento_dos_estados = [{'estado': 'SP', 'faturamento': 67836.43},
                           {'estado': 'RJ', 'faturamento': 36678.66},
                           {'estado': 'MG', 'faturamento': 29229.88},
                           {'estado': 'ES', 'faturamento': 27165.48},
                           {'estado': 'Outros', 'faturamento': 19849.53}]


#Faturamento total
faturamento_total = 0

for faturamento in faturamento_dos_estados:
    faturamento_total += faturamento['faturamento']


#imprimindo tabela com a porcentagem do faturameto dos estados
print(f'{"Valor Total:":<15} {faturamento_total:>25.2f}\n')
print('Porcentagem que cada estado arrecadou')
print(41 * '-')
print(f'{"Estado":<15} {"Porcentagem":>25}')

for faturamento in faturamento_dos_estados:
    porcentagem = calcular_porcentagem(faturamento['faturamento'], faturamento_total)
    print(f'{faturamento["estado"]:<15} {porcentagem:>25.2f}')
